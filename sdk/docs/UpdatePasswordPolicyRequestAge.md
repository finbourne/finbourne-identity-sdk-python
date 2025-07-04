# UpdatePasswordPolicyRequestAge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_age_days** | **int** | The maximum age (in days) a password can be before expiring and needing to be changed.  0 indicates no limit | 
**history_count** | **int** | The number of unique passwords that need to be used before a previous password is permitted again.  0 indicates none | 
## Example

```python
from finbourne_identity.models.update_password_policy_request_age import UpdatePasswordPolicyRequestAge
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, conint

max_age_days: conint(strict=True, le=999, ge=0) = Field(..., alias="maxAgeDays", description="The maximum age (in days) a password can be before expiring and needing to be changed.  0 indicates no limit")
max_age_days: StrictInt = 42
history_count: conint(strict=True, le=30, ge=0) = Field(..., alias="historyCount", description="The number of unique passwords that need to be used before a previous password is permitted again.  0 indicates none")
history_count: StrictInt = 42
update_password_policy_request_age_instance = UpdatePasswordPolicyRequestAge(max_age_days=max_age_days, history_count=history_count)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

