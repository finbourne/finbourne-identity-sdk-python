# UpdatePasswordPolicyRequestConditions

Password policy conditions for a password policy
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | [**UpdatePasswordPolicyRequestComplexity**](UpdatePasswordPolicyRequestComplexity.md) |  | 
**age** | [**UpdatePasswordPolicyRequestAge**](UpdatePasswordPolicyRequestAge.md) |  | 
**lockout** | [**UpdatePasswordPolicyRequestLockout**](UpdatePasswordPolicyRequestLockout.md) |  | 
## Example

```python
from finbourne_identity.models.update_password_policy_request_conditions import UpdatePasswordPolicyRequestConditions
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

complexity: UpdatePasswordPolicyRequestComplexity = # Replace with your value
age: UpdatePasswordPolicyRequestAge = # Replace with your value
lockout: UpdatePasswordPolicyRequestLockout = # Replace with your value
update_password_policy_request_conditions_instance = UpdatePasswordPolicyRequestConditions(complexity=complexity, age=age, lockout=lockout)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

