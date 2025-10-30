# PasswordPolicyResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**PasswordPolicyResponseConditions**](PasswordPolicyResponseConditions.md) |  | 
## Example

```python
from finbourne_identity.models.password_policy_response import PasswordPolicyResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

conditions: PasswordPolicyResponseConditions
password_policy_response_instance = PasswordPolicyResponse(conditions=conditions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

