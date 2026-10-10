<h1 align="center">cauteum (Python)</h1>

<p align="center">
  <strong>Python SDK for cauteum-gateway</strong><br>
  Manage sandboxes over gRPC and execute through OpenShell RPC.
</p>

<p align="center">
  <a href="https://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/badge/License-Apache--2.0-blue.svg" alt="License"></a>
</p>

<p align="center">
  <sub>Part of the <a href="https://github.com/cautem">cauteum</a> ecosystem</sub>
</p>

---

## Overview

The [gateway guide](https://cautem.github.io/cauteum-haven.github.io/guides/gateway/) describes the server this client calls. For OpenShell parity, see [compatibility status](https://cautem.github.io/cauteum-haven.github.io/reference/openshell-compatibility/).

The SDK uses native gRPC for `cauteum.control.v1` and the pinned OpenShell
`ExecSandbox` method. HTTP remains for the transport health probe. Interactive
TTY stays on the CLI (`cauteum connect`).

---

## Installation

```bash
pip install -e .
```

Run the command in this checkout. The `cauteum` package is not published on PyPI yet.

---

## Quick Start

```python
from cauteum import Client, Sandbox

with Client("http://127.0.0.1:7443") as c:
    c.create(Sandbox(name="demo", image="python:3.12-slim"))
    print(c.list())
    print(c.exec("demo", "echo", "hi"))
```

Set `CAUTEUM_GATEWAY_TOKEN` or pass `token="…"` to `Client` when the
gateway requires bearer authentication. RPC failures are raised as `grpc.RpcError`;
the health probe uses `httpx` exceptions.

Generated protocol clients are checked in. From this module in the
multi-repository workspace, regenerate them with `python scripts/generate_proto.py`
after updating the gateway control Proto or pinned OpenShell source.

---

## Related

| Resource | Link |
|----------|------|
| Organization | [https://github.com/cautem](https://github.com/cautem) |
| Go SDK | [cautem/cauteum-sdk](https://github.com/cautem/cauteum-sdk) |
| Gateway | [cautem/cauteum-gateway](https://github.com/cautem/cauteum-gateway) |

## License

Apache-2.0 © cauteum
