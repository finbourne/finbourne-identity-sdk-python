# UserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user&#39;s system supplied unique identifier | 
**alternative_user_ids** | **dict(str, str)** | The user&#39;s alternative IDs | [optional] 
**email_address** | **str** | The user&#39;s emailAddress address, which must be unique within the system | 
**second_email_address** | **str** | The user&#39;s second email address. Only allowed for service users. | [optional] 
**login** | **str** |  | 
**first_name** | **str** | The user&#39;s first name | 
**last_name** | **str** | The user&#39;s last name | 
**roles** | [**list[RoleResponse]**](RoleResponse.md) | The roles that the user has. | [optional] 
**type** | **str** | The type of user (e.g. Personal or Service) | 
**status** | **str** | The status of the user | 
**external** | **bool** | Whether or not the user originates from an external identity system | 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


