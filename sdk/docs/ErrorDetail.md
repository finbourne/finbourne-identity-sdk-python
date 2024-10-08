# ErrorDetail

Provides details about an entity error that occured

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the entity this error relates to | [optional] 
**type** | **str** | Error type | [optional] 
**detail** | **str** | Human readable description of the error | [optional] 

## Example

```python
from finbourne_identity.models.error_detail import ErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetail from a JSON string
error_detail_instance = ErrorDetail.from_json(json)
# print the JSON string representation of the object
print ErrorDetail.to_json()

# convert the object into a dict
error_detail_dict = error_detail_instance.to_dict()
# create an instance of ErrorDetail from a dict
error_detail_form_dict = error_detail.from_dict(error_detail_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


