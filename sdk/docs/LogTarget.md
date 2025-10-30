# LogTarget

Represents a LogTarget resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**alternate_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**detail_entry** | **Dict[str, Optional[object]]** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_target import LogTarget
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
type: Optional[StrictStr] = "example_type"
alternate_id: Optional[StrictStr] = "example_alternate_id"
display_name: Optional[StrictStr] = "example_display_name"
detail_entry: Optional[Dict[str, Any]] = # Replace with your value
log_target_instance = LogTarget(id=id, type=type, alternate_id=alternate_id, display_name=display_name, detail_entry=detail_entry)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

