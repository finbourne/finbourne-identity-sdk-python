# UpdatePasswordPolicyRequestLockout

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_attempts** | **int** | The maximum number of unsuccessful attempts before the user is locked out of their account. 0 indicates no limit | 
## Example

```python
from finbourne_identity.models.update_password_policy_request_lockout import UpdatePasswordPolicyRequestLockout
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

max_attempts: StrictInt = # Replace with your value
max_attempts: StrictInt = 42
update_password_policy_request_lockout_instance = UpdatePasswordPolicyRequestLockout(max_attempts=max_attempts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

