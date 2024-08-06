# UpdatePasswordPolicyRequestConditions

Password policy conditions for a password policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | [**UpdatePasswordPolicyRequestComplexity**](UpdatePasswordPolicyRequestComplexity.md) |  | 
**age** | [**UpdatePasswordPolicyRequestAge**](UpdatePasswordPolicyRequestAge.md) |  | 
**lockout** | [**UpdatePasswordPolicyRequestLockout**](UpdatePasswordPolicyRequestLockout.md) |  | 

## Example

```python
from finbourne_identity.models.update_password_policy_request_conditions import UpdatePasswordPolicyRequestConditions

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordPolicyRequestConditions from a JSON string
update_password_policy_request_conditions_instance = UpdatePasswordPolicyRequestConditions.from_json(json)
# print the JSON string representation of the object
print UpdatePasswordPolicyRequestConditions.to_json()

# convert the object into a dict
update_password_policy_request_conditions_dict = update_password_policy_request_conditions_instance.to_dict()
# create an instance of UpdatePasswordPolicyRequestConditions from a dict
update_password_policy_request_conditions_form_dict = update_password_policy_request_conditions.from_dict(update_password_policy_request_conditions_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


