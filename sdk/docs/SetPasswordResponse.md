# SetPasswordResponse

The result of setting a password
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** | The date and time at which the password was successfully updated | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.set_password_response import SetPasswordResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist
from datetime import datetime
updated_at: datetime = # Replace with your value
links: Optional[conlist(Link)] = None
set_password_response_instance = SetPasswordResponse(updated_at=updated_at, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

