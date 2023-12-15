# PasswordPolicyLockout


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_attempts** | **int** | The maximum number of unsuccessful attempts before the user is locked out of their account | [optional] 

## Example

```python
from finbourne_identity.models.password_policy_lockout import PasswordPolicyLockout

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyLockout from a JSON string
password_policy_lockout_instance = PasswordPolicyLockout.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyLockout.to_json()

# convert the object into a dict
password_policy_lockout_dict = password_policy_lockout_instance.to_dict()
# create an instance of PasswordPolicyLockout from a dict
password_policy_lockout_form_dict = password_policy_lockout.from_dict(password_policy_lockout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


