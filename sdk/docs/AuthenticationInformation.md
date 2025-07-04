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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

issuer_url: StrictStr = "example_issuer_url"
fallback_issuer_urls: Optional[conlist(StrictStr)] = # Replace with your value
saml_identity_provider_id: Optional[StrictStr] = "example_saml_identity_provider_id"
support: Optional[SupportAccessExpiry] = None
support_access_expiry_with_role: Optional[conlist(SupportAccessExpiryWithRole)] = # Replace with your value
links: Optional[conlist(Link)] = None
authentication_information_instance = AuthenticationInformation(issuer_url=issuer_url, fallback_issuer_urls=fallback_issuer_urls, saml_identity_provider_id=saml_identity_provider_id, support=support, support_access_expiry_with_role=support_access_expiry_with_role, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

