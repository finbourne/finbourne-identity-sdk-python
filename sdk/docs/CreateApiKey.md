# CreateApiKey

Create an API key
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name for the API key | 
**deactivation_date** | **datetime** | The optional date at which the key should deactivate | [optional] 
## Example

```python
from finbourne_identity.models.create_api_key import CreateApiKey
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
deactivation_date: Optional[datetime] = # Replace with your value
create_api_key_instance = CreateApiKey(display_name=display_name, deactivation_date=deactivation_date)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

