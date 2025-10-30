# ApiKey

The metadata of an API key
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique Id of the API key | 
**display_name** | **str** | The display name of the API key | 
**created_date** | **datetime** | The creation date of the API key | 
**deactivation_date** | **datetime** | The deactivation date of the API key | [optional] 
## Example

```python
from finbourne_identity.models.api_key import ApiKey
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
display_name: StrictStr = "example_display_name"
created_date: datetime = # Replace with your value
deactivation_date: Optional[datetime] = # Replace with your value
api_key_instance = ApiKey(id=id, display_name=display_name, created_date=created_date, deactivation_date=deactivation_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

