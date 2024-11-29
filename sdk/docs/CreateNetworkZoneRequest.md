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

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNetworkZoneRequest from a JSON string
create_network_zone_request_instance = CreateNetworkZoneRequest.from_json(json)
# print the JSON string representation of the object
print CreateNetworkZoneRequest.to_json()

# convert the object into a dict
create_network_zone_request_dict = create_network_zone_request_instance.to_dict()
# create an instance of CreateNetworkZoneRequest from a dict
create_network_zone_request_form_dict = create_network_zone_request.from_dict(create_network_zone_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


