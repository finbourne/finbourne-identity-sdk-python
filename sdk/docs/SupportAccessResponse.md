# SupportAccessResponse

Timestamped successful response to grant access to your account

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the support access request | 
**duration** | **str** | The duration for which access is requested (in any ISO-8601 format) | 
**description** | **str** | The description of why the support access has been granted (i.e. support ticket numbers) | [optional] 
**created_at** | **datetime** | DateTimeOffset at which the access was granted | 
**expiry** | **datetime** | DateTimeOffset at which the access will be revoked | 
**created_by** | **str** | Obfuscated UserId of the user who granted the support access | 
**terminated** | **bool** | Whether or not that access has been invalidated | [optional] 
**terminated_at** | **datetime** | DateTimeOffset at which the access was invalidated | [optional] 
**terminated_by** | **str** | Obfuscated UserId of the user who revoked the access | [optional] 
**permitted_roles** | **List[str]** | A list of permitted roles, valid for support staff to assume, for the duration of the access request | [optional] 

## Example

```python
from finbourne_identity.models.support_access_response import SupportAccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SupportAccessResponse from a JSON string
support_access_response_instance = SupportAccessResponse.from_json(json)
# print the JSON string representation of the object
print SupportAccessResponse.to_json()

# convert the object into a dict
support_access_response_dict = support_access_response_instance.to_dict()
# create an instance of SupportAccessResponse from a dict
support_access_response_form_dict = support_access_response.from_dict(support_access_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


