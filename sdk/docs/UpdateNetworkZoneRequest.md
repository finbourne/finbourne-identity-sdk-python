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

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNetworkZoneRequest from a JSON string
update_network_zone_request_instance = UpdateNetworkZoneRequest.from_json(json)
# print the JSON string representation of the object
print UpdateNetworkZoneRequest.to_json()

# convert the object into a dict
update_network_zone_request_dict = update_network_zone_request_instance.to_dict()
# create an instance of UpdateNetworkZoneRequest from a dict
update_network_zone_request_form_dict = update_network_zone_request.from_dict(update_network_zone_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


