# CreateRoleRequest

Specifies the information required to create a new role.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The role name, which must be unique within the system. | 
**description** | **str** | The description for this role | [optional] 
## Example

```python
from finbourne_identity.models.create_role_request import CreateRoleRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
create_role_request_instance = CreateRoleRequest(name=name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

