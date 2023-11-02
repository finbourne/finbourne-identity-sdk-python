# CreateApiKey

Create an API key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name for the API key | 
**deactivation_date** | **datetime** | The optional date at which the key should deactivate | [optional] 

## Example

```python
from finbourne_identity.models.create_api_key import CreateApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiKey from a JSON string
create_api_key_instance = CreateApiKey.from_json(json)
# print the JSON string representation of the object
print CreateApiKey.to_json()

# convert the object into a dict
create_api_key_dict = create_api_key_instance.to_dict()
# create an instance of CreateApiKey from a dict
create_api_key_form_dict = create_api_key.from_dict(create_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


