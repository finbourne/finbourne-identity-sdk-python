# SupportAccessExpiryWithRole

Time at which the support access granted for a role expires
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **datetime** | DateTimeOffset at which the access will be revoked | 
**permitted_role** | **str** | Unique identifier for permitted role.  Use GET /identity/api/authentication/support-roles to lookup role label/code from identifier. | 
## Example

```python
from finbourne_identity.models.support_access_expiry_with_role import SupportAccessExpiryWithRole
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

expiry: datetime = # Replace with your value
permitted_role: StrictStr = "example_permitted_role"
support_access_expiry_with_role_instance = SupportAccessExpiryWithRole(expiry=expiry, permitted_role=permitted_role)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

