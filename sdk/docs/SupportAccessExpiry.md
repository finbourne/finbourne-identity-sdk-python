# SupportAccessExpiry

Time at which the support access expires

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **datetime** | DateTimeOffset at which the access will be revoked | 

## Example

```python
from finbourne_identity.models.support_access_expiry import SupportAccessExpiry

# TODO update the JSON string below
json = "{}"
# create an instance of SupportAccessExpiry from a JSON string
support_access_expiry_instance = SupportAccessExpiry.from_json(json)
# print the JSON string representation of the object
print SupportAccessExpiry.to_json()

# convert the object into a dict
support_access_expiry_dict = support_access_expiry_instance.to_dict()
# create an instance of SupportAccessExpiry from a dict
support_access_expiry_form_dict = support_access_expiry.from_dict(support_access_expiry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


