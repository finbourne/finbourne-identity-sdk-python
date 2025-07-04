# PasswordPolicyResponseLockout

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_attempts** | **int** | The maximum number of unsuccessful attempts before the user is locked out of their account | 
## Example

```python
from finbourne_identity.models.password_policy_response_lockout import PasswordPolicyResponseLockout
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt

max_attempts: StrictInt = # Replace with your value
max_attempts: StrictInt = 42
password_policy_response_lockout_instance = PasswordPolicyResponseLockout(max_attempts=max_attempts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

