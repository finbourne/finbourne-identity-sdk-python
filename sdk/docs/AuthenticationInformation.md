# AuthenticationInformation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_url** | **str** |  | 
**fallback_issuer_urls** | **List[str]** |  | [optional] 
**saml_identity_provider_id** | **str** |  | [optional] 
**support** | [**SupportAccessExpiry**](SupportAccessExpiry.md) |  | [optional] 
**support_access_expiry_with_role** | [**List[SupportAccessExpiryWithRole]**](SupportAccessExpiryWithRole.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.authentication_information import AuthenticationInformation

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationInformation from a JSON string
authentication_information_instance = AuthenticationInformation.from_json(json)
# print the JSON string representation of the object
print AuthenticationInformation.to_json()

# convert the object into a dict
authentication_information_dict = authentication_information_instance.to_dict()
# create an instance of AuthenticationInformation from a dict
authentication_information_form_dict = authentication_information.from_dict(authentication_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


