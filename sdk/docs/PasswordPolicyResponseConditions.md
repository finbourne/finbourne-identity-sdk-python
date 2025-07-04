# PasswordPolicyResponseConditions

Password policy conditions for a password policy
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complexity** | [**PasswordPolicyResponseComplexity**](PasswordPolicyResponseComplexity.md) |  | 
**age** | [**PasswordPolicyResponseAge**](PasswordPolicyResponseAge.md) |  | 
**lockout** | [**PasswordPolicyResponseLockout**](PasswordPolicyResponseLockout.md) |  | 
## Example

```python
from finbourne_identity.models.password_policy_response_conditions import PasswordPolicyResponseConditions
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

complexity: PasswordPolicyResponseComplexity = # Replace with your value
age: PasswordPolicyResponseAge = # Replace with your value
lockout: PasswordPolicyResponseLockout = # Replace with your value
password_policy_response_conditions_instance = PasswordPolicyResponseConditions(complexity=complexity, age=age, lockout=lockout)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

