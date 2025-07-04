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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

code: Optional[StrictStr] = "example_code"
issuer: Optional[StrictStr] = "example_issuer"
audience: Optional[StrictStr] = "example_audience"
description: Optional[StrictStr] = "example_description"
claim_mappings: Optional[ClaimMappings] = # Replace with your value
logout_url: Optional[StrictStr] = "example_logout_url"
external_token_issuer_response_instance = ExternalTokenIssuerResponse(code=code, issuer=issuer, audience=audience, description=description, claim_mappings=claim_mappings, logout_url=logout_url)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

