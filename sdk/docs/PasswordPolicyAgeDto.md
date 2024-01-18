# PasswordPolicyAgeDto


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_age_days** | **int** | The maximum age (in days) a password can be before expiring and needing to be changed | 
**history_count** | **int** | The number of unique passwords that need to be used before a previous password is permitted again | 

## Example

```python
from finbourne_identity.models.password_policy_age_dto import PasswordPolicyAgeDto

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordPolicyAgeDto from a JSON string
password_policy_age_dto_instance = PasswordPolicyAgeDto.from_json(json)
# print the JSON string representation of the object
print PasswordPolicyAgeDto.to_json()

# convert the object into a dict
password_policy_age_dto_dict = password_policy_age_dto_instance.to_dict()
# create an instance of PasswordPolicyAgeDto from a dict
password_policy_age_dto_form_dict = password_policy_age_dto.from_dict(password_policy_age_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


