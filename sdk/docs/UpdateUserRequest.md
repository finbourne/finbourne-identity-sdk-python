# UpdateUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email_address** | **str** |  | 
**second_email_address** | **str** |  | [optional] 
**login** | **str** | The user&#39;s login username, in the form of an email address, which must be unique within the system.  For user accounts this should exactly match the user&#39;s email address. | 
**alternative_user_ids** | **dict(str, str)** |  | [optional] 
**roles** | [**list[RoleId]**](RoleId.md) | Deprecated. To update a user&#39;s roles use the AddUserToRole and RemoveUserFromRole endpoints | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


