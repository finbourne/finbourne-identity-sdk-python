# LogAuthenticationProvider


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_authentication_provider import LogAuthenticationProvider

# TODO update the JSON string below
json = "{}"
# create an instance of LogAuthenticationProvider from a JSON string
log_authentication_provider_instance = LogAuthenticationProvider.from_json(json)
# print the JSON string representation of the object
print LogAuthenticationProvider.to_json()

# convert the object into a dict
log_authentication_provider_dict = log_authentication_provider_instance.to_dict()
# create an instance of LogAuthenticationProvider from a dict
log_authentication_provider_form_dict = log_authentication_provider.from_dict(log_authentication_provider_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


