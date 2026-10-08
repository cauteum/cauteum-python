<h1 align="center">whaleshell (Python)</h1>

<p align="center">
  <strong>Python SDK for whaleshell-gateway</strong><br>
  Create, list, and relay-exec sandboxes over HTTP.
</p>

<p align="center">
  <a href="https://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/badge/License-Apache--2.0-blue.svg" alt="License"></a>
</p>

<p align="center">
  <sub>Part of the <a href="https://github.com/whaleshell">whaleshell</a> ecosystem</sub>
</p>

---

## Overview

The [gateway guide](https://whaleshell.github.io/guides/gateway/) describes the server this client calls. For OpenShell parity, see [compatibility status](https://whaleshell.github.io/reference/openshell-compatibility/).

HTTP client for **whaleshell-gateway** (registry + relay exec). Interactive TTY stays on the CLI (`whaleshell connect`).

---

## Installation

```bash
pip install -e .
```

Run the command in this checkout. The `whaleshell` package is not published on PyPI yet.

---

## Quick Start

```python
from whaleshell import Client, Sandbox

with Client("http://127.0.0.1:7443") as c:
    c.create(Sandbox(name="demo", status="running"))
    print(c.list())
    print(c.exec("demo", "echo", "hi"))
```

---

## Related

| Resource | Link |
|----------|------|
| Organization | [https://github.com/whaleshell](https://github.com/whaleshell) |
| Go SDK | [whaleshell/whaleshell-sdk](https://github.com/whaleshell/whaleshell-sdk) |
| Gateway | [whaleshell/whaleshell-gateway](https://github.com/whaleshell/whaleshell-gateway) |

## License

Apache-2.0 © whaleshell
