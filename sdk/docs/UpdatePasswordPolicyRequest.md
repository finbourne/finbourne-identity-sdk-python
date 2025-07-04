# UpdatePasswordPolicyRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**UpdatePasswordPolicyRequestConditions**](UpdatePasswordPolicyRequestConditions.md) |  | 
## Example

```python
from finbourne_identity.models.update_password_policy_request import UpdatePasswordPolicyRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

conditions: UpdatePasswordPolicyRequestConditions = # Replace with your value
update_password_policy_request_instance = UpdatePasswordPolicyRequest(conditions=conditions)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

