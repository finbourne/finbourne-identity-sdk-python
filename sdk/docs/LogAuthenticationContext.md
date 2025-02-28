# LogAuthenticationContext

Represents a LogAuthenticationContext resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_provider** | **str** |  | [optional] 
**credential_provider** | **List[str]** |  | [optional] 
**credential_type** | **List[str]** |  | [optional] 
**issuer** | [**LogIssuer**](LogIssuer.md) |  | [optional] 
**interface** | **str** |  | [optional] 
**authentication_step** | **int** |  | [optional] 
**external_session_id** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_authentication_context import LogAuthenticationContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogAuthenticationContext from a JSON string
log_authentication_context_instance = LogAuthenticationContext.from_json(json)
# print the JSON string representation of the object
print LogAuthenticationContext.to_json()

# convert the object into a dict
log_authentication_context_dict = log_authentication_context_instance.to_dict()
# create an instance of LogAuthenticationContext from a dict
log_authentication_context_form_dict = log_authentication_context.from_dict(log_authentication_context_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


