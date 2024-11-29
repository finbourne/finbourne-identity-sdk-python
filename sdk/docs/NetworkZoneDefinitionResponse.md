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

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZoneDefinitionResponse from a JSON string
network_zone_definition_response_instance = NetworkZoneDefinitionResponse.from_json(json)
# print the JSON string representation of the object
print NetworkZoneDefinitionResponse.to_json()

# convert the object into a dict
network_zone_definition_response_dict = network_zone_definition_response_instance.to_dict()
# create an instance of NetworkZoneDefinitionResponse from a dict
network_zone_definition_response_form_dict = network_zone_definition_response.from_dict(network_zone_definition_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


