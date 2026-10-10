#!/usr/bin/env python3
"""Generate cautem and pinned OpenShell Python gRPC clients."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


MODULE_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = MODULE_ROOT.parent
GATEWAY_PROTO = WORKSPACE_ROOT / "cautem-gateway" / "api" / "proto"
UPSTREAM_PROTO = WORKSPACE_ROOT / "tools" / "upstream" / "openshell" / "proto"
OPEN_SHELL_OUT = MODULE_ROOT / "cautem" / "_proto" / "openshell"


def generate(proto_root: Path, output: Path, files: list[str]) -> None:
    subprocess.run(
        [
            sys.executable,
            "-m",
            "grpc_tools.protoc",
            f"-I{proto_root}",
            f"--python_out={output}",
            f"--pyi_out={output}",
            f"--grpc_python_out={output}",
            *files,
        ],
        cwd=WORKSPACE_ROOT,
        check=True,
    )


def main() -> None:
    generate(
        GATEWAY_PROTO,
        MODULE_ROOT,
        ["cautem/control/v1/console.proto"],
    )
    generate(
        UPSTREAM_PROTO,
        OPEN_SHELL_OUT,
        ["openshell.proto", "datamodel.proto", "options.proto", "sandbox.proto"],
    )

    # protoc emits flat imports for the upstream's flat proto layout. Make them
    # package-relative so the generated files work from an installed wheel.
    replacements = {
        "openshell_pb2": "openshell_pb2",
        "datamodel_pb2": "datamodel_pb2",
        "options_pb2": "options_pb2",
        "sandbox_pb2": "sandbox_pb2",
    }
    for path in OPEN_SHELL_OUT.glob("*_pb2*.py"):
        contents = path.read_text()
        for module in replacements:
            contents = re.sub(
                rf"^import {module} as ",
                f"from . import {module} as ",
                contents,
                flags=re.MULTILINE,
            )
        path.write_text(contents)

    for directory in (
        MODULE_ROOT / "cautem" / "control",
        MODULE_ROOT / "cautem" / "control" / "v1",
        MODULE_ROOT / "cautem" / "_proto",
        OPEN_SHELL_OUT,
    ):
        directory.mkdir(parents=True, exist_ok=True)
        (directory / "__init__.py").touch()


if __name__ == "__main__":
    main()
