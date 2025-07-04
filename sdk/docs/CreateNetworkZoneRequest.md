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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

code: StrictStr = "example_code"
description: Optional[StrictStr] = "example_description"
network_zone_ips: conlist(IpAddressDefinition) = # Replace with your value
action: Optional[StrictStr] = "example_action"
apply_rules: NetworkZonesApplyRules = # Replace with your value
create_network_zone_request_instance = CreateNetworkZoneRequest(code=code, description=description, network_zone_ips=network_zone_ips, action=action, apply_rules=apply_rules)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

