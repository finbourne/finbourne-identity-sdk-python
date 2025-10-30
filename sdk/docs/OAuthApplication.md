# OAuthApplication

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | **str** |  | 
**display_name** | **str** |  | 
**secret** | **str** |  | [optional] 
**client_id** | **str** |  | 
**issuer** | **str** |  | 
## Example

```python
from finbourne_identity.models.o_auth_application import OAuthApplication
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: StrictStr = "example_id"
type: StrictStr = "example_type"
display_name: StrictStr = "example_display_name"
secret: Optional[StrictStr] = "example_secret"
client_id: StrictStr = "example_client_id"
issuer: StrictStr = "example_issuer"
o_auth_application_instance = OAuthApplication(id=id, type=type, display_name=display_name, secret=secret, client_id=client_id, issuer=issuer)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

