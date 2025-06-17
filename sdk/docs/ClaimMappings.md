# ClaimMappings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**email** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**user_type** | **str** |  | 
**groups** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.claim_mappings import ClaimMappings

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimMappings from a JSON string
claim_mappings_instance = ClaimMappings.from_json(json)
# print the JSON string representation of the object
print ClaimMappings.to_json()

# convert the object into a dict
claim_mappings_dict = claim_mappings_instance.to_dict()
# create an instance of ClaimMappings from a dict
claim_mappings_form_dict = claim_mappings.from_dict(claim_mappings_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


