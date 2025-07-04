# ListUsersResponse

Users directory query response
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Uri of this response | [optional] 
**values** | [**Dict[str, UserSummary]**](UserSummary.md) | Successful entities, indexed by their id | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | Failed entities, indexed by their id | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.list_users_response import ListUsersResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

href: Optional[StrictStr] = "example_href"
values: Optional[Dict[str, UserSummary]] = # Replace with your value
failed: Optional[Dict[str, ErrorDetail]] = # Replace with your value
links: Optional[conlist(Link)] = None
list_users_response_instance = ListUsersResponse(href=href, values=values, failed=failed, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

