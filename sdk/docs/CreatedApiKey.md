# CreatedApiKey

A newly created API key
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The API Key value | 
**id** | **str** | The unique Id of the API key | 
**display_name** | **str** | The display name of the API key | 
**created_date** | **datetime** | The creation date of the API key | 
**deactivation_date** | **datetime** | The deactivation date of the API key | [optional] 
## Example

```python
from finbourne_identity.models.created_api_key import CreatedApiKey
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator
from datetime import datetime
key: StrictStr = "example_key"
id: StrictStr = "example_id"
display_name: StrictStr = "example_display_name"
created_date: datetime = # Replace with your value
deactivation_date: Optional[datetime] = # Replace with your value
created_api_key_instance = CreatedApiKey(key=key, id=id, display_name=display_name, created_date=created_date, deactivation_date=deactivation_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

