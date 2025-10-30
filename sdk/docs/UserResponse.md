# UserResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user&#39;s system supplied unique identifier | 
**alternative_user_ids** | **Dict[str, Optional[str]]** | The user&#39;s alternative IDs | [optional] 
**email_address** | **str** | The user&#39;s emailAddress address, which must be unique within the system | 
**second_email_address** | **str** | The user&#39;s second email address. Only allowed for service users. | [optional] 
**login** | **str** |  | 
**first_name** | **str** | The user&#39;s first name | 
**last_name** | **str** | The user&#39;s last name | 
**roles** | [**List[RoleResponse]**](RoleResponse.md) | The roles that the user has. | [optional] 
**type** | **str** | The type of user (e.g. Personal or Service) | 
**status** | **str** | The status of the user | 
**external** | **bool** | Whether or not the user originates from an external identity system | 
**last_login** | **datetime** | Last time the user logged in | [optional] 
**last_updated** | **datetime** | Last time the user was updated | [optional] 
**created** | **datetime** | Date the user was created | [optional] 
**password_changed** | **datetime** | Last time the password was changed for this user | [optional] 
**user_expiry** | **datetime** | The user&#39;s expiry unix datetime | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.user_response import UserResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
alternative_user_ids: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
email_address: StrictStr = "example_email_address"
second_email_address: Optional[StrictStr] = "example_second_email_address"
login: StrictStr = "example_login"
first_name: StrictStr = "example_first_name"
last_name: StrictStr = "example_last_name"
roles: Optional[List[RoleResponse]] = # Replace with your value
type: StrictStr = "example_type"
status: StrictStr = "example_status"
external: StrictBool = # Replace with your value
external:StrictBool = True
last_login: Optional[datetime] = # Replace with your value
last_updated: Optional[datetime] = # Replace with your value
created: Optional[datetime] = # Replace with your value
password_changed: Optional[datetime] = # Replace with your value
user_expiry: Optional[datetime] = # Replace with your value
links: Optional[List[Link]] = None
user_response_instance = UserResponse(id=id, alternative_user_ids=alternative_user_ids, email_address=email_address, second_email_address=second_email_address, login=login, first_name=first_name, last_name=last_name, roles=roles, type=type, status=status, external=external, last_login=last_login, last_updated=last_updated, created=created, password_changed=password_changed, user_expiry=user_expiry, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

