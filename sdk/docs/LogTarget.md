# LogTarget

Represents a LogTarget resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**alternate_id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**detail_entry** | **Dict[str, object]** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_target import LogTarget

# TODO update the JSON string below
json = "{}"
# create an instance of LogTarget from a JSON string
log_target_instance = LogTarget.from_json(json)
# print the JSON string representation of the object
print LogTarget.to_json()

# convert the object into a dict
log_target_dict = log_target_instance.to_dict()
# create an instance of LogTarget from a dict
log_target_form_dict = log_target.from_dict(log_target_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


