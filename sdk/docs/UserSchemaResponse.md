# UserSchemaResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternative_user_ids** | [**List[UserSchemaProperty]**](UserSchemaProperty.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.user_schema_response import UserSchemaResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

alternative_user_ids: Optional[conlist(UserSchemaProperty)] = # Replace with your value
user_schema_response_instance = UserSchemaResponse(alternative_user_ids=alternative_user_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

