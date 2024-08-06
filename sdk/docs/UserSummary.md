# UserSummary

Lightweight view of an user details

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user id | [optional] 
**login** | **str** | The user login | [optional] 
**email** | **str** | The email address registered for that user | [optional] 
**second_email** | **str** |  | [optional] 
**first_name** | **str** | User&#39;s first name | [optional] 
**last_name** | **str** | User&#39;s last name | [optional] 
**type** | **str** | User&#39;s type (Personal, Service...) | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.user_summary import UserSummary

# TODO update the JSON string below
json = "{}"
# create an instance of UserSummary from a JSON string
user_summary_instance = UserSummary.from_json(json)
# print the JSON string representation of the object
print UserSummary.to_json()

# convert the object into a dict
user_summary_dict = user_summary_instance.to_dict()
# create an instance of UserSummary from a dict
user_summary_form_dict = user_summary.from_dict(user_summary_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


