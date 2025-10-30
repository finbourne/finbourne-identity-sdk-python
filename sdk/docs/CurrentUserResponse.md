# CurrentUserResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user&#39;s system supplied unique identifier | 
**email_address** | **str** | The user&#39;s email address which may be null depending on the authentication method | 
**type** | **str** | The type of user (e.g. Personal or Service) | 
**domain_type** | **str** | The type of domain in which the user exists | [optional] 
**user_expiry** | **datetime** | The user&#39;s user expiry datetime | [optional] 
**groups** | **List[str]** | The groups this user belongs to | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.current_user_response import CurrentUserResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
email_address: StrictStr = "example_email_address"
type: StrictStr = "example_type"
domain_type: Optional[StrictStr] = "example_domain_type"
user_expiry: Optional[datetime] = # Replace with your value
groups: Optional[List[StrictStr]] = # Replace with your value
links: Optional[List[Link]] = None
current_user_response_instance = CurrentUserResponse(id=id, email_address=email_address, type=type, domain_type=domain_type, user_expiry=user_expiry, groups=groups, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

