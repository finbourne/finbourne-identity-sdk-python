# CreateApplicationRequest

A request to create an application for authenticating the source of token requests

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The Display Name of the application | 
**client_id** | **str** | The OpenID Connect ClientId of the application | 
**type** | **str** | The Type of the application. This must be either Native or Web | 
**redirect_uris** | **list[str]** | A web application&#39;s acceptable list of post-login redirect URIs | [optional] 
**post_logout_redirect_uris** | **list[str]** | A web application&#39;s acceptable list of post-logout redirect URIs | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


