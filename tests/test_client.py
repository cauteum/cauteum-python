"""Tests for the native gRPC client and HTTP health probe."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from threading import Thread

import grpc
import httpx
import pytest

from cautem import Client, ConnectUnsupported, Sandbox
from cautem.control.v1 import console_pb2, console_pb2_grpc
from cautem._proto.openshell import openshell_pb2, openshell_pb2_grpc


class _Control(console_pb2_grpc.SandboxServiceServicer):
    def __init__(self):
        self.auth = []
        self.get_names = []

    def _record(self, context):
        metadata = dict(context.invocation_metadata())
        self.auth.append(metadata.get("authorization"))

    def CreateSandbox(self, request, context):  # noqa: N802
        self._record(context)
        return console_pb2.CreateSandboxResponse(
            sandbox=console_pb2.SandboxSummary(
                name=request.name,
                workspace=request.workspace,
                image=request.image,
                registry_status="running",
                resource_version=1,
                id="id-" + request.name,
                labels=request.labels,
            ),
            completed=True,
        )

    def ListSandboxes(self, request, context):  # noqa: N802
        self._record(context)
        return console_pb2.ListSandboxesResponse(
            sandboxes=[
                console_pb2.SandboxSummary(
                    name="demo",
                    workspace=request.workspace,
                    image="python:3.12-slim",
                    registry_status="running",
                    resource_version=1,
                    id="id-demo",
                )
            ]
        )

    def GetSandbox(self, request, context):  # noqa: N802
        self._record(context)
        self.get_names.append(request.name)
        return console_pb2.GetSandboxResponse(
            sandbox=console_pb2.SandboxSummary(
                name=request.name,
                workspace=request.workspace,
                image="python:3.12-slim",
                registry_status="running",
                resource_version=1,
                id="id-" + request.name,
            )
        )

    def DeleteSandbox(self, request, context):  # noqa: N802
        self._record(context)
        return console_pb2.DeleteSandboxResponse(deleted=True)


class _OpenShell(openshell_pb2_grpc.OpenShellServicer):
    def GetSandbox(self, request, context):  # noqa: N802
        return openshell_pb2.SandboxResponse(
            sandbox=openshell_pb2.Sandbox(
                metadata={"id": "id-" + request.name, "name": request.name}
            )
        )

    def ExecSandbox(self, request, context):  # noqa: N802
        yield openshell_pb2.ExecSandboxEvent(
            stdout=openshell_pb2.ExecSandboxStdout(data=b"hi\n")
        )
        yield openshell_pb2.ExecSandboxEvent(
            exit=openshell_pb2.ExecSandboxExit(exit_code=0)
        )


@pytest.fixture()
def gateway():
    control = _Control()
    server = grpc.server(ThreadPoolExecutor(max_workers=4))
    console_pb2_grpc.add_SandboxServiceServicer_to_server(control, server)
    openshell_pb2_grpc.add_OpenShellServicer_to_server(_OpenShell(), server)
    port = server.add_insecure_port("127.0.0.1:0")
    server.start()
    yield "http://127.0.0.1:%s" % port, control
    server.stop(0).wait()


def test_crud_and_exec(gateway):
    gateway_url, control = gateway
    with Client(gateway_url, token=" sdk-test-token ") as client:
        client.create(Sandbox(name="demo", image="python:3.12-slim"))
        assert len(client.list()) == 1
        assert client.get("demo").name == "demo"
        result = client.exec("demo", "echo", "hi")
        assert result.exit_code == 0 and result.output == "hi\n"
        with pytest.raises(ConnectUnsupported):
            client.connect("demo")
        client.delete("demo")
    assert control.auth
    assert all(value == "Bearer sdk-test-token" for value in control.auth)


def test_token_defaults_to_gateway_environment(gateway, monkeypatch):
    gateway_url, control = gateway
    monkeypatch.setenv("CAUTEM_GATEWAY_TOKEN", "env-token")
    with Client(gateway_url) as client:
        assert client.list()[0].name == "demo"
    assert control.auth == ["Bearer env-token"]


def test_sandbox_name_is_sent_as_rpc_data(gateway):
    gateway_url, control = gateway
    with Client(gateway_url) as client:
        assert client.get("demo?admin=true").name == "demo?admin=true"
    assert control.get_names == ["demo?admin=true"]


def test_health_probe_stays_http():
    seen = []

    def respond(request):
        seen.append(request.url.path)
        return httpx.Response(200, json={"ok": True}, request=request)

    client = Client("http://127.0.0.1:1")
    client._http.close()
    client._http = httpx.Client(
        base_url="http://127.0.0.1:1", transport=httpx.MockTransport(respond)
    )
    try:
        assert client.healthz() == {"ok": True}
    finally:
        client.close()
    assert seen == ["/healthz"]
