# CreateNetworkZoneRequest

The Create Network Zone Request information
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**description** | **str** |  | [optional] 
**network_zone_ips** | [**List[IpAddressDefinition]**](IpAddressDefinition.md) |  | 
**action** | **str** |  | [optional] 
**apply_rules** | [**NetworkZonesApplyRules**](NetworkZonesApplyRules.md) |  | 
## Example

```python
from finbourne_identity.models.create_network_zone_request import CreateNetworkZoneRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: StrictStr = "example_code"
description: Optional[StrictStr] = "example_description"
network_zone_ips: List[IpAddressDefinition] = # Replace with your value
action: Optional[StrictStr] = "example_action"
apply_rules: NetworkZonesApplyRules = # Replace with your value
create_network_zone_request_instance = CreateNetworkZoneRequest(code=code, description=description, network_zone_ips=network_zone_ips, action=action, apply_rules=apply_rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

