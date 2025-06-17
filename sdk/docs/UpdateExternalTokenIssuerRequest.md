# UpdateExternalTokenIssuerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** |  | [optional] 
**audience** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**claim_mappings** | [**ClaimMappings**](ClaimMappings.md) |  | [optional] 
**logout_url** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.update_external_token_issuer_request import UpdateExternalTokenIssuerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateExternalTokenIssuerRequest from a JSON string
update_external_token_issuer_request_instance = UpdateExternalTokenIssuerRequest.from_json(json)
# print the JSON string representation of the object
print UpdateExternalTokenIssuerRequest.to_json()

# convert the object into a dict
update_external_token_issuer_request_dict = update_external_token_issuer_request_instance.to_dict()
# create an instance of UpdateExternalTokenIssuerRequest from a dict
update_external_token_issuer_request_form_dict = update_external_token_issuer_request.from_dict(update_external_token_issuer_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


