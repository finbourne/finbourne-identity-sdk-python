# LogGeographicalContext

Represents a LogGeographicalContext resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**geolocation** | [**LogGeolocation**](LogGeolocation.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.log_geographical_context import LogGeographicalContext

# TODO update the JSON string below
json = "{}"
# create an instance of LogGeographicalContext from a JSON string
log_geographical_context_instance = LogGeographicalContext.from_json(json)
# print the JSON string representation of the object
print LogGeographicalContext.to_json()

# convert the object into a dict
log_geographical_context_dict = log_geographical_context_instance.to_dict()
# create an instance of LogGeographicalContext from a dict
log_geographical_context_form_dict = log_geographical_context.from_dict(log_geographical_context_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


