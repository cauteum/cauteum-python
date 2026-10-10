# Changelog

## Unreleased

## [0.1.6] - 2026-10-11

### Changed

- Rename the installable package and SDK imports to `cautem`.

### Changed

- Move overview, sandbox CRUD, and command execution from REST endpoints to native `cautem.control.v1` and pinned OpenShell gRPC clients. The beta Python API now requires sandbox images for create operations.
- Check in reproducible generated Python protobuf/gRPC clients and declare their runtime dependencies.
- Retain HTTP only for the unauthenticated health probe.

## [v0.1.0-beta.1] - 2026-10-08

### Changed

- Adopt Apache-2.0 licensing and include the project license and notices in package metadata.
- Mark the package as beta; PyPI publication remains pending.
