# OAuthApplication


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**display_name** | **str** |  | 
**secret** | **str** |  | [optional] 
**client_id** | **str** |  | 
**issuer** | **str** |  | 

## Example

```python
from finbourne_identity.models.o_auth_application import OAuthApplication

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthApplication from a JSON string
o_auth_application_instance = OAuthApplication.from_json(json)
# print the JSON string representation of the object
print OAuthApplication.to_json()

# convert the object into a dict
o_auth_application_dict = o_auth_application_instance.to_dict()
# create an instance of OAuthApplication from a dict
o_auth_application_form_dict = o_auth_application.from_dict(o_auth_application_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


