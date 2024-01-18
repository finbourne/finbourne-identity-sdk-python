# PasswordPolicyLockoutDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_attempts** | **int** | The maximum number of unsuccessful attempts before the user is locked out of their account | 

## Example

```python
from finbourne_identity.models.password_policy_lockout_dto import PasswordPolicyLockoutDto

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyLockoutDto from a JSON string
password_policy_lockout_dto_instance = PasswordPolicyLockoutDto.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyLockoutDto.to_json()

# convert the object into a dict
password_policy_lockout_dto_dict = password_policy_lockout_dto_instance.to_dict()
# create an instance of PasswordPolicyLockoutDto from a dict
password_policy_lockout_dto_form_dict = password_policy_lockout_dto.from_dict(password_policy_lockout_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


