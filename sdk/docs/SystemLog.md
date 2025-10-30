# SystemLog

A system log event
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actor** | [**LogActor**](LogActor.md) |  | [optional] 
**authentication_context** | [**LogAuthenticationContext**](LogAuthenticationContext.md) |  | [optional] 
**client_info** | [**LogClientInfo**](LogClientInfo.md) |  | [optional] 
**debug_context** | [**LogDebugContext**](LogDebugContext.md) |  | [optional] 
**display_message** | **str** | Represents a DisplayMessage resource in the Okta API | [optional] 
**event_type** | **str** | Represents a EventType resource in the Okta API | [optional] 
**legacy_event_type** | **str** | Represents a LegacyEventType resource in the Okta API | [optional] 
**outcome** | [**LogOutcome**](LogOutcome.md) |  | [optional] 
**published** | **datetime** | Represents when Published in the Okta API | [optional] 
**request** | [**LogRequest**](LogRequest.md) |  | [optional] 
**security_context** | [**LogSecurityContext**](LogSecurityContext.md) |  | [optional] 
**severity** | [**LogSeverity**](LogSeverity.md) |  | [optional] 
**target** | [**List[LogTarget]**](LogTarget.md) | Represents a LogTarget resource in the Okta API | [optional] 
**transaction** | [**LogTransaction**](LogTransaction.md) |  | [optional] 
**uuid** | **str** | Represents Uuid in the Okta API | [optional] 
**version** | **str** | Represents a Version in the Okta API | [optional] 
## Example

```python
from finbourne_identity.models.system_log import SystemLog
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

actor: Optional[LogActor] = None
authentication_context: Optional[LogAuthenticationContext] = # Replace with your value
client_info: Optional[LogClientInfo] = # Replace with your value
debug_context: Optional[LogDebugContext] = # Replace with your value
display_message: Optional[StrictStr] = "example_display_message"
event_type: Optional[StrictStr] = "example_event_type"
legacy_event_type: Optional[StrictStr] = "example_legacy_event_type"
outcome: Optional[LogOutcome] = None
published: Optional[datetime] = # Replace with your value
request: Optional[LogRequest] = None
security_context: Optional[LogSecurityContext] = # Replace with your value
severity: Optional[LogSeverity] = None
target: Optional[List[LogTarget]] = # Replace with your value
transaction: Optional[LogTransaction] = None
uuid: Optional[StrictStr] = "example_uuid"
version: Optional[StrictStr] = "example_version"
system_log_instance = SystemLog(actor=actor, authentication_context=authentication_context, client_info=client_info, debug_context=debug_context, display_message=display_message, event_type=event_type, legacy_event_type=legacy_event_type, outcome=outcome, published=published, request=request, security_context=security_context, severity=severity, target=target, transaction=transaction, uuid=uuid, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

