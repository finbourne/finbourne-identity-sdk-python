# CreateUserRequest

Details necessary for creating a new user

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The first name of the user | 
**last_name** | **str** | The last name of the user | 
**email_address** | **str** | The user&#39;s email address - to which the account validation email will be sent. For user accounts  this should exactly match the Login. | 
**second_email_address** | **str** | The user&#39;s second email address. Only allowed for Service users | [optional] 
**login** | **str** | The user&#39;s login username, in the form of an email address, which must be unique within the system.  For user accounts this should exactly match the user&#39;s email address. | 
**roles** | [**List[RoleId]**](RoleId.md) | Optional. Any known roles the user should be created with. | [optional] 
**type** | **str** | The type of user (e.g. Personal or Service) | 

## Example

```python
from finbourne_identity.models.create_user_request import CreateUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRequest from a JSON string
create_user_request_instance = CreateUserRequest.from_json(json)
# print the JSON string representation of the object
print CreateUserRequest.to_json()

# convert the object into a dict
create_user_request_dict = create_user_request_instance.to_dict()
# create an instance of CreateUserRequest from a dict
create_user_request_form_dict = create_user_request.from_dict(create_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


