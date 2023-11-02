# SupportAccessRequest

A Request to grant support access to your account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The duration for which access is requested (in any ISO-8601 format) | 
**description** | **str** | The description of why the support access has been granted (i.e. support ticket numbers) | [optional] 
**permitted_roles** | **List[str]** |  | [optional] 

## Example

```python
from finbourne_identity.models.support_access_request import SupportAccessRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SupportAccessRequest from a JSON string
support_access_request_instance = SupportAccessRequest.from_json(json)
# print the JSON string representation of the object
print SupportAccessRequest.to_json()

# convert the object into a dict
support_access_request_dict = support_access_request_instance.to_dict()
# create an instance of SupportAccessRequest from a dict
support_access_request_form_dict = support_access_request.from_dict(support_access_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


