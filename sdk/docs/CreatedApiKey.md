# CreatedApiKey

A newly created API key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The API Key value | 
**id** | **str** | The unique Id of the API key | 
**display_name** | **str** | The display name of the API key | 
**created_date** | **datetime** | The creation date of the API key | 
**deactivation_date** | **datetime** | The deactivation date of the API key | [optional] 

## Example

```python
from finbourne_identity.models.created_api_key import CreatedApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedApiKey from a JSON string
created_api_key_instance = CreatedApiKey.from_json(json)
# print the JSON string representation of the object
print CreatedApiKey.to_json()

# convert the object into a dict
created_api_key_dict = created_api_key_instance.to_dict()
# create an instance of CreatedApiKey from a dict
created_api_key_form_dict = created_api_key.from_dict(created_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


