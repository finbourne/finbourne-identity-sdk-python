# LogActor

Represents a LogActor resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**alternate_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**detail_entry** | **Dict[str, object]** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_actor import LogActor
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

id: Optional[StrictStr] = "example_id"
type: Optional[StrictStr] = "example_type"
alternate_id: Optional[StrictStr] = "example_alternate_id"
display_name: Optional[StrictStr] = "example_display_name"
detail_entry: Optional[Dict[str, Any]] = # Replace with your value
log_actor_instance = LogActor(id=id, type=type, alternate_id=alternate_id, display_name=display_name, detail_entry=detail_entry)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

