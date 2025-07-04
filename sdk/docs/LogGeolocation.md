# LogGeolocation

Represents a LogGeolocation resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_geolocation import LogGeolocation
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, StrictFloat, StrictInt

latitude: Optional[Union[StrictFloat, StrictInt]] = None
longitude: Optional[Union[StrictFloat, StrictInt]] = None
log_geolocation_instance = LogGeolocation(latitude=latitude, longitude=longitude)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

