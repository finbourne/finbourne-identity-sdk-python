# LogOutcome

Represents a LogOutcome resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_outcome import LogOutcome
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictStr

result: Optional[StrictStr] = "example_result"
reason: Optional[StrictStr] = "example_reason"
log_outcome_instance = LogOutcome(result=result, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

