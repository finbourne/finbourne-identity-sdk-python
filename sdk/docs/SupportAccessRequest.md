# SupportAccessRequest

A Request to grant support access to your account
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **str** | The duration for which access is requested (in any ISO-8601 format) | 
**description** | **str** | The description of why the support access has been granted (i.e. support ticket numbers) | [optional] 
**permitted_roles** | **List[str]** |  | [optional] 
## Example

```python
from finbourne_identity.models.support_access_request import SupportAccessRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

duration: StrictStr = "example_duration"
description: Optional[StrictStr] = "example_description"
permitted_roles: Optional[List[StrictStr]] = # Replace with your value
support_access_request_instance = SupportAccessRequest(duration=duration, description=description, permitted_roles=permitted_roles)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

