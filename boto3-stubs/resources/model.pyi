import logging
import sys
from typing import Any, Dict, List, Optional, Tuple, Union

from botocore.model import Shape

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

logger: logging.Logger

_ActionDefinition = TypedDict(
    "_ActionDefinition",
    {"request": Dict[str, Any], "resource": Dict[str, Any], "path": str},
    total=False,
)
_DefinitionWithParamsDefinition = TypedDict(
    "_DefinitionWithParamsDefinition", {"params": List[Dict[str, Any]]}, total=False
)
_RequestDefinition = TypedDict("_RequestDefinition", {"operation": str}, total=False)
_WaiterDefinition = TypedDict("_WaiterDefinition", {"waiterName": str}, total=False)
_ResponseResourceDefinition = TypedDict(
    "_ResponseResourceDefinition", {"type": str, "path": str}, total=False
)
_ResourceModelDefinition = TypedDict("_ResourceModelDefinition", {"shape": str}, total=False)

class Identifier:
    def __init__(self, name: str, member_name: Optional[str] = ...) -> None:
        self.name: str
        self.member_name: str

class Action:
    def __init__(
        self, name: str, definition: _ActionDefinition, resource_defs: Dict[str, Dict[str, Any]]
    ) -> None:
        self.name: str
        self.request: Optional[Request]
        self.resource: Optional[ResponseResource]
        self.path: Optional[str]

class DefinitionWithParams:
    def __init__(self, definition: _DefinitionWithParamsDefinition) -> None: ...
    @property
    def params(self) -> List[Parameter]: ...

class Parameter:
    def __init__(
        self,
        target: str,
        source: str,
        name: Optional[str] = ...,
        path: Optional[str] = ...,
        value: Union[str, int, float, bool, None] = ...,
        **kwargs: Any,
    ) -> None:
        self.target: str
        self.source: str
        self.name: Optional[str]
        self.path: Optional[str]
        self.value: Union[str, int, float, bool, None]

class Request(DefinitionWithParams):
    def __init__(self, definition: _RequestDefinition) -> None:
        self.operation: str

class Waiter(DefinitionWithParams):
    PREFIX: Literal["WaitUntil"]
    def __init__(self, name: str, definition: _WaiterDefinition) -> None:
        self.name: str
        self.waiter_name: str

class ResponseResource:
    def __init__(
        self, definition: _ResponseResourceDefinition, resource_defs: Dict[str, Dict[str, Any]]
    ) -> None:
        self.type: str
        self.path: str

    @property
    def identifiers(self) -> List[Identifier]: ...
    @property
    def model(self) -> "ResourceModel": ...

class Collection(Action):
    @property
    def batch_actions(self) -> List[Action]: ...

class ResourceModel:
    def __init__(
        self,
        name: str,
        definition: _ResourceModelDefinition,
        resource_defs: Dict[str, Dict[str, Any]],
    ) -> None:
        self.name: str
        self.shape: Optional[str]

    def load_rename_map(self, shape: Optional[Shape] = ...) -> None: ...
    def get_attributes(self, shape: Shape) -> Dict[str, Tuple[str, Any]]: ...
    @property
    def identifiers(self) -> List[Identifier]: ...
    @property
    def load(self) -> Optional[Action]: ...
    @property
    def actions(self) -> List[Action]: ...
    @property
    def batch_actions(self) -> List[Action]: ...
    @property
    def subresources(self) -> List[ResponseResource]: ...
    @property
    def references(self) -> List[Action]: ...
    @property
    def collections(self) -> List[Collection]: ...
    @property
    def waiters(self) -> List[Waiter]: ...
