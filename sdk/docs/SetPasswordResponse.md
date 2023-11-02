# SetPasswordResponse

The result of setting a password

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** | The date and time at which the password was successfully updated | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.set_password_response import SetPasswordResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetPasswordResponse from a JSON string
set_password_response_instance = SetPasswordResponse.from_json(json)
# print the JSON string representation of the object
print SetPasswordResponse.to_json()

# convert the object into a dict
set_password_response_dict = set_password_response_instance.to_dict()
# create an instance of SetPasswordResponse from a dict
set_password_response_form_dict = set_password_response.from_dict(set_password_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


