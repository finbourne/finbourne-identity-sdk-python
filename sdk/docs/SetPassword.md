# SetPassword

Set password request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the new password | 
## Example

```python
from finbourne_identity.models.set_password import SetPassword
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr

value: StrictStr = "example_value"
set_password_instance = SetPassword(value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

