# CellParentStatusResponse

Response containing the current cell parent status.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | The current attachment status of the cell. | [optional] 
**admin_domain_name** | **str** | The name of the admin domain in the parent cell, if any. | [optional] 
**primary_domain_name** | **str** | The domain designated as the primary domain for this cell, if any. | [optional] 
**registration_step** | **str** | The most recently reached registration checkpoint, or null if no registration has started. One of &#x60;UserEnsured&#x60;, &#x60;PATGenerated&#x60;, &#x60;PATPushed&#x60;. | [optional] 
**registration_error** | **str** | Operator-readable message describing the most recent registration failure, or null on success. | [optional] 
## Example

```python
from finbourne_identity.models.cell_parent_status_response import CellParentStatusResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

status: Optional[StrictStr] = "example_status"
admin_domain_name: Optional[StrictStr] = "example_admin_domain_name"
primary_domain_name: Optional[StrictStr] = "example_primary_domain_name"
registration_step: Optional[StrictStr] = "example_registration_step"
registration_error: Optional[StrictStr] = "example_registration_error"
cell_parent_status_response_instance = CellParentStatusResponse(status=status, admin_domain_name=admin_domain_name, primary_domain_name=primary_domain_name, registration_step=registration_step, registration_error=registration_error)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

