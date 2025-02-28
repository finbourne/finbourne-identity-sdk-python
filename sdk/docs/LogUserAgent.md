# LogUserAgent

Represents a LogUserAgent resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_user_agent** | **str** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**browser** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_user_agent import LogUserAgent

# TODO update the JSON string below
json = "{}"
# create an instance of LogUserAgent from a JSON string
log_user_agent_instance = LogUserAgent.from_json(json)
# print the JSON string representation of the object
print LogUserAgent.to_json()

# convert the object into a dict
log_user_agent_dict = log_user_agent_instance.to_dict()
# create an instance of LogUserAgent from a dict
log_user_agent_form_dict = log_user_agent.from_dict(log_user_agent_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


