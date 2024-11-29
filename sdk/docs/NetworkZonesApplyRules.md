# NetworkZonesApplyRules


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_type** | **List[str]** |  | 
**user_roles** | **List[str]** |  | 

## Example

```python
from finbourne_identity.models.network_zones_apply_rules import NetworkZonesApplyRules

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkZonesApplyRules from a JSON string
network_zones_apply_rules_instance = NetworkZonesApplyRules.from_json(json)
# print the JSON string representation of the object
print NetworkZonesApplyRules.to_json()

# convert the object into a dict
network_zones_apply_rules_dict = network_zones_apply_rules_instance.to_dict()
# create an instance of NetworkZonesApplyRules from a dict
network_zones_apply_rules_form_dict = network_zones_apply_rules.from_dict(network_zones_apply_rules_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


