"""gRPC client for cautem-gateway and the pinned OpenShell contract."""

from __future__ import annotations

import os
import uuid
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from urllib.parse import urlparse

import grpc
import httpx

from .control.v1 import console_pb2, console_pb2_grpc
from ._proto.openshell import openshell_pb2, openshell_pb2_grpc


class ConnectUnsupported(RuntimeError):
    """Interactive connect stays on the CLI (`cautem connect <name>`)."""


@dataclass
class Sandbox:
    name: str
    status: str = ""
    id: str = ""
    image: str = ""
    workspace: str = "default"
    resource_version: int = 0
    labels: Dict[str, str] = field(default_factory=dict)
    command: List[str] = field(default_factory=list)


@dataclass
class ExecResult:
    exit_code: int
    output: str


class Client:
    """Uses native gRPC for resources and OpenShell execution RPCs."""

    def __init__(
        self,
        base_url: str,
        timeout: float = 70.0,
        token: Optional[str] = None,
        workspace: str = "default",
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.workspace = workspace or "default"
        bearer = (
            token
            if token is not None
            else os.getenv("CAUTEM_GATEWAY_TOKEN", "")
        ).strip()
        self._metadata = (("authorization", f"Bearer {bearer}"),) if bearer else ()
        self._http = httpx.Client(base_url=self.base_url, timeout=timeout)
        self._channel: Optional[grpc.Channel] = None

    def close(self) -> None:
        self._http.close()
        if self._channel is not None:
            self._channel.close()
            self._channel = None

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def _rpc(self) -> grpc.Channel:
        if self._channel is not None:
            return self._channel
        endpoint = urlparse(self.base_url)
        if not endpoint.hostname or endpoint.path or endpoint.query or endpoint.fragment:
            raise ValueError("gateway URL must contain only scheme and authority")
        target = endpoint.netloc
        if endpoint.scheme == "https":
            self._channel = grpc.secure_channel(
                target, grpc.ssl_channel_credentials()
            )
        elif endpoint.scheme == "http":
            host = endpoint.hostname.lower()
            if host != "localhost" and not host.endswith(".localhost"):
                import ipaddress

                if not ipaddress.ip_address(host).is_loopback:
                    raise ValueError("unencrypted gRPC is allowed only for loopback gateways")
            self._channel = grpc.insecure_channel(target)
        else:
            raise ValueError(f"unsupported gateway URL scheme: {endpoint.scheme!r}")
        return self._channel

    def _call(self, method, request):
        return method(request, timeout=self.timeout, metadata=self._metadata)

    def healthz(self) -> Dict[str, object]:
        """Check liveness over the transport-specific HTTP health endpoint."""
        response = self._http.get("/healthz")
        response.raise_for_status()
        return response.json()

    def info(self) -> Dict[str, object]:
        """Return the caller-visible overview and advertised capabilities."""
        console = console_pb2_grpc.ConsoleServiceStub(self._rpc())
        overview = self._call(
            console.GetOverview,
            console_pb2.GetOverviewRequest(workspace=self.workspace),
        )
        capabilities = self._call(
            console.GetConsoleCapabilities,
            console_pb2.GetConsoleCapabilitiesRequest(),
        )
        return {
            "gateway_id": overview.gateway_id,
            "workspace": overview.workspace,
            "sandbox_count": overview.sandbox_count,
            "runtime_status_available": overview.runtime_status_available,
            "compute_drivers": list(capabilities.compute_drivers),
            "sandbox_lifecycle_available": capabilities.sandbox_lifecycle_available,
        }

    def create(self, sb: Sandbox) -> None:
        if not sb.name:
            raise ValueError("sandbox name required")
        if not sb.image:
            raise ValueError("sandbox image required")
        stub = console_pb2_grpc.SandboxServiceStub(self._rpc())
        self._call(
            stub.CreateSandbox,
            console_pb2.CreateSandboxRequest(
                workspace=sb.workspace or self.workspace,
                name=sb.name,
                image=sb.image,
                command=sb.command,
                labels=sb.labels,
                request_id=uuid.uuid4().hex,
            ),
        )

    def list(self) -> List[Sandbox]:
        stub = console_pb2_grpc.SandboxServiceStub(self._rpc())
        token = ""
        items: List[Sandbox] = []
        while True:
            response = self._call(
                stub.ListSandboxes,
                console_pb2.ListSandboxesRequest(
                    workspace=self.workspace, page_size=1000, page_token=token
                ),
            )
            items.extend(_sandbox_from_summary(item) for item in response.sandboxes)
            token = response.next_page_token
            if not token:
                return items

    def get(self, name: str) -> Sandbox:
        stub = console_pb2_grpc.SandboxServiceStub(self._rpc())
        response = self._call(
            stub.GetSandbox,
            console_pb2.GetSandboxRequest(workspace=self.workspace, name=name),
        )
        return _sandbox_from_summary(response.sandbox)

    def delete(self, name: str) -> None:
        stub = console_pb2_grpc.SandboxServiceStub(self._rpc())
        current = self.get(name)
        self._call(
            stub.DeleteSandbox,
            console_pb2.DeleteSandboxRequest(
                workspace=current.workspace,
                name=current.name,
                expected_resource_version=current.resource_version,
                request_id=uuid.uuid4().hex,
            ),
        )

    def exec(self, name: str, *argv: str) -> ExecResult:
        if not name or not argv:
            raise ValueError("usage: exec(name, *argv)")
        stub = openshell_pb2_grpc.OpenShellStub(self._rpc())
        sandbox = self._call(
            stub.GetSandbox,
            openshell_pb2.GetSandboxRequest(name=name, workspace=self.workspace),
        ).sandbox
        stream = stub.ExecSandbox(
            openshell_pb2.ExecSandboxRequest(sandbox_id=sandbox.metadata.id, command=list(argv)),
            timeout=self.timeout,
            metadata=self._metadata,
        )
        output: List[bytes] = []
        exit_code = -1
        for event in stream:
            payload = event.WhichOneof("payload")
            if payload == "stdout":
                output.append(event.stdout.data)
            elif payload == "stderr":
                output.append(event.stderr.data)
            elif payload == "exit":
                exit_code = event.exit.exit_code
        return ExecResult(exit_code=exit_code, output=b"".join(output).decode(errors="replace"))

    def connect(self, name: str) -> None:
        raise ConnectUnsupported(
            f"interactive connect is not supported; use: cautem connect {name}"
        )


def _sandbox_from_summary(summary: console_pb2.SandboxSummary) -> Sandbox:
    return Sandbox(
        name=summary.name,
        status=summary.registry_status,
        id=summary.id,
        image=summary.image,
        workspace=summary.workspace,
        resource_version=summary.resource_version,
        labels=dict(summary.labels),
    )
