# LogIpChainEntry

Represents a LogIpChainEntry resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**geographical_context** | [**LogGeographicalContext**](LogGeographicalContext.md) |  | [optional] 
**version** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_ip_chain_entry import LogIpChainEntry

# TODO update the JSON string below
json = "{}"
# create an instance of LogIpChainEntry from a JSON string
log_ip_chain_entry_instance = LogIpChainEntry.from_json(json)
# print the JSON string representation of the object
print LogIpChainEntry.to_json()

# convert the object into a dict
log_ip_chain_entry_dict = log_ip_chain_entry_instance.to_dict()
# create an instance of LogIpChainEntry from a dict
log_ip_chain_entry_form_dict = log_ip_chain_entry.from_dict(log_ip_chain_entry_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


