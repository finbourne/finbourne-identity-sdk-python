# PasswordPolicyConditions

Password policy conditions for a password policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | [**PasswordPolicyComplexity**](PasswordPolicyComplexity.md) |  | [optional] 
**age** | [**PasswordPolicyAge**](PasswordPolicyAge.md) |  | [optional] 
**lockout** | [**PasswordPolicyLockout**](PasswordPolicyLockout.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.password_policy_conditions import PasswordPolicyConditions

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyConditions from a JSON string
password_policy_conditions_instance = PasswordPolicyConditions.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyConditions.to_json()

# convert the object into a dict
password_policy_conditions_dict = password_policy_conditions_instance.to_dict()
# create an instance of PasswordPolicyConditions from a dict
password_policy_conditions_form_dict = password_policy_conditions.from_dict(password_policy_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


