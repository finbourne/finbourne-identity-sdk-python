# TemporaryPassword


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The user&#39;s temporary password | 

## Example

```python
from finbourne_identity.models.temporary_password import TemporaryPassword

# TODO update the JSON string below
json = "{}"
# create an instance of TemporaryPassword from a JSON string
temporary_password_instance = TemporaryPassword.from_json(json)
# print the JSON string representation of the object
print TemporaryPassword.to_json()

# convert the object into a dict
temporary_password_dict = temporary_password_instance.to_dict()
# create an instance of TemporaryPassword from a dict
temporary_password_form_dict = temporary_password.from_dict(temporary_password_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


