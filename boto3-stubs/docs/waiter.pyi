from typing import Any
from boto3.docs.base import NestedDocumenter
from botocore.hooks import BaseEventHooks
from botocore.model import ServiceModel
from botocore.waiter import WaiterModel

class WaiterResourceDocumenter(NestedDocumenter):
    def __init__(
        self,
        resource: Any,
        service_waiter_model: WaiterModel,
        root_docs_path: str,
    ) -> None: ...
    def document_resource_waiters(self, section: Any) -> None: ...

def document_resource_waiter(
    section: Any,
    resource_name: str,
    event_emitter: BaseEventHooks,
    service_model: ServiceModel,
    resource_waiter_model: Any,
    service_waiter_model: WaiterModel,
    include_signature: bool = ...,
) -> None: ...
