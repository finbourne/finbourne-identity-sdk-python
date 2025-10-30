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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

result: Optional[StrictStr] = "example_result"
reason: Optional[StrictStr] = "example_reason"
log_outcome_instance = LogOutcome(result=result, reason=reason)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

