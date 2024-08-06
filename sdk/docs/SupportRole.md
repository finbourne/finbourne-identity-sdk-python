# SupportRole


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**role_identifier** | **Dict[str, str]** |  | [optional] 
**internal_identifier** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.support_role import SupportRole

# TODO update the JSON string below
json = "{}"
# create an instance of SupportRole from a JSON string
support_role_instance = SupportRole.from_json(json)
# print the JSON string representation of the object
print SupportRole.to_json()

# convert the object into a dict
support_role_dict = support_role_instance.to_dict()
# create an instance of SupportRole from a dict
support_role_form_dict = support_role.from_dict(support_role_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


