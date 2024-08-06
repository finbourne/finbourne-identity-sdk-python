# CurrentUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user&#39;s system supplied unique identifier | 
**email_address** | **str** | The user&#39;s email address which may be null depending on the authentication method | 
**type** | **str** | The type of user (e.g. Personal or Service) | 
**domain_type** | **str** | The type of domain in which the user exists | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_identity.models.current_user_response import CurrentUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentUserResponse from a JSON string
current_user_response_instance = CurrentUserResponse.from_json(json)
# print the JSON string representation of the object
print CurrentUserResponse.to_json()

# convert the object into a dict
current_user_response_dict = current_user_response_instance.to_dict()
# create an instance of CurrentUserResponse from a dict
current_user_response_form_dict = current_user_response.from_dict(current_user_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


