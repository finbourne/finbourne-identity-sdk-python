# CreateUserRequest

Details necessary for creating a new user
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The first name of the user | 
**last_name** | **str** | The last name of the user | 
**email_address** | **str** | The user&#39;s email address - to which the account validation email will be sent. For user accounts  this should exactly match the Login. | 
**second_email_address** | **str** | The user&#39;s second email address. Only allowed for Service users | [optional] 
**login** | **str** | The user&#39;s login username, in the form of an email address, which must be unique within the system.  For user accounts this should exactly match the user&#39;s email address. | 
**alternative_user_ids** | **Dict[str, str]** |  | [optional] 
**roles** | [**List[RoleId]**](RoleId.md) | Optional. Any known roles the user should be created with. | [optional] 
**type** | **str** | The type of user (e.g. Personal or Service) | 
## Example

```python
from finbourne_identity.models.create_user_request import CreateUserRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

first_name: StrictStr = "example_first_name"
last_name: StrictStr = "example_last_name"
email_address: StrictStr = "example_email_address"
second_email_address: Optional[StrictStr] = "example_second_email_address"
login: StrictStr = "example_login"
alternative_user_ids: Optional[Dict[str, StrictStr]] = # Replace with your value
roles: Optional[conlist(RoleId, max_items=20)] = Field(None, description="Optional. Any known roles the user should be created with.")
type: StrictStr = "example_type"
create_user_request_instance = CreateUserRequest(first_name=first_name, last_name=last_name, email_address=email_address, second_email_address=second_email_address, login=login, alternative_user_ids=alternative_user_ids, roles=roles, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

