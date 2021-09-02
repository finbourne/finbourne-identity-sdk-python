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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


