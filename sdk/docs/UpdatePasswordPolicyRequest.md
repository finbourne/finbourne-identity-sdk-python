# UpdatePasswordPolicyRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**UpdatePasswordPolicyRequestConditions**](UpdatePasswordPolicyRequestConditions.md) |  | 

## Example

```python
from finbourne_identity.models.update_password_policy_request import UpdatePasswordPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordPolicyRequest from a JSON string
update_password_policy_request_instance = UpdatePasswordPolicyRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePasswordPolicyRequest.to_json()

# convert the object into a dict
update_password_policy_request_dict = update_password_policy_request_instance.to_dict()
# create an instance of UpdatePasswordPolicyRequest from a dict
update_password_policy_request_form_dict = update_password_policy_request.from_dict(update_password_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


