# ClaimMappings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**login** | **str** |  | 
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**user_type** | **str** |  | 
**groups** | **str** |  | [optional] 
## Example

```python
from finbourne_identity.models.claim_mappings import ClaimMappings
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

user_id: StrictStr = "example_user_id"
login: StrictStr = "example_login"
email: StrictStr = "example_email"
first_name: StrictStr = "example_first_name"
last_name: StrictStr = "example_last_name"
user_type: StrictStr = "example_user_type"
groups: Optional[StrictStr] = "example_groups"
claim_mappings_instance = ClaimMappings(user_id=user_id, login=login, email=email, first_name=first_name, last_name=last_name, user_type=user_type, groups=groups)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

