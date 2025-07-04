# LogGeographicalContext

Represents a LogGeographicalContext resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**geolocation** | [**LogGeolocation**](LogGeolocation.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.log_geographical_context import LogGeographicalContext
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

city: Optional[StrictStr] = "example_city"
state: Optional[StrictStr] = "example_state"
country: Optional[StrictStr] = "example_country"
postal_code: Optional[StrictStr] = "example_postal_code"
geolocation: Optional[LogGeolocation] = None
log_geographical_context_instance = LogGeographicalContext(city=city, state=state, country=country, postal_code=postal_code, geolocation=geolocation)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

