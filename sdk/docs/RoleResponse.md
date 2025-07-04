# RoleResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The role&#39;s system supplied unique identifier | 
**role_id** | [**RoleId**](RoleId.md) |  | 
**source** | **str** | The source of the role | 
**name** | **str** | The role name, which must be unique within the system. | 
**description** | **str** | The description for this role | [optional] 
**saml_name** | **str** | The name to use on the SAML request if assigning this role via SAML Just in Time (JIT) | [optional] 
## Example

```python
from finbourne_identity.models.role_response import RoleResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

id: StrictStr = "example_id"
role_id: RoleId = # Replace with your value
source: StrictStr = "example_source"
name: StrictStr = "example_name"
description: Optional[StrictStr] = "example_description"
saml_name: Optional[StrictStr] = "example_saml_name"
role_response_instance = RoleResponse(id=id, role_id=role_id, source=source, name=name, description=description, saml_name=saml_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

