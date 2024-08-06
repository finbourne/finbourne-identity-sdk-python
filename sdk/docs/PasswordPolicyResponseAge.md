# PasswordPolicyResponseAge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_age_days** | **int** | The maximum age (in days) a password can be before expiring and needing to be changed | 
**history_count** | **int** | The number of unique passwords that need to be used before a previous password is permitted again | 

## Example

```python
from finbourne_identity.models.password_policy_response_age import PasswordPolicyResponseAge

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyResponseAge from a JSON string
password_policy_response_age_instance = PasswordPolicyResponseAge.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyResponseAge.to_json()

# convert the object into a dict
password_policy_response_age_dict = password_policy_response_age_instance.to_dict()
# create an instance of PasswordPolicyResponseAge from a dict
password_policy_response_age_form_dict = password_policy_response_age.from_dict(password_policy_response_age_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


