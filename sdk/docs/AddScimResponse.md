# AddScimResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_url** | **str** |  | [optional] 
**api_token** | **str** |  | [optional] 
## Example

```python
from finbourne_identity.models.add_scim_response import AddScimResponse
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

base_url: Optional[StrictStr] = "example_base_url"
api_token: Optional[StrictStr] = "example_api_token"
add_scim_response_instance = AddScimResponse(base_url=base_url, api_token=api_token)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

