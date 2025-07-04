# UpdateNetworkZoneRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**network_zone_ips** | [**List[IpAddressDefinition]**](IpAddressDefinition.md) |  | 
**action** | **str** |  | [optional] 
**apply_rules** | [**NetworkZonesApplyRules**](NetworkZonesApplyRules.md) |  | 
**hierarchy** | **int** |  | 
## Example

```python
from finbourne_identity.models.update_network_zone_request import UpdateNetworkZoneRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist

description: Optional[StrictStr] = "example_description"
network_zone_ips: conlist(IpAddressDefinition) = # Replace with your value
action: Optional[StrictStr] = "example_action"
apply_rules: NetworkZonesApplyRules = # Replace with your value
hierarchy: StrictInt = # Replace with your value
hierarchy: StrictInt = 42
update_network_zone_request_instance = UpdateNetworkZoneRequest(description=description, network_zone_ips=network_zone_ips, action=action, apply_rules=apply_rules, hierarchy=hierarchy)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

