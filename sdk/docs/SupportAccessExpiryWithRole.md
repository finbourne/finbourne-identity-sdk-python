# SupportAccessExpiryWithRole

Time at which the support access granted for a role expires

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **datetime** | DateTimeOffset at which the access will be revoked | 
**permitted_role** | **str** | Unique identifier for permitted role.   Use GET /identity/api/authentication/support-roles to lookup role label/code from identifier. | 

## Example

```python
from finbourne_identity.models.support_access_expiry_with_role import SupportAccessExpiryWithRole

# TODO update the JSON string below
json = "{}"
# create an instance of SupportAccessExpiryWithRole from a JSON string
support_access_expiry_with_role_instance = SupportAccessExpiryWithRole.from_json(json)
# print the JSON string representation of the object
print SupportAccessExpiryWithRole.to_json()

# convert the object into a dict
support_access_expiry_with_role_dict = support_access_expiry_with_role_instance.to_dict()
# create an instance of SupportAccessExpiryWithRole from a dict
support_access_expiry_with_role_form_dict = support_access_expiry_with_role.from_dict(support_access_expiry_with_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


