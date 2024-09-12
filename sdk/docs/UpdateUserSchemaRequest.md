# UpdateUserSchemaRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternative_user_ids** | [**List[UserSchemaProperty]**](UserSchemaProperty.md) |  | 

## Example

```python
from finbourne_identity.models.update_user_schema_request import UpdateUserSchemaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserSchemaRequest from a JSON string
update_user_schema_request_instance = UpdateUserSchemaRequest.from_json(json)
# print the JSON string representation of the object
print UpdateUserSchemaRequest.to_json()

# convert the object into a dict
update_user_schema_request_dict = update_user_schema_request_instance.to_dict()
# create an instance of UpdateUserSchemaRequest from a dict
update_user_schema_request_form_dict = update_user_schema_request.from_dict(update_user_schema_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


