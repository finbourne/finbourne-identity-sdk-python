# SetPassword

Set password request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the new password | 

## Example

```python
from finbourne_identity.models.set_password import SetPassword

# TODO update the JSON string below
json = "{}"
# create an instance of SetPassword from a JSON string
set_password_instance = SetPassword.from_json(json)
# print the JSON string representation of the object
print SetPassword.to_json()

# convert the object into a dict
set_password_dict = set_password_instance.to_dict()
# create an instance of SetPassword from a dict
set_password_form_dict = set_password.from_dict(set_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


