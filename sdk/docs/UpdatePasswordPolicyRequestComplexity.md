# UpdatePasswordPolicyRequestComplexity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_length** | **int** | The minimum length for a password | 
**exclude_first_name** | **bool** | Rule determining whether a user&#39;s first name should be permitted in their password | 
**exclude_last_name** | **bool** | Rule determining whether a user&#39;s last name should be permitted in their password | 

## Example

```python
from finbourne_identity.models.update_password_policy_request_complexity import UpdatePasswordPolicyRequestComplexity

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordPolicyRequestComplexity from a JSON string
update_password_policy_request_complexity_instance = UpdatePasswordPolicyRequestComplexity.from_json(json)
# print the JSON string representation of the object
print UpdatePasswordPolicyRequestComplexity.to_json()

# convert the object into a dict
update_password_policy_request_complexity_dict = update_password_policy_request_complexity_instance.to_dict()
# create an instance of UpdatePasswordPolicyRequestComplexity from a dict
update_password_policy_request_complexity_form_dict = update_password_policy_request_complexity.from_dict(update_password_policy_request_complexity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


