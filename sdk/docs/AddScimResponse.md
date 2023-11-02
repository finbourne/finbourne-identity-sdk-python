# AddScimResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** |  | [optional] 
**api_token** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.add_scim_response import AddScimResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddScimResponse from a JSON string
add_scim_response_instance = AddScimResponse.from_json(json)
# print the JSON string representation of the object
print AddScimResponse.to_json()

# convert the object into a dict
add_scim_response_dict = add_scim_response_instance.to_dict()
# create an instance of AddScimResponse from a dict
add_scim_response_form_dict = add_scim_response.from_dict(add_scim_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


