# SupportRolesResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**support_roles** | [**List[SupportRole]**](SupportRole.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.support_roles_response import SupportRolesResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

support_roles: Optional[conlist(SupportRole)] = # Replace with your value
support_roles_response_instance = SupportRolesResponse(support_roles=support_roles)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

