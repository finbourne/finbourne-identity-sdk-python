# SessionPolicyResponse

Session timing settings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_session_idle_minutes** | **int** | Maximum minutes a user&#39;s session can be idle before re-authentication is required. | [optional] 
**max_session_lifetime_minutes** | **int** | Maximum minutes a user&#39;s session can live in total. When absent, sessions do not expire. | [optional] 
## Example

```python
from finbourne_identity.models.session_policy_response import SessionPolicyResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

max_session_idle_minutes: Optional[StrictInt] = # Replace with your value
max_session_lifetime_minutes: Optional[StrictInt] = # Replace with your value
session_policy_response_instance = SessionPolicyResponse(max_session_idle_minutes=max_session_idle_minutes, max_session_lifetime_minutes=max_session_lifetime_minutes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

