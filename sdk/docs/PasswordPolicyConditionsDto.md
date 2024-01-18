# PasswordPolicyConditionsDto

Password policy conditions for a password policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | [**PasswordPolicyComplexityDto**](PasswordPolicyComplexityDto.md) |  | 
**age** | [**PasswordPolicyAgeDto**](PasswordPolicyAgeDto.md) |  | 
**lockout** | [**PasswordPolicyLockoutDto**](PasswordPolicyLockoutDto.md) |  | 

## Example

```python
from finbourne_identity.models.password_policy_conditions_dto import PasswordPolicyConditionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyConditionsDto from a JSON string
password_policy_conditions_dto_instance = PasswordPolicyConditionsDto.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyConditionsDto.to_json()

# convert the object into a dict
password_policy_conditions_dto_dict = password_policy_conditions_dto_instance.to_dict()
# create an instance of PasswordPolicyConditionsDto from a dict
password_policy_conditions_dto_form_dict = password_policy_conditions_dto.from_dict(password_policy_conditions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


