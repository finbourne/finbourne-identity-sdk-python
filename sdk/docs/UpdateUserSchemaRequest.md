# UpdateUserSchemaRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternative_user_ids** | [**List[UserSchemaProperty]**](UserSchemaProperty.md) |  | 
## Example

```python
from finbourne_identity.models.update_user_schema_request import UpdateUserSchemaRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

alternative_user_ids: conlist(UserSchemaProperty, max_items=10) = Field(..., alias="alternativeUserIds")
update_user_schema_request_instance = UpdateUserSchemaRequest(alternative_user_ids=alternative_user_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

