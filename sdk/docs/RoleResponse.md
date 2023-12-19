# RoleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The role&#39;s system supplied unique identifier | 
**role_id** | [**RoleId**](RoleId.md) |  | 
**source** | **str** | The source of the role | 
**name** | **str** | The role name, which must be unique within the system. | 
**description** | **str** | The description for this role | [optional] 
**saml_name** | **str** | The name to use on the SAML request if assigning this role via SAML Just in Time (JIT) | [optional] 

## Example

```python
from finbourne_identity.models.role_response import RoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResponse from a JSON string
role_response_instance = RoleResponse.from_json(json)
# print the JSON string representation of the object
print RoleResponse.to_json()

# convert the object into a dict
role_response_dict = role_response_instance.to_dict()
# create an instance of RoleResponse from a dict
role_response_form_dict = role_response.from_dict(role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


