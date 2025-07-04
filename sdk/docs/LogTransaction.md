# LogTransaction

Represents a LogTransaction resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**detail** | **Dict[str, object]** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_transaction import LogTransaction
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictStr

type: Optional[StrictStr] = "example_type"
id: Optional[StrictStr] = "example_id"
detail: Optional[Dict[str, Any]] = None
log_transaction_instance = LogTransaction(type=type, id=id, detail=detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

