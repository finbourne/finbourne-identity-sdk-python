# ApiKey

The metadata of an API key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique Id of the API key | 
**display_name** | **str** | The display name of the API key | 
**created_date** | **datetime** | The creation date of the API key | 
**deactivation_date** | **datetime** | The deactivation date of the API key | [optional] 

## Example

```python
from finbourne_identity.models.api_key import ApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKey from a JSON string
api_key_instance = ApiKey.from_json(json)
# print the JSON string representation of the object
print ApiKey.to_json()

# convert the object into a dict
api_key_dict = api_key_instance.to_dict()
# create an instance of ApiKey from a dict
api_key_form_dict = api_key.from_dict(api_key_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


