# CreateUserRequest

Details necessary for creating a new user

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The first name of the user | 
**last_name** | **str** | The last name of the user | 
**email_address** | **str** | The user&#39;s email address - to which the account validation email will be sent. For user accounts  this should exactly match the Login. | 
**login** | **str** | The user&#39;s login username, in the form of an email address, which must be unique within the system.  For user accounts this should exactly match the user&#39;s email address. | 
**roles** | [**list[RoleId]**](RoleId.md) | Optional. Any known roles the user should be created with. | [optional] 
**type** | **str** | The type of user (e.g. Personal or Service) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


