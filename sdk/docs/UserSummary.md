# UserSummary

Lightweight view of an user details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user id | [optional] 
**login** | **str** | The user login | [optional] 
**email** | **str** | The email address registered for that user | [optional] 
**second_email** | **str** |  | [optional] 
**first_name** | **str** | User&#39;s first name | [optional] 
**last_name** | **str** | User&#39;s last name | [optional] 
**type** | **str** | User&#39;s type (Personal, Service...) | [optional] 
**alternative_user_ids** | **Dict[str, Optional[str]]** | User&#39;s alternative user IDs. Only returned for the current user | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.user_summary import UserSummary
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Optional[StrictStr] = "example_id"
login: Optional[StrictStr] = "example_login"
email: Optional[StrictStr] = "example_email"
second_email: Optional[StrictStr] = "example_second_email"
first_name: Optional[StrictStr] = "example_first_name"
last_name: Optional[StrictStr] = "example_last_name"
type: Optional[StrictStr] = "example_type"
alternative_user_ids: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
links: Optional[List[Link]] = None
user_summary_instance = UserSummary(id=id, login=login, email=email, second_email=second_email, first_name=first_name, last_name=last_name, type=type, alternative_user_ids=alternative_user_ids, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

