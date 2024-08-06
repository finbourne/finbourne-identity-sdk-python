# PasswordPolicyResponseLockout


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_attempts** | **int** | The maximum number of unsuccessful attempts before the user is locked out of their account | 

## Example

```python
from finbourne_identity.models.password_policy_response_lockout import PasswordPolicyResponseLockout

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyResponseLockout from a JSON string
password_policy_response_lockout_instance = PasswordPolicyResponseLockout.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyResponseLockout.to_json()

# convert the object into a dict
password_policy_response_lockout_dict = password_policy_response_lockout_instance.to_dict()
# create an instance of PasswordPolicyResponseLockout from a dict
password_policy_response_lockout_form_dict = password_policy_response_lockout.from_dict(password_policy_response_lockout_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


