# LogClientInfo

Represents a LogClientInfo resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_agent** | [**LogUserAgent**](LogUserAgent.md) |  | [optional] 
**zone** | **str** |  | [optional] 
**device** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**ip_address** | **str** |  | [optional] 
**geographical_context** | [**LogGeographicalContext**](LogGeographicalContext.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.log_client_info import LogClientInfo
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

user_agent: Optional[LogUserAgent] = # Replace with your value
zone: Optional[StrictStr] = "example_zone"
device: Optional[StrictStr] = "example_device"
id: Optional[StrictStr] = "example_id"
ip_address: Optional[StrictStr] = "example_ip_address"
geographical_context: Optional[LogGeographicalContext] = # Replace with your value
log_client_info_instance = LogClientInfo(user_agent=user_agent, zone=zone, device=device, id=id, ip_address=ip_address, geographical_context=geographical_context)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

