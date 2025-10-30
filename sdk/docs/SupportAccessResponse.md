# SupportAccessResponse

Timestamped successful response to grant access to your account
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the support access request | 
**duration** | **str** | The duration for which access is requested (in any ISO-8601 format) | 
**description** | **str** | The description of why the support access has been granted (i.e. support ticket numbers) | [optional] 
**created_at** | **datetime** | DateTimeOffset at which the access was granted | 
**expiry** | **datetime** | DateTimeOffset at which the access will be revoked | 
**created_by** | **str** | Obfuscated UserId of the user who granted the support access | 
**terminated** | **bool** | Whether or not that access has been invalidated | [optional] 
**terminated_at** | **datetime** | DateTimeOffset at which the access was invalidated | [optional] 
**terminated_by** | **str** | Obfuscated UserId of the user who revoked the access | [optional] 
**permitted_roles** | **List[str]** | A list of permitted roles, valid for support staff to assume, for the duration of the access request | [optional] 
## Example

```python
from finbourne_identity.models.support_access_response import SupportAccessResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
duration: StrictStr = "example_duration"
description: Optional[StrictStr] = "example_description"
created_at: datetime = # Replace with your value
expiry: datetime = # Replace with your value
created_by: StrictStr = "example_created_by"
terminated: Optional[StrictBool] = # Replace with your value
terminated:Optional[StrictBool] = None
terminated_at: Optional[datetime] = # Replace with your value
terminated_by: Optional[StrictStr] = "example_terminated_by"
permitted_roles: Optional[List[StrictStr]] = # Replace with your value
support_access_response_instance = SupportAccessResponse(id=id, duration=duration, description=description, created_at=created_at, expiry=expiry, created_by=created_by, terminated=terminated, terminated_at=terminated_at, terminated_by=terminated_by, permitted_roles=permitted_roles)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

