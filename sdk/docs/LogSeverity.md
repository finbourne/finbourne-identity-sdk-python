# LogSeverity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_severity import LogSeverity
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictStr

value: Optional[StrictStr] = "example_value"
log_severity_instance = LogSeverity(value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

