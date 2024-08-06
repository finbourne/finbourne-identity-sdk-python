# ListUsersResponse

Users directory query response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | Uri of this response | [optional] 
**values** | [**Dict[str, UserSummary]**](UserSummary.md) | Successful entities, indexed by their id | [optional] 
**failed** | [**Dict[str, ErrorDetail]**](ErrorDetail.md) | Failed entities, indexed by their id | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.list_users_response import ListUsersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsersResponse from a JSON string
list_users_response_instance = ListUsersResponse.from_json(json)
# print the JSON string representation of the object
print ListUsersResponse.to_json()

# convert the object into a dict
list_users_response_dict = list_users_response_instance.to_dict()
# create an instance of ListUsersResponse from a dict
list_users_response_form_dict = list_users_response.from_dict(list_users_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


