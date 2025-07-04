# UpdateRoleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description for this role | [optional] 
## Example

```python
from finbourne_identity.models.update_role_request import UpdateRoleRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

description: Optional[StrictStr] = "example_description"
update_role_request_instance = UpdateRoleRequest(description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

