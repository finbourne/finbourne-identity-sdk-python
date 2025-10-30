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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

issuer: Optional[StrictStr] = "example_issuer"
audience: Optional[StrictStr] = "example_audience"
description: Optional[StrictStr] = "example_description"
claim_mappings: Optional[ClaimMappings] = # Replace with your value
logout_url: Optional[StrictStr] = "example_logout_url"
update_external_token_issuer_request_instance = UpdateExternalTokenIssuerRequest(issuer=issuer, audience=audience, description=description, claim_mappings=claim_mappings, logout_url=logout_url)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

