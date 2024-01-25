# UpdatePasswordPolicyRequestLockout


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_attempts** | **int** | The maximum number of unsuccessful attempts before the user is locked out of their account.  0 indicates no limit | 

## Example

```python
from finbourne_identity.models.update_password_policy_request_lockout import UpdatePasswordPolicyRequestLockout

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordPolicyRequestLockout from a JSON string
update_password_policy_request_lockout_instance = UpdatePasswordPolicyRequestLockout.from_json(json)
# print the JSON string representation of the object
print UpdatePasswordPolicyRequestLockout.to_json()

# convert the object into a dict
update_password_policy_request_lockout_dict = update_password_policy_request_lockout_instance.to_dict()
# create an instance of UpdatePasswordPolicyRequestLockout from a dict
update_password_policy_request_lockout_form_dict = update_password_policy_request_lockout.from_dict(update_password_policy_request_lockout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


