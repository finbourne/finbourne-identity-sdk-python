# ErrorDetail

Provides details about an entity error that occured
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the entity this error relates to | [optional] 
**type** | **str** | Error type | [optional] 
**detail** | **str** | Human readable description of the error | [optional] 
## Example

```python
from finbourne_identity.models.error_detail import ErrorDetail
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

id: Optional[StrictStr] = "example_id"
type: Optional[StrictStr] = "example_type"
detail: Optional[StrictStr] = "example_detail"
error_detail_instance = ErrorDetail(id=id, type=type, detail=detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

