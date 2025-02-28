# LogActor

Represents a LogActor resource in the Okta API

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
from finbourne_identity.models.log_actor import LogActor

# TODO update the JSON string below
json = "{}"
# create an instance of LogActor from a JSON string
log_actor_instance = LogActor.from_json(json)
# print the JSON string representation of the object
print LogActor.to_json()

# convert the object into a dict
log_actor_dict = log_actor_instance.to_dict()
# create an instance of LogActor from a dict
log_actor_form_dict = log_actor.from_dict(log_actor_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


