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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

code: StrictStr = "example_code"
issuer: StrictStr = "example_issuer"
audience: StrictStr = "example_audience"
description: Optional[StrictStr] = "example_description"
claim_mappings: Optional[ClaimMappings] = # Replace with your value
logout_url: StrictStr = "example_logout_url"
create_external_token_issuer_request_instance = CreateExternalTokenIssuerRequest(code=code, issuer=issuer, audience=audience, description=description, claim_mappings=claim_mappings, logout_url=logout_url)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

