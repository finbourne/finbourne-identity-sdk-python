# ExternalTokenIssuerResponse

Response DTO exposed to client for an external token issuer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The External Token Issuer Code | [optional] 
**issuer** | **str** | Issuer of the External Token Issuer | [optional] 
**audience** | **str** | Audience of the External Token Issuer | [optional] 
**description** | **str** | The Description of the External Token Issuer | [optional] 
**claim_mappings** | [**ClaimMappings**](ClaimMappings.md) |  | [optional] 
**logout_url** | **str** | The LogoutUrl of the External Token Issuer | [optional] 

## Example

```python
from finbourne_identity.models.external_token_issuer_response import ExternalTokenIssuerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalTokenIssuerResponse from a JSON string
external_token_issuer_response_instance = ExternalTokenIssuerResponse.from_json(json)
# print the JSON string representation of the object
print ExternalTokenIssuerResponse.to_json()

# convert the object into a dict
external_token_issuer_response_dict = external_token_issuer_response_instance.to_dict()
# create an instance of ExternalTokenIssuerResponse from a dict
external_token_issuer_response_form_dict = external_token_issuer_response.from_dict(external_token_issuer_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


