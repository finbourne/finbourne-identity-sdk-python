# ClaimMappings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**login** | **str** |  | [optional] 
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**user_type** | **str** |  | 
**groups** | **str** |  | [optional] 
## Example

```python
from finbourne_identity.models.claim_mappings import ClaimMappings
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

user_id: Optional[StrictStr] = "example_user_id"
login: Optional[StrictStr] = "example_login"
email: StrictStr = "example_email"
first_name: StrictStr = "example_first_name"
last_name: StrictStr = "example_last_name"
user_type: StrictStr = "example_user_type"
groups: Optional[StrictStr] = "example_groups"
claim_mappings_instance = ClaimMappings(user_id=user_id, login=login, email=email, first_name=first_name, last_name=last_name, user_type=user_type, groups=groups)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

