# SupportRolesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**support_roles** | [**List[SupportRole]**](SupportRole.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.support_roles_response import SupportRolesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportRolesResponse from a JSON string
support_roles_response_instance = SupportRolesResponse.from_json(json)
# print the JSON string representation of the object
print SupportRolesResponse.to_json()

# convert the object into a dict
support_roles_response_dict = support_roles_response_instance.to_dict()
# create an instance of SupportRolesResponse from a dict
support_roles_response_form_dict = support_roles_response.from_dict(support_roles_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


