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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

complexity: PasswordPolicyResponseComplexity
age: PasswordPolicyResponseAge
lockout: PasswordPolicyResponseLockout
password_policy_response_conditions_instance = PasswordPolicyResponseConditions(complexity=complexity, age=age, lockout=lockout)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

