# LogIssuer

Represents a LogIssuer resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_issuer import LogIssuer

# TODO update the JSON string below
json = "{}"
# create an instance of LogIssuer from a JSON string
log_issuer_instance = LogIssuer.from_json(json)
# print the JSON string representation of the object
print LogIssuer.to_json()

# convert the object into a dict
log_issuer_dict = log_issuer_instance.to_dict()
# create an instance of LogIssuer from a dict
log_issuer_form_dict = log_issuer.from_dict(log_issuer_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


