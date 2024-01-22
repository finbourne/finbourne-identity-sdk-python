# UpdatePasswordPolicyRequestAge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_age_days** | **int** | The maximum age (in days) a password can be before expiring and needing to be changed | 
**history_count** | **int** | The number of unique passwords that need to be used before a previous password is permitted again | 

## Example

```python
from finbourne_identity.models.update_password_policy_request_age import UpdatePasswordPolicyRequestAge

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordPolicyRequestAge from a JSON string
update_password_policy_request_age_instance = UpdatePasswordPolicyRequestAge.from_json(json)
# print the JSON string representation of the object
print UpdatePasswordPolicyRequestAge.to_json()

# convert the object into a dict
update_password_policy_request_age_dict = update_password_policy_request_age_instance.to_dict()
# create an instance of UpdatePasswordPolicyRequestAge from a dict
update_password_policy_request_age_form_dict = update_password_policy_request_age.from_dict(update_password_policy_request_age_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


