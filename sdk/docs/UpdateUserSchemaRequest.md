# UpdateUserSchemaRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alternative_user_ids** | [**List[UserSchemaProperty]**](UserSchemaProperty.md) |  | 
## Example

```python
from finbourne_identity.models.update_user_schema_request import UpdateUserSchemaRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

alternative_user_ids: List[UserSchemaProperty] = # Replace with your value
update_user_schema_request_instance = UpdateUserSchemaRequest(alternative_user_ids=alternative_user_ids)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

