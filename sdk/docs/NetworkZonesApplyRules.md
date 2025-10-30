# NetworkZonesApplyRules

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_type** | **List[str]** |  | 
**user_roles** | **List[str]** |  | 
## Example

```python
from finbourne_identity.models.network_zones_apply_rules import NetworkZonesApplyRules
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

session_type: List[StrictStr] = # Replace with your value
user_roles: List[StrictStr] = # Replace with your value
network_zones_apply_rules_instance = NetworkZonesApplyRules(session_type=session_type, user_roles=user_roles)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

