from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SandboxWatchEventKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SANDBOX_WATCH_EVENT_KIND_UNSPECIFIED: _ClassVar[SandboxWatchEventKind]
    SANDBOX_WATCH_EVENT_KIND_RESET: _ClassVar[SandboxWatchEventKind]
    SANDBOX_WATCH_EVENT_KIND_UPSERT: _ClassVar[SandboxWatchEventKind]
    SANDBOX_WATCH_EVENT_KIND_DELETE: _ClassVar[SandboxWatchEventKind]
    SANDBOX_WATCH_EVENT_KIND_SYNCED: _ClassVar[SandboxWatchEventKind]
    SANDBOX_WATCH_EVENT_KIND_HEARTBEAT: _ClassVar[SandboxWatchEventKind]

class SandboxLogWatchKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SANDBOX_LOG_WATCH_KIND_UNSPECIFIED: _ClassVar[SandboxLogWatchKind]
    SANDBOX_LOG_WATCH_KIND_RESET: _ClassVar[SandboxLogWatchKind]
    SANDBOX_LOG_WATCH_KIND_LINE: _ClassVar[SandboxLogWatchKind]
    SANDBOX_LOG_WATCH_KIND_HEARTBEAT: _ClassVar[SandboxLogWatchKind]
SANDBOX_WATCH_EVENT_KIND_UNSPECIFIED: SandboxWatchEventKind
SANDBOX_WATCH_EVENT_KIND_RESET: SandboxWatchEventKind
SANDBOX_WATCH_EVENT_KIND_UPSERT: SandboxWatchEventKind
SANDBOX_WATCH_EVENT_KIND_DELETE: SandboxWatchEventKind
SANDBOX_WATCH_EVENT_KIND_SYNCED: SandboxWatchEventKind
SANDBOX_WATCH_EVENT_KIND_HEARTBEAT: SandboxWatchEventKind
SANDBOX_LOG_WATCH_KIND_UNSPECIFIED: SandboxLogWatchKind
SANDBOX_LOG_WATCH_KIND_RESET: SandboxLogWatchKind
SANDBOX_LOG_WATCH_KIND_LINE: SandboxLogWatchKind
SANDBOX_LOG_WATCH_KIND_HEARTBEAT: SandboxLogWatchKind

class GetGlobalPolicyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGlobalPolicyResponse(_message.Message):
    __slots__ = ("policy_yaml", "resource_version")
    POLICY_YAML_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    policy_yaml: str
    resource_version: int
    def __init__(self, policy_yaml: _Optional[str] = ..., resource_version: _Optional[int] = ...) -> None: ...

class UpdateGlobalPolicyRequest(_message.Message):
    __slots__ = ("policy_yaml", "expected_resource_version", "clear")
    POLICY_YAML_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLEAR_FIELD_NUMBER: _ClassVar[int]
    policy_yaml: str
    expected_resource_version: int
    clear: bool
    def __init__(self, policy_yaml: _Optional[str] = ..., expected_resource_version: _Optional[int] = ..., clear: bool = ...) -> None: ...

class UpdateGlobalPolicyResponse(_message.Message):
    __slots__ = ("resource_version",)
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    resource_version: int
    def __init__(self, resource_version: _Optional[int] = ...) -> None: ...

class GetSandboxPolicyRequest(_message.Message):
    __slots__ = ("workspace", "sandbox_name", "view")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    sandbox_name: str
    view: str
    def __init__(self, workspace: _Optional[str] = ..., sandbox_name: _Optional[str] = ..., view: _Optional[str] = ...) -> None: ...

class GetSandboxPolicyResponse(_message.Message):
    __slots__ = ("policy_yaml", "resource_version", "policy_revision")
    POLICY_YAML_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    POLICY_REVISION_FIELD_NUMBER: _ClassVar[int]
    policy_yaml: str
    resource_version: int
    policy_revision: int
    def __init__(self, policy_yaml: _Optional[str] = ..., resource_version: _Optional[int] = ..., policy_revision: _Optional[int] = ...) -> None: ...

class UpdateSandboxPolicyRequest(_message.Message):
    __slots__ = ("workspace", "sandbox_name", "base_policy_yaml", "expected_policy_revision")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    BASE_POLICY_YAML_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_POLICY_REVISION_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    sandbox_name: str
    base_policy_yaml: str
    expected_policy_revision: int
    def __init__(self, workspace: _Optional[str] = ..., sandbox_name: _Optional[str] = ..., base_policy_yaml: _Optional[str] = ..., expected_policy_revision: _Optional[int] = ...) -> None: ...

class UpdateSandboxPolicyResponse(_message.Message):
    __slots__ = ("effective_policy_yaml", "stripped_provider_rules", "policy_revision")
    EFFECTIVE_POLICY_YAML_FIELD_NUMBER: _ClassVar[int]
    STRIPPED_PROVIDER_RULES_FIELD_NUMBER: _ClassVar[int]
    POLICY_REVISION_FIELD_NUMBER: _ClassVar[int]
    effective_policy_yaml: str
    stripped_provider_rules: int
    policy_revision: int
    def __init__(self, effective_policy_yaml: _Optional[str] = ..., stripped_provider_rules: _Optional[int] = ..., policy_revision: _Optional[int] = ...) -> None: ...

class ListSandboxPolicyRevisionsRequest(_message.Message):
    __slots__ = ("workspace", "sandbox_name")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    sandbox_name: str
    def __init__(self, workspace: _Optional[str] = ..., sandbox_name: _Optional[str] = ...) -> None: ...

class ListSandboxPolicyRevisionsResponse(_message.Message):
    __slots__ = ("revisions",)
    REVISIONS_FIELD_NUMBER: _ClassVar[int]
    revisions: _containers.RepeatedCompositeFieldContainer[PolicyRevisionSummary]
    def __init__(self, revisions: _Optional[_Iterable[_Union[PolicyRevisionSummary, _Mapping]]] = ...) -> None: ...

class GetSandboxPolicyRevisionRequest(_message.Message):
    __slots__ = ("workspace", "sandbox_name", "revision")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    sandbox_name: str
    revision: int
    def __init__(self, workspace: _Optional[str] = ..., sandbox_name: _Optional[str] = ..., revision: _Optional[int] = ...) -> None: ...

class GetSandboxPolicyRevisionResponse(_message.Message):
    __slots__ = ("policy_yaml", "revision")
    POLICY_YAML_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    policy_yaml: str
    revision: PolicyRevisionSummary
    def __init__(self, policy_yaml: _Optional[str] = ..., revision: _Optional[_Union[PolicyRevisionSummary, _Mapping]] = ...) -> None: ...

class PolicyRevisionSummary(_message.Message):
    __slots__ = ("revision", "updated_at_unix_ms", "bytes", "status")
    REVISION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    revision: int
    updated_at_unix_ms: int
    bytes: int
    status: str
    def __init__(self, revision: _Optional[int] = ..., updated_at_unix_ms: _Optional[int] = ..., bytes: _Optional[int] = ..., status: _Optional[str] = ...) -> None: ...

class UpdateProviderCredentialsRequest(_message.Message):
    __slots__ = ("workspace", "provider_name", "credentials")
    class CredentialsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_NAME_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    provider_name: str
    credentials: _containers.ScalarMap[str, str]
    def __init__(self, workspace: _Optional[str] = ..., provider_name: _Optional[str] = ..., credentials: _Optional[_Mapping[str, str]] = ...) -> None: ...

class UpdateProviderCredentialsResponse(_message.Message):
    __slots__ = ("updated_keys",)
    UPDATED_KEYS_FIELD_NUMBER: _ClassVar[int]
    updated_keys: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, updated_keys: _Optional[_Iterable[str]] = ...) -> None: ...

class ListProviderProfilesRequest(_message.Message):
    __slots__ = ("workspace",)
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    def __init__(self, workspace: _Optional[str] = ...) -> None: ...

class ProviderProfileSummary(_message.Message):
    __slots__ = ("id", "category", "source", "scope", "resource_version")
    ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    id: str
    category: str
    source: str
    scope: str
    resource_version: int
    def __init__(self, id: _Optional[str] = ..., category: _Optional[str] = ..., source: _Optional[str] = ..., scope: _Optional[str] = ..., resource_version: _Optional[int] = ...) -> None: ...

class ListProviderProfilesResponse(_message.Message):
    __slots__ = ("profiles",)
    PROFILES_FIELD_NUMBER: _ClassVar[int]
    profiles: _containers.RepeatedCompositeFieldContainer[ProviderProfileSummary]
    def __init__(self, profiles: _Optional[_Iterable[_Union[ProviderProfileSummary, _Mapping]]] = ...) -> None: ...

class GetProviderProfileRequest(_message.Message):
    __slots__ = ("workspace", "id")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    id: str
    def __init__(self, workspace: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetProviderProfileResponse(_message.Message):
    __slots__ = ("profile_yaml", "source", "resource_version")
    PROFILE_YAML_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    profile_yaml: str
    source: str
    resource_version: int
    def __init__(self, profile_yaml: _Optional[str] = ..., source: _Optional[str] = ..., resource_version: _Optional[int] = ...) -> None: ...

class ImportProviderProfileRequest(_message.Message):
    __slots__ = ("workspace", "profile_yaml", "id")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PROFILE_YAML_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    profile_yaml: str
    id: str
    def __init__(self, workspace: _Optional[str] = ..., profile_yaml: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class ImportProviderProfileResponse(_message.Message):
    __slots__ = ("imported_id",)
    IMPORTED_ID_FIELD_NUMBER: _ClassVar[int]
    imported_id: str
    def __init__(self, imported_id: _Optional[str] = ...) -> None: ...

class UpdateProviderProfileRequest(_message.Message):
    __slots__ = ("workspace", "id", "expected_resource_version", "profile_yaml")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROFILE_YAML_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    id: str
    expected_resource_version: int
    profile_yaml: str
    def __init__(self, workspace: _Optional[str] = ..., id: _Optional[str] = ..., expected_resource_version: _Optional[int] = ..., profile_yaml: _Optional[str] = ...) -> None: ...

class UpdateProviderProfileResponse(_message.Message):
    __slots__ = ("resource_version",)
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    resource_version: int
    def __init__(self, resource_version: _Optional[int] = ...) -> None: ...

class DeleteProviderProfileRequest(_message.Message):
    __slots__ = ("workspace", "id")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    id: str
    def __init__(self, workspace: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class DeleteProviderProfileResponse(_message.Message):
    __slots__ = ("deleted",)
    DELETED_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    def __init__(self, deleted: bool = ...) -> None: ...

class GetViewerRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetViewerResponse(_message.Message):
    __slots__ = ("subject", "roles", "scopes", "identity_provider")
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    SCOPES_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    subject: str
    roles: _containers.RepeatedScalarFieldContainer[str]
    scopes: _containers.RepeatedScalarFieldContainer[str]
    identity_provider: str
    def __init__(self, subject: _Optional[str] = ..., roles: _Optional[_Iterable[str]] = ..., scopes: _Optional[_Iterable[str]] = ..., identity_provider: _Optional[str] = ...) -> None: ...

class GetConsoleCapabilitiesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetConsoleCapabilitiesResponse(_message.Message):
    __slots__ = ("sandbox_lifecycle_available", "sandbox_watch_available", "compute_drivers")
    SANDBOX_LIFECYCLE_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_WATCH_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_DRIVERS_FIELD_NUMBER: _ClassVar[int]
    sandbox_lifecycle_available: bool
    sandbox_watch_available: bool
    compute_drivers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, sandbox_lifecycle_available: bool = ..., sandbox_watch_available: bool = ..., compute_drivers: _Optional[_Iterable[str]] = ...) -> None: ...

class GetOverviewRequest(_message.Message):
    __slots__ = ("workspace",)
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    def __init__(self, workspace: _Optional[str] = ...) -> None: ...

class GetOverviewResponse(_message.Message):
    __slots__ = ("gateway_id", "workspace", "sandbox_count", "registry_running_count", "snapshot_at_unix_ms", "runtime_status_available")
    GATEWAY_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_COUNT_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_RUNNING_COUNT_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_STATUS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    gateway_id: str
    workspace: str
    sandbox_count: int
    registry_running_count: int
    snapshot_at_unix_ms: int
    runtime_status_available: bool
    def __init__(self, gateway_id: _Optional[str] = ..., workspace: _Optional[str] = ..., sandbox_count: _Optional[int] = ..., registry_running_count: _Optional[int] = ..., snapshot_at_unix_ms: _Optional[int] = ..., runtime_status_available: bool = ...) -> None: ...

class ListSandboxesRequest(_message.Message):
    __slots__ = ("workspace", "page_size", "page_token", "name_prefix", "registry_status", "compute_driver", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_DRIVER_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    page_size: int
    page_token: str
    name_prefix: str
    registry_status: str
    compute_driver: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, workspace: _Optional[str] = ..., page_size: _Optional[int] = ..., page_token: _Optional[str] = ..., name_prefix: _Optional[str] = ..., registry_status: _Optional[str] = ..., compute_driver: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListSandboxesResponse(_message.Message):
    __slots__ = ("sandboxes", "next_page_token")
    SANDBOXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    sandboxes: _containers.RepeatedCompositeFieldContainer[SandboxSummary]
    next_page_token: str
    def __init__(self, sandboxes: _Optional[_Iterable[_Union[SandboxSummary, _Mapping]]] = ..., next_page_token: _Optional[str] = ...) -> None: ...

class GetSandboxRequest(_message.Message):
    __slots__ = ("workspace", "name")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    name: str
    def __init__(self, workspace: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class GetSandboxResponse(_message.Message):
    __slots__ = ("sandbox",)
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    sandbox: SandboxSummary
    def __init__(self, sandbox: _Optional[_Union[SandboxSummary, _Mapping]] = ...) -> None: ...

class WatchSandboxesRequest(_message.Message):
    __slots__ = ("workspace",)
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    def __init__(self, workspace: _Optional[str] = ...) -> None: ...

class WatchSandboxesResponse(_message.Message):
    __slots__ = ("kind", "stream_sequence", "sandbox", "deleted_name", "observed_at_unix_ms")
    KIND_FIELD_NUMBER: _ClassVar[int]
    STREAM_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    DELETED_NAME_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    kind: SandboxWatchEventKind
    stream_sequence: int
    sandbox: SandboxSummary
    deleted_name: str
    observed_at_unix_ms: int
    def __init__(self, kind: _Optional[_Union[SandboxWatchEventKind, str]] = ..., stream_sequence: _Optional[int] = ..., sandbox: _Optional[_Union[SandboxSummary, _Mapping]] = ..., deleted_name: _Optional[str] = ..., observed_at_unix_ms: _Optional[int] = ...) -> None: ...

class GetSandboxLogsRequest(_message.Message):
    __slots__ = ("workspace", "name", "limit", "since_unix_ms", "source", "level")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    SINCE_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    name: str
    limit: int
    since_unix_ms: int
    source: str
    level: str
    def __init__(self, workspace: _Optional[str] = ..., name: _Optional[str] = ..., limit: _Optional[int] = ..., since_unix_ms: _Optional[int] = ..., source: _Optional[str] = ..., level: _Optional[str] = ...) -> None: ...

class GetSandboxLogsResponse(_message.Message):
    __slots__ = ("lines", "cursor")
    LINES_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    lines: _containers.RepeatedCompositeFieldContainer[SandboxLogLine]
    cursor: int
    def __init__(self, lines: _Optional[_Iterable[_Union[SandboxLogLine, _Mapping]]] = ..., cursor: _Optional[int] = ...) -> None: ...

class WatchSandboxLogsRequest(_message.Message):
    __slots__ = ("workspace", "name", "initial_limit", "after_cursor", "since_unix_ms", "source", "level")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INITIAL_LIMIT_FIELD_NUMBER: _ClassVar[int]
    AFTER_CURSOR_FIELD_NUMBER: _ClassVar[int]
    SINCE_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    name: str
    initial_limit: int
    after_cursor: int
    since_unix_ms: int
    source: str
    level: str
    def __init__(self, workspace: _Optional[str] = ..., name: _Optional[str] = ..., initial_limit: _Optional[int] = ..., after_cursor: _Optional[int] = ..., since_unix_ms: _Optional[int] = ..., source: _Optional[str] = ..., level: _Optional[str] = ...) -> None: ...

class WatchSandboxLogsResponse(_message.Message):
    __slots__ = ("kind", "line", "cursor", "observed_at_unix_ms")
    KIND_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    OBSERVED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    kind: SandboxLogWatchKind
    line: SandboxLogLine
    cursor: int
    observed_at_unix_ms: int
    def __init__(self, kind: _Optional[_Union[SandboxLogWatchKind, str]] = ..., line: _Optional[_Union[SandboxLogLine, _Mapping]] = ..., cursor: _Optional[int] = ..., observed_at_unix_ms: _Optional[int] = ...) -> None: ...

class SandboxLogLine(_message.Message):
    __slots__ = ("cursor", "timestamp_unix_ms", "source", "level", "target", "message")
    CURSOR_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    cursor: int
    timestamp_unix_ms: int
    source: str
    level: str
    target: str
    message: str
    def __init__(self, cursor: _Optional[int] = ..., timestamp_unix_ms: _Optional[int] = ..., source: _Optional[str] = ..., level: _Optional[str] = ..., target: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class CreateSandboxRequest(_message.Message):
    __slots__ = ("workspace", "name", "image", "workload_template_name", "command", "request_id", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    WORKLOAD_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMAND_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    name: str
    image: str
    workload_template_name: str
    command: _containers.RepeatedScalarFieldContainer[str]
    request_id: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, workspace: _Optional[str] = ..., name: _Optional[str] = ..., image: _Optional[str] = ..., workload_template_name: _Optional[str] = ..., command: _Optional[_Iterable[str]] = ..., request_id: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateSandboxResponse(_message.Message):
    __slots__ = ("sandbox", "completed", "operation_id")
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    sandbox: SandboxSummary
    completed: bool
    operation_id: str
    def __init__(self, sandbox: _Optional[_Union[SandboxSummary, _Mapping]] = ..., completed: bool = ..., operation_id: _Optional[str] = ...) -> None: ...

class StartSandboxRequest(_message.Message):
    __slots__ = ("workspace", "name", "expected_resource_version", "request_id")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    name: str
    expected_resource_version: int
    request_id: str
    def __init__(self, workspace: _Optional[str] = ..., name: _Optional[str] = ..., expected_resource_version: _Optional[int] = ..., request_id: _Optional[str] = ...) -> None: ...

class StartSandboxResponse(_message.Message):
    __slots__ = ("sandbox", "completed", "operation_id")
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    sandbox: SandboxSummary
    completed: bool
    operation_id: str
    def __init__(self, sandbox: _Optional[_Union[SandboxSummary, _Mapping]] = ..., completed: bool = ..., operation_id: _Optional[str] = ...) -> None: ...

class StopSandboxRequest(_message.Message):
    __slots__ = ("workspace", "name", "expected_resource_version", "request_id")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    name: str
    expected_resource_version: int
    request_id: str
    def __init__(self, workspace: _Optional[str] = ..., name: _Optional[str] = ..., expected_resource_version: _Optional[int] = ..., request_id: _Optional[str] = ...) -> None: ...

class StopSandboxResponse(_message.Message):
    __slots__ = ("sandbox", "completed", "operation_id")
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    sandbox: SandboxSummary
    completed: bool
    operation_id: str
    def __init__(self, sandbox: _Optional[_Union[SandboxSummary, _Mapping]] = ..., completed: bool = ..., operation_id: _Optional[str] = ...) -> None: ...

class DeleteSandboxRequest(_message.Message):
    __slots__ = ("workspace", "name", "expected_resource_version", "request_id")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    name: str
    expected_resource_version: int
    request_id: str
    def __init__(self, workspace: _Optional[str] = ..., name: _Optional[str] = ..., expected_resource_version: _Optional[int] = ..., request_id: _Optional[str] = ...) -> None: ...

class DeleteSandboxResponse(_message.Message):
    __slots__ = ("deleted", "operation_id")
    DELETED_FIELD_NUMBER: _ClassVar[int]
    OPERATION_ID_FIELD_NUMBER: _ClassVar[int]
    deleted: bool
    operation_id: str
    def __init__(self, deleted: bool = ..., operation_id: _Optional[str] = ...) -> None: ...

class GetOperationRequest(_message.Message):
    __slots__ = ("workspace", "request_id")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    request_id: str
    def __init__(self, workspace: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class GetOperationResponse(_message.Message):
    __slots__ = ("operation",)
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation: OperationSummary
    def __init__(self, operation: _Optional[_Union[OperationSummary, _Mapping]] = ...) -> None: ...

class ListOperationsRequest(_message.Message):
    __slots__ = ("workspace", "after_number", "limit")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    AFTER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    after_number: int
    limit: int
    def __init__(self, workspace: _Optional[str] = ..., after_number: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class ListOperationsResponse(_message.Message):
    __slots__ = ("operations", "next_after_number")
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_AFTER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    operations: _containers.RepeatedCompositeFieldContainer[OperationSummary]
    next_after_number: int
    def __init__(self, operations: _Optional[_Iterable[_Union[OperationSummary, _Mapping]]] = ..., next_after_number: _Optional[int] = ...) -> None: ...

class ListAuditEventsRequest(_message.Message):
    __slots__ = ("workspace", "after_id", "limit")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    AFTER_ID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    after_id: int
    limit: int
    def __init__(self, workspace: _Optional[str] = ..., after_id: _Optional[int] = ..., limit: _Optional[int] = ...) -> None: ...

class ListAuditEventsResponse(_message.Message):
    __slots__ = ("events", "next_after_id")
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_AFTER_ID_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[AuditEventSummary]
    next_after_id: int
    def __init__(self, events: _Optional[_Iterable[_Union[AuditEventSummary, _Mapping]]] = ..., next_after_id: _Optional[int] = ...) -> None: ...

class OperationSummary(_message.Message):
    __slots__ = ("id", "number", "request_id", "actor", "workspace", "sandbox", "action", "state", "error_code", "result_registry_status", "result_resource_version", "created_at_unix_ms", "updated_at_unix_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    RESULT_REGISTRY_STATUS_FIELD_NUMBER: _ClassVar[int]
    RESULT_RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    number: int
    request_id: str
    actor: str
    workspace: str
    sandbox: str
    action: str
    state: str
    error_code: str
    result_registry_status: str
    result_resource_version: int
    created_at_unix_ms: int
    updated_at_unix_ms: int
    def __init__(self, id: _Optional[str] = ..., number: _Optional[int] = ..., request_id: _Optional[str] = ..., actor: _Optional[str] = ..., workspace: _Optional[str] = ..., sandbox: _Optional[str] = ..., action: _Optional[str] = ..., state: _Optional[str] = ..., error_code: _Optional[str] = ..., result_registry_status: _Optional[str] = ..., result_resource_version: _Optional[int] = ..., created_at_unix_ms: _Optional[int] = ..., updated_at_unix_ms: _Optional[int] = ...) -> None: ...

class AuditEventSummary(_message.Message):
    __slots__ = ("id", "timestamp_unix_ms", "actor", "action", "workspace", "sandbox", "outcome", "code")
    ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_FIELD_NUMBER: _ClassVar[int]
    OUTCOME_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    id: int
    timestamp_unix_ms: int
    actor: str
    action: str
    workspace: str
    sandbox: str
    outcome: str
    code: str
    def __init__(self, id: _Optional[int] = ..., timestamp_unix_ms: _Optional[int] = ..., actor: _Optional[str] = ..., action: _Optional[str] = ..., workspace: _Optional[str] = ..., sandbox: _Optional[str] = ..., outcome: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class SandboxSummary(_message.Message):
    __slots__ = ("name", "workspace", "registry_status", "compute_driver", "resource_version", "updated_at_unix_ms", "runtime_status_available", "id", "image", "labels")
    class LabelsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    REGISTRY_STATUS_FIELD_NUMBER: _ClassVar[int]
    COMPUTE_DRIVER_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    RUNTIME_STATUS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    workspace: str
    registry_status: str
    compute_driver: str
    resource_version: int
    updated_at_unix_ms: int
    runtime_status_available: bool
    id: str
    image: str
    labels: _containers.ScalarMap[str, str]
    def __init__(self, name: _Optional[str] = ..., workspace: _Optional[str] = ..., registry_status: _Optional[str] = ..., compute_driver: _Optional[str] = ..., resource_version: _Optional[int] = ..., updated_at_unix_ms: _Optional[int] = ..., runtime_status_available: bool = ..., id: _Optional[str] = ..., image: _Optional[str] = ..., labels: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListServicesRequest(_message.Message):
    __slots__ = ("workspace",)
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    def __init__(self, workspace: _Optional[str] = ...) -> None: ...

class ListServicesResponse(_message.Message):
    __slots__ = ("services",)
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[ServiceSummary]
    def __init__(self, services: _Optional[_Iterable[_Union[ServiceSummary, _Mapping]]] = ...) -> None: ...

class ServiceSummary(_message.Message):
    __slots__ = ("name", "sandbox_name", "port", "updated_at_unix_ms")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    name: str
    sandbox_name: str
    port: int
    updated_at_unix_ms: int
    def __init__(self, name: _Optional[str] = ..., sandbox_name: _Optional[str] = ..., port: _Optional[int] = ..., updated_at_unix_ms: _Optional[int] = ...) -> None: ...

class ListTemplatesRequest(_message.Message):
    __slots__ = ("workspace",)
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    def __init__(self, workspace: _Optional[str] = ...) -> None: ...

class ListTemplatesResponse(_message.Message):
    __slots__ = ("templates",)
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[TemplateSummary]
    def __init__(self, templates: _Optional[_Iterable[_Union[TemplateSummary, _Mapping]]] = ...) -> None: ...

class TemplateSummary(_message.Message):
    __slots__ = ("name", "workspace", "image", "providers", "resource_version", "created_at_unix_ms")
    NAME_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    name: str
    workspace: str
    image: str
    providers: _containers.RepeatedScalarFieldContainer[str]
    resource_version: int
    created_at_unix_ms: int
    def __init__(self, name: _Optional[str] = ..., workspace: _Optional[str] = ..., image: _Optional[str] = ..., providers: _Optional[_Iterable[str]] = ..., resource_version: _Optional[int] = ..., created_at_unix_ms: _Optional[int] = ...) -> None: ...

class ListWorkspacesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ListWorkspacesResponse(_message.Message):
    __slots__ = ("workspaces",)
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[WorkspaceSummary]
    def __init__(self, workspaces: _Optional[_Iterable[_Union[WorkspaceSummary, _Mapping]]] = ...) -> None: ...

class GetWorkspaceRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetWorkspaceResponse(_message.Message):
    __slots__ = ("workspace",)
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: WorkspaceSummary
    def __init__(self, workspace: _Optional[_Union[WorkspaceSummary, _Mapping]] = ...) -> None: ...

class WorkspaceSummary(_message.Message):
    __slots__ = ("name", "caller_role", "member_count", "resource_version", "updated_at_unix_ms")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CALLER_ROLE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    name: str
    caller_role: str
    member_count: int
    resource_version: int
    updated_at_unix_ms: int
    def __init__(self, name: _Optional[str] = ..., caller_role: _Optional[str] = ..., member_count: _Optional[int] = ..., resource_version: _Optional[int] = ..., updated_at_unix_ms: _Optional[int] = ...) -> None: ...

class ListPolicyProposalsRequest(_message.Message):
    __slots__ = ("workspace", "sandbox_name", "status", "page_size", "after_id")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    AFTER_ID_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    sandbox_name: str
    status: str
    page_size: int
    after_id: str
    def __init__(self, workspace: _Optional[str] = ..., sandbox_name: _Optional[str] = ..., status: _Optional[str] = ..., page_size: _Optional[int] = ..., after_id: _Optional[str] = ...) -> None: ...

class ListPolicyProposalsResponse(_message.Message):
    __slots__ = ("proposals", "next_after_id")
    PROPOSALS_FIELD_NUMBER: _ClassVar[int]
    NEXT_AFTER_ID_FIELD_NUMBER: _ClassVar[int]
    proposals: _containers.RepeatedCompositeFieldContainer[PolicyProposalSummary]
    next_after_id: str
    def __init__(self, proposals: _Optional[_Iterable[_Union[PolicyProposalSummary, _Mapping]]] = ..., next_after_id: _Optional[str] = ...) -> None: ...

class GetPolicyProposalRequest(_message.Message):
    __slots__ = ("workspace", "id")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    id: str
    def __init__(self, workspace: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class GetPolicyProposalResponse(_message.Message):
    __slots__ = ("proposal",)
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    proposal: PolicyProposalSummary
    def __init__(self, proposal: _Optional[_Union[PolicyProposalSummary, _Mapping]] = ...) -> None: ...

class ApprovePolicyProposalResponse(_message.Message):
    __slots__ = ("proposal",)
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    proposal: PolicyProposalSummary
    def __init__(self, proposal: _Optional[_Union[PolicyProposalSummary, _Mapping]] = ...) -> None: ...

class RejectPolicyProposalResponse(_message.Message):
    __slots__ = ("proposal",)
    PROPOSAL_FIELD_NUMBER: _ClassVar[int]
    proposal: PolicyProposalSummary
    def __init__(self, proposal: _Optional[_Union[PolicyProposalSummary, _Mapping]] = ...) -> None: ...

class ApprovePolicyProposalRequest(_message.Message):
    __slots__ = ("workspace", "id")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    id: str
    def __init__(self, workspace: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...

class RejectPolicyProposalRequest(_message.Message):
    __slots__ = ("workspace", "id", "reason")
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    id: str
    reason: str
    def __init__(self, workspace: _Optional[str] = ..., id: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class PolicyProposalSummary(_message.Message):
    __slots__ = ("id", "sandbox_name", "status", "intent_summary", "rule_name", "rule_yaml", "rationale", "security_notes", "confidence", "hosts", "rejection_reason", "validation_result", "security_flagged", "created_at_unix_ms", "decided_at_unix_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    SANDBOX_NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    INTENT_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    RULE_NAME_FIELD_NUMBER: _ClassVar[int]
    RULE_YAML_FIELD_NUMBER: _ClassVar[int]
    RATIONALE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_NOTES_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    HOSTS_FIELD_NUMBER: _ClassVar[int]
    REJECTION_REASON_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FLAGGED_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    DECIDED_AT_UNIX_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    sandbox_name: str
    status: str
    intent_summary: str
    rule_name: str
    rule_yaml: str
    rationale: str
    security_notes: str
    confidence: float
    hosts: _containers.RepeatedScalarFieldContainer[str]
    rejection_reason: str
    validation_result: str
    security_flagged: bool
    created_at_unix_ms: int
    decided_at_unix_ms: int
    def __init__(self, id: _Optional[str] = ..., sandbox_name: _Optional[str] = ..., status: _Optional[str] = ..., intent_summary: _Optional[str] = ..., rule_name: _Optional[str] = ..., rule_yaml: _Optional[str] = ..., rationale: _Optional[str] = ..., security_notes: _Optional[str] = ..., confidence: _Optional[float] = ..., hosts: _Optional[_Iterable[str]] = ..., rejection_reason: _Optional[str] = ..., validation_result: _Optional[str] = ..., security_flagged: bool = ..., created_at_unix_ms: _Optional[int] = ..., decided_at_unix_ms: _Optional[int] = ...) -> None: ...
