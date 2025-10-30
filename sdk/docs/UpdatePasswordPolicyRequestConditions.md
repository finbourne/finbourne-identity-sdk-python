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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

complexity: UpdatePasswordPolicyRequestComplexity
age: UpdatePasswordPolicyRequestAge
lockout: UpdatePasswordPolicyRequestLockout
update_password_policy_request_conditions_instance = UpdatePasswordPolicyRequestConditions(complexity=complexity, age=age, lockout=lockout)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

