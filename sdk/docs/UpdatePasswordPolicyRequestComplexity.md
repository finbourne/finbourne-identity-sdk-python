# UpdatePasswordPolicyRequestComplexity

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_length** | **int** | The minimum length for a password | 
**exclude_first_name** | **bool** | Rule determining whether a user&#39;s first name should be permitted in their password | 
**exclude_last_name** | **bool** | Rule determining whether a user&#39;s last name should be permitted in their password | 
## Example

```python
from finbourne_identity.models.update_password_policy_request_complexity import UpdatePasswordPolicyRequestComplexity
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictBool, conint

min_length: conint(strict=True, le=30, ge=12) = Field(..., alias="minLength", description="The minimum length for a password")
min_length: StrictInt = 42
exclude_first_name: StrictBool = # Replace with your value
exclude_first_name:StrictBool = True
exclude_last_name: StrictBool = # Replace with your value
exclude_last_name:StrictBool = True
update_password_policy_request_complexity_instance = UpdatePasswordPolicyRequestComplexity(min_length=min_length, exclude_first_name=exclude_first_name, exclude_last_name=exclude_last_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

