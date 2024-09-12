# UserSchemaProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from finbourne_identity.models.user_schema_property import UserSchemaProperty

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaProperty from a JSON string
user_schema_property_instance = UserSchemaProperty.from_json(json)
# print the JSON string representation of the object
print UserSchemaProperty.to_json()

# convert the object into a dict
user_schema_property_dict = user_schema_property_instance.to_dict()
# create an instance of UserSchemaProperty from a dict
user_schema_property_form_dict = user_schema_property.from_dict(user_schema_property_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


