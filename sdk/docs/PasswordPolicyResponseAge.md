# PasswordPolicyResponseAge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_age_days** | **int** | The maximum age (in days) a password can be before expiring and needing to be changed | 
**history_count** | **int** | The number of unique passwords that need to be used before a previous password is permitted again | 
## Example

```python
from finbourne_identity.models.password_policy_response_age import PasswordPolicyResponseAge
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt

max_age_days: StrictInt = # Replace with your value
max_age_days: StrictInt = 42
history_count: StrictInt = # Replace with your value
history_count: StrictInt = 42
password_policy_response_age_instance = PasswordPolicyResponseAge(max_age_days=max_age_days, history_count=history_count)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

