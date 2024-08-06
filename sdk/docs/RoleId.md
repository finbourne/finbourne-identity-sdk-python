# RoleId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from finbourne_identity.models.role_id import RoleId

# TODO update the JSON string below
json = "{}"
# create an instance of RoleId from a JSON string
role_id_instance = RoleId.from_json(json)
# print the JSON string representation of the object
print RoleId.to_json()

# convert the object into a dict
role_id_dict = role_id_instance.to_dict()
# create an instance of RoleId from a dict
role_id_form_dict = role_id.from_dict(role_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


