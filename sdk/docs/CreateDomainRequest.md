# CreateDomainRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The name LUSID domain to create | 
**description** | **str** | Optional. Free text description of the domain. | [optional] 
**company_name** | **str** | The name of the company to which the domain is registered | 
**owner** | [**CreateUserRequest**](CreateUserRequest.md) |  | 
**technical_contact** | [**CreateUserRequest**](CreateUserRequest.md) |  | [optional] 
**billing_contact** | [**CreateUserRequest**](CreateUserRequest.md) |  | [optional] 
**signed_agreements** | **list[str]** | Optional. If Terms and Conditions agreements have been signed during the sign up process | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


