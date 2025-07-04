# UpdateUserRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email_address** | **str** |  | 
**second_email_address** | **str** |  | [optional] 
**login** | **str** | The user&#39;s login username, in the form of an email address, which must be unique within the system.  For user accounts this should exactly match the user&#39;s email address. | 
**alternative_user_ids** | **Dict[str, str]** |  | [optional] 
**roles** | [**List[RoleId]**](RoleId.md) | Deprecated. To update a user&#39;s roles use the AddUserToRole and RemoveUserFromRole endpoints | [optional] 
## Example

```python
from finbourne_identity.models.update_user_request import UpdateUserRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

first_name: StrictStr = "example_first_name"
last_name: StrictStr = "example_last_name"
email_address: StrictStr = "example_email_address"
second_email_address: Optional[StrictStr] = "example_second_email_address"
login: StrictStr = "example_login"
alternative_user_ids: Optional[Dict[str, StrictStr]] = # Replace with your value
roles: Optional[conlist(RoleId)] = # Replace with your value
update_user_request_instance = UpdateUserRequest(first_name=first_name, last_name=last_name, email_address=email_address, second_email_address=second_email_address, login=login, alternative_user_ids=alternative_user_ids, roles=roles)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

