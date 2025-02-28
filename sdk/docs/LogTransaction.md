# LogTransaction

Represents a LogTransaction resource in the Okta API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**detail** | **Dict[str, object]** |  | [optional] 

## Example

```python
from finbourne_identity.models.log_transaction import LogTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of LogTransaction from a JSON string
log_transaction_instance = LogTransaction.from_json(json)
# print the JSON string representation of the object
print LogTransaction.to_json()

# convert the object into a dict
log_transaction_dict = log_transaction_instance.to_dict()
# create an instance of LogTransaction from a dict
log_transaction_form_dict = log_transaction.from_dict(log_transaction_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


