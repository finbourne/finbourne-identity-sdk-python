# UserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user&#39;s system supplied unique identifier | 
**alternative_user_ids** | **Dict[str, str]** | The user&#39;s alternative IDs | [optional] 
**email_address** | **str** | The user&#39;s emailAddress address, which must be unique within the system | 
**second_email_address** | **str** | The user&#39;s second email address. Only allowed for service users. | [optional] 
**login** | **str** |  | 
**first_name** | **str** | The user&#39;s first name | 
**last_name** | **str** | The user&#39;s last name | 
**roles** | [**List[RoleResponse]**](RoleResponse.md) | The roles that the user has. | [optional] 
**type** | **str** | The type of user (e.g. Personal or Service) | 
**status** | **str** | The status of the user | 
**external** | **bool** | Whether or not the user originates from an external identity system | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print UserResponse.to_json()

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_form_dict = user_response.from_dict(user_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


