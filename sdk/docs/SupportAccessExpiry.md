# SupportAccessExpiry

Time at which the support access expires
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **datetime** | DateTimeOffset at which the access will be revoked | 
## Example

```python
from finbourne_identity.models.support_access_expiry import SupportAccessExpiry
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

expiry: datetime = # Replace with your value
support_access_expiry_instance = SupportAccessExpiry(expiry=expiry)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

