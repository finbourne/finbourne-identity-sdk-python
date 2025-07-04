# UserResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user&#39;s system supplied unique identifier | 
**alternative_user_ids** | **Dict[str, str]** | The user&#39;s alternative IDs | [optional] 
**email_address** | **str** | The user&#39;s emailAddress address, which must be unique within the system | 
**second_email_address** | **str** | The user&#39;s second email address. Only allowed for service users. | [optional] 
**login** | **str** |  | 
**first_name** | **str** | The user&#39;s first name | 
**last_name** | **str** | The user&#39;s last name | 
**roles** | [**List[RoleResponse]**](RoleResponse.md) | The roles that the user has. | [optional] 
**type** | **str** | The type of user (e.g. Personal or Service) | 
**status** | **str** | The status of the user | 
**external** | **bool** | Whether or not the user originates from an external identity system | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.user_response import UserResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr

id: StrictStr = "example_id"
alternative_user_ids: Optional[Dict[str, StrictStr]] = # Replace with your value
email_address: StrictStr = "example_email_address"
second_email_address: Optional[StrictStr] = "example_second_email_address"
login: StrictStr = "example_login"
first_name: StrictStr = "example_first_name"
last_name: StrictStr = "example_last_name"
roles: Optional[conlist(RoleResponse)] = # Replace with your value
type: StrictStr = "example_type"
status: StrictStr = "example_status"
external: StrictBool = # Replace with your value
external:StrictBool = True
links: Optional[conlist(Link)] = None
user_response_instance = UserResponse(id=id, alternative_user_ids=alternative_user_ids, email_address=email_address, second_email_address=second_email_address, login=login, first_name=first_name, last_name=last_name, roles=roles, type=type, status=status, external=external, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

