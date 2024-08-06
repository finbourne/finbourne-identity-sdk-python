# UpdateRoleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description for this role | [optional] 

## Example

```python
from finbourne_identity.models.update_role_request import UpdateRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoleRequest from a JSON string
update_role_request_instance = UpdateRoleRequest.from_json(json)
# print the JSON string representation of the object
print UpdateRoleRequest.to_json()

# convert the object into a dict
update_role_request_dict = update_role_request_instance.to_dict()
# create an instance of UpdateRoleRequest from a dict
update_role_request_form_dict = update_role_request.from_dict(update_role_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


