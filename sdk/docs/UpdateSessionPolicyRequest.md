# UpdateSessionPolicyRequest

Session timing settings.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_session_idle_minutes** | **int** | Maximum minutes a user&#39;s session can be idle before re-authentication is required. Must be between 5 minutes and 12 hours (720 minutes). | 
**max_session_lifetime_minutes** | **int** | Maximum minutes a user&#39;s session can live in total. Omit to disable session expiry; otherwise must be between 5 minutes and 24 hours (1440 minutes). | [optional] 
## Example

```python
from finbourne_identity.models.update_session_policy_request import UpdateSessionPolicyRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

max_session_idle_minutes: StrictInt = # Replace with your value
max_session_lifetime_minutes: Optional[StrictInt] = # Replace with your value
update_session_policy_request_instance = UpdateSessionPolicyRequest(max_session_idle_minutes=max_session_idle_minutes, max_session_lifetime_minutes=max_session_lifetime_minutes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

