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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

id: StrictStr = "example_id"
type: StrictStr = "example_type"
display_name: StrictStr = "example_display_name"
secret: Optional[StrictStr] = "example_secret"
client_id: StrictStr = "example_client_id"
issuer: StrictStr = "example_issuer"
o_auth_application_instance = OAuthApplication(id=id, type=type, display_name=display_name, secret=secret, client_id=client_id, issuer=issuer)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

