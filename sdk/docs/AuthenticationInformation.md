# AuthenticationInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer_url** | **str** |  | 
**fallback_issuer_urls** | **List[str]** |  | [optional] 
**saml_identity_provider_id** | **str** |  | [optional] 
**support** | [**SupportAccessExpiry**](SupportAccessExpiry.md) |  | [optional] 
**support_access_expiry_with_role** | [**List[SupportAccessExpiryWithRole]**](SupportAccessExpiryWithRole.md) |  | [optional] 
**status** | **bool** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.authentication_information import AuthenticationInformation
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

issuer_url: StrictStr = "example_issuer_url"
fallback_issuer_urls: Optional[List[StrictStr]] = # Replace with your value
saml_identity_provider_id: Optional[StrictStr] = "example_saml_identity_provider_id"
support: Optional[SupportAccessExpiry] = None
support_access_expiry_with_role: Optional[List[SupportAccessExpiryWithRole]] = # Replace with your value
status: Optional[StrictBool] = None
status:Optional[StrictBool] = None
links: Optional[List[Link]] = None
authentication_information_instance = AuthenticationInformation(issuer_url=issuer_url, fallback_issuer_urls=fallback_issuer_urls, saml_identity_provider_id=saml_identity_provider_id, support=support, support_access_expiry_with_role=support_access_expiry_with_role, status=status, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

