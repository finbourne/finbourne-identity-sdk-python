# LogRequest

Represents a LogRequest resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_chain** | [**List[LogIpChainEntry]**](LogIpChainEntry.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.log_request import LogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LogRequest from a JSON string
log_request_instance = LogRequest.from_json(json)
# print the JSON string representation of the object
print LogRequest.to_json()

# convert the object into a dict
log_request_dict = log_request_instance.to_dict()
# create an instance of LogRequest from a dict
log_request_form_dict = log_request.from_dict(log_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


