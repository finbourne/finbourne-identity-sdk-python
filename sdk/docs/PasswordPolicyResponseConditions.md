# PasswordPolicyResponseConditions

Password policy conditions for a password policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | [**PasswordPolicyResponseComplexity**](PasswordPolicyResponseComplexity.md) |  | 
**age** | [**PasswordPolicyResponseAge**](PasswordPolicyResponseAge.md) |  | 
**lockout** | [**PasswordPolicyResponseLockout**](PasswordPolicyResponseLockout.md) |  | 

## Example

```python
from finbourne_identity.models.password_policy_response_conditions import PasswordPolicyResponseConditions

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyResponseConditions from a JSON string
password_policy_response_conditions_instance = PasswordPolicyResponseConditions.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyResponseConditions.to_json()

# convert the object into a dict
password_policy_response_conditions_dict = password_policy_response_conditions_instance.to_dict()
# create an instance of PasswordPolicyResponseConditions from a dict
password_policy_response_conditions_form_dict = password_policy_response_conditions.from_dict(password_policy_response_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


