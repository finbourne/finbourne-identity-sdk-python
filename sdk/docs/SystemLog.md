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

# TODO update the JSON string below
json = "{}"
# create an instance of SystemLog from a JSON string
system_log_instance = SystemLog.from_json(json)
# print the JSON string representation of the object
print SystemLog.to_json()

# convert the object into a dict
system_log_dict = system_log_instance.to_dict()
# create an instance of SystemLog from a dict
system_log_form_dict = system_log.from_dict(system_log_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


