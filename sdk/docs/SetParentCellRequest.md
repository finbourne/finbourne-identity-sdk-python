# SetParentCellRequest

Request body for setting the parent cell.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_domain_name** | **str** | The name of the admin domain in the parent cell. | 
**confirm** | **bool** | Whether to confirm the parent cell attachment (second invocation). First call with false creates a Proposed state; second call with true transitions to Attaching. | 
## Example

```python
from finbourne_identity.models.set_parent_cell_request import SetParentCellRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

admin_domain_name: StrictStr = "example_admin_domain_name"
confirm: StrictBool = # Replace with your value
confirm:StrictBool = True
set_parent_cell_request_instance = SetParentCellRequest(admin_domain_name=admin_domain_name, confirm=confirm)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

