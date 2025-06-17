# CreateExternalTokenIssuerRequest

Client input for creating an external token issuer.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**issuer** | **str** |  | 
**audience** | **str** |  | 
**description** | **str** |  | [optional] 
**claim_mappings** | [**ClaimMappings**](ClaimMappings.md) |  | [optional] 
**logout_url** | **str** |  | 

## Example

```python
from finbourne_identity.models.create_external_token_issuer_request import CreateExternalTokenIssuerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateExternalTokenIssuerRequest from a JSON string
create_external_token_issuer_request_instance = CreateExternalTokenIssuerRequest.from_json(json)
# print the JSON string representation of the object
print CreateExternalTokenIssuerRequest.to_json()

# convert the object into a dict
create_external_token_issuer_request_dict = create_external_token_issuer_request_instance.to_dict()
# create an instance of CreateExternalTokenIssuerRequest from a dict
create_external_token_issuer_request_form_dict = create_external_token_issuer_request.from_dict(create_external_token_issuer_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


