# PasswordPolicyComplexityDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_length** | **int** | The minimum length for a password | 
**exclude_first_name** | **bool** | Rule determining whether a user&#39;s first name should be permitted in their password | 
**exclude_last_name** | **bool** | Rule determining whether a user&#39;s last name should be permitted in their password | 

## Example

```python
from finbourne_identity.models.password_policy_complexity_dto import PasswordPolicyComplexityDto

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyComplexityDto from a JSON string
password_policy_complexity_dto_instance = PasswordPolicyComplexityDto.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyComplexityDto.to_json()

# convert the object into a dict
password_policy_complexity_dto_dict = password_policy_complexity_dto_instance.to_dict()
# create an instance of PasswordPolicyComplexityDto from a dict
password_policy_complexity_dto_form_dict = password_policy_complexity_dto.from_dict(password_policy_complexity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


