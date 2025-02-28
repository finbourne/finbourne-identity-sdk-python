# LogDebugContext

Represents a LogDebugContext resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debug_data** | **Dict[str, object]** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_debug_context import LogDebugContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogDebugContext from a JSON string
log_debug_context_instance = LogDebugContext.from_json(json)
# print the JSON string representation of the object
print LogDebugContext.to_json()

# convert the object into a dict
log_debug_context_dict = log_debug_context_instance.to_dict()
# create an instance of LogDebugContext from a dict
log_debug_context_form_dict = log_debug_context.from_dict(log_debug_context_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


