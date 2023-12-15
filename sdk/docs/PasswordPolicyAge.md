# PasswordPolicyAge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_age_days** | **int** | The maximum age (in days) a password can be before expiring and needing to be changed | [optional] 
**history_count** | **int** | The number of unique passwords that need to be used before a previous password is permitted again | [optional] 

## Example

```python
from finbourne_identity.models.password_policy_age import PasswordPolicyAge

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyAge from a JSON string
password_policy_age_instance = PasswordPolicyAge.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyAge.to_json()

# convert the object into a dict
password_policy_age_dict = password_policy_age_instance.to_dict()
# create an instance of PasswordPolicyAge from a dict
password_policy_age_form_dict = password_policy_age.from_dict(password_policy_age_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


