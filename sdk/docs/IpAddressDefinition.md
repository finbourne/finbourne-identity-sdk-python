# IpAddressDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**value** | **str** |  | 

## Example

```python
from finbourne_identity.models.ip_address_definition import IpAddressDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of IpAddressDefinition from a JSON string
ip_address_definition_instance = IpAddressDefinition.from_json(json)
# print the JSON string representation of the object
print IpAddressDefinition.to_json()

# convert the object into a dict
ip_address_definition_dict = ip_address_definition_instance.to_dict()
# create an instance of IpAddressDefinition from a dict
ip_address_definition_form_dict = ip_address_definition.from_dict(ip_address_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


