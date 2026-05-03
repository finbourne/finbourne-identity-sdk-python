# DetachParentCellRequest

Request body for `DetachParentCell`. The endpoint uses a double-invoke pattern: the first call (Finbourne.Lydia.WebApi.Dtos.CellManagement.DetachParentCellRequest.Confirm=false) transitions the cell into Finbourne.Lydia.Postgres.Database.DTO.AttachmentStatus.Detaching; the second call (Finbourne.Lydia.WebApi.Dtos.CellManagement.DetachParentCellRequest.Confirm=true) performs the actual detach.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirm** | **bool** | False to mark the cell as &#x60;Detaching&#x60;; true to execute the detach. | [optional] 
## Example

```python
from finbourne_identity.models.detach_parent_cell_request import DetachParentCellRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

confirm: Optional[StrictBool] = # Replace with your value
confirm:Optional[StrictBool] = None
detach_parent_cell_request_instance = DetachParentCellRequest(confirm=confirm)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

