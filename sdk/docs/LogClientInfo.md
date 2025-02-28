# LogClientInfo

Represents a LogClientInfo resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_agent** | [**LogUserAgent**](LogUserAgent.md) |  | [optional] 
**zone** | **str** |  | [optional] 
**device** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**geographical_context** | [**LogGeographicalContext**](LogGeographicalContext.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.log_client_info import LogClientInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LogClientInfo from a JSON string
log_client_info_instance = LogClientInfo.from_json(json)
# print the JSON string representation of the object
print LogClientInfo.to_json()

# convert the object into a dict
log_client_info_dict = log_client_info_instance.to_dict()
# create an instance of LogClientInfo from a dict
log_client_info_form_dict = log_client_info.from_dict(log_client_info_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


