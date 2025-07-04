# UpdatePasswordPolicyRequestLockout

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_attempts** | **int** | The maximum number of unsuccessful attempts before the user is locked out of their account.  0 indicates no limit | 
## Example

```python
from finbourne_identity.models.update_password_policy_request_lockout import UpdatePasswordPolicyRequestLockout
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, conint

max_attempts: conint(strict=True, le=100, ge=0) = Field(..., alias="maxAttempts", description="The maximum number of unsuccessful attempts before the user is locked out of their account.  0 indicates no limit")
max_attempts: StrictInt = 42
update_password_policy_request_lockout_instance = UpdatePasswordPolicyRequestLockout(max_attempts=max_attempts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

