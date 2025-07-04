# TemporaryPassword

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The user&#39;s temporary password | 
## Example

```python
from finbourne_identity.models.temporary_password import TemporaryPassword
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

password: StrictStr = "example_password"
temporary_password_instance = TemporaryPassword(password=password)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

