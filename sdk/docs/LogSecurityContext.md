# LogSecurityContext

Represents a LogSecurityContext resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **int** |  | [optional] 
**as_org** | **str** |  | [optional] 
**isp** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**is_proxy** | **bool** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_security_context import LogSecurityContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogSecurityContext from a JSON string
log_security_context_instance = LogSecurityContext.from_json(json)
# print the JSON string representation of the object
print LogSecurityContext.to_json()

# convert the object into a dict
log_security_context_dict = log_security_context_instance.to_dict()
# create an instance of LogSecurityContext from a dict
log_security_context_form_dict = log_security_context.from_dict(log_security_context_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


