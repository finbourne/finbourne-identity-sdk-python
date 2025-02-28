# LogSeverity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_severity import LogSeverity

# TODO update the JSON string below
json = "{}"
# create an instance of LogSeverity from a JSON string
log_severity_instance = LogSeverity.from_json(json)
# print the JSON string representation of the object
print LogSeverity.to_json()

# convert the object into a dict
log_severity_dict = log_severity_instance.to_dict()
# create an instance of LogSeverity from a dict
log_severity_form_dict = log_severity.from_dict(log_severity_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


