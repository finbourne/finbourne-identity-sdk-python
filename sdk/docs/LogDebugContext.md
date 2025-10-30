# LogDebugContext

Represents a LogDebugContext resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debug_data** | **Dict[str, Optional[object]]** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_debug_context import LogDebugContext
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

debug_data: Optional[Dict[str, Any]] = # Replace with your value
log_debug_context_instance = LogDebugContext(debug_data=debug_data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

