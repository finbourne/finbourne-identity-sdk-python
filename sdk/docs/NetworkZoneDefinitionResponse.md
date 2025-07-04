# NetworkZoneDefinitionResponse

The Client facing representation of a NetworkZone
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The Network Zone Code | [optional] 
**hierarchy** | **int** | Hierarchy of the Network Zone | [optional] 
**description** | **str** | The Description of the Network Zone | [optional] 
**created_at** | **datetime** | Network Zone Creation timestamp | [optional] 
**updated_at** | **datetime** | Timestamp of the last update | [optional] 
**network_zone_ips** | [**List[IpAddressDefinition]**](IpAddressDefinition.md) | Network zone IP information (IPs and CIDR ranges) | [optional] 
**action** | **str** | Kind of action to apply when a request matches this Network Zone (Block/Allow/NoOp) | [optional] 
**apply_rules** | [**NetworkZonesApplyRules**](NetworkZonesApplyRules.md) |  | [optional] 
**created_by** | **str** | User Id that created the Network Zone | [optional] 
**updated_by** | **str** | User Id of the last update on the Network Zone | [optional] 
## Example

```python
from finbourne_identity.models.network_zone_definition_response import NetworkZoneDefinitionResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist
from datetime import datetime
code: Optional[StrictStr] = "example_code"
hierarchy: Optional[StrictInt] = # Replace with your value
hierarchy: Optional[StrictInt] = None
description: Optional[StrictStr] = "example_description"
created_at: Optional[datetime] = # Replace with your value
updated_at: Optional[datetime] = # Replace with your value
network_zone_ips: Optional[conlist(IpAddressDefinition)] = # Replace with your value
action: Optional[StrictStr] = "example_action"
apply_rules: Optional[NetworkZonesApplyRules] = # Replace with your value
created_by: Optional[StrictStr] = "example_created_by"
updated_by: Optional[StrictStr] = "example_updated_by"
network_zone_definition_response_instance = NetworkZoneDefinitionResponse(code=code, hierarchy=hierarchy, description=description, created_at=created_at, updated_at=updated_at, network_zone_ips=network_zone_ips, action=action, apply_rules=apply_rules, created_by=created_by, updated_by=updated_by)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

