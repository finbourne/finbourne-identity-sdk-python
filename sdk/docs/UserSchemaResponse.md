# UserSchemaResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternative_user_ids** | [**List[UserSchemaProperty]**](UserSchemaProperty.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.user_schema_response import UserSchemaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSchemaResponse from a JSON string
user_schema_response_instance = UserSchemaResponse.from_json(json)
# print the JSON string representation of the object
print UserSchemaResponse.to_json()

# convert the object into a dict
user_schema_response_dict = user_schema_response_instance.to_dict()
# create an instance of UserSchemaResponse from a dict
user_schema_response_form_dict = user_schema_response.from_dict(user_schema_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


