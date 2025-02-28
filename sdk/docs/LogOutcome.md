# LogOutcome

Represents a LogOutcome resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_outcome import LogOutcome

# TODO update the JSON string below
json = "{}"
# create an instance of LogOutcome from a JSON string
log_outcome_instance = LogOutcome.from_json(json)
# print the JSON string representation of the object
print LogOutcome.to_json()

# convert the object into a dict
log_outcome_dict = log_outcome_instance.to_dict()
# create an instance of LogOutcome from a dict
log_outcome_form_dict = log_outcome.from_dict(log_outcome_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


