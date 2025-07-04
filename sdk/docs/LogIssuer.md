# LogIssuer

Represents a LogIssuer resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_issuer import LogIssuer
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictStr

id: Optional[StrictStr] = "example_id"
type: Optional[StrictStr] = "example_type"
log_issuer_instance = LogIssuer(id=id, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

