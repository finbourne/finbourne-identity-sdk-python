# CreateApplicationRequest

A request to create an application for authenticating the source of token requests

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The Display Name of the application | 
**client_id** | **str** | The OpenID Connect ClientId of the application | 
**type** | **str** | The Type of the application. This must be either Native or Web | 
**redirect_uris** | **List[str]** | A web application&#39;s acceptable list of post-login redirect URIs | [optional] 
**post_logout_redirect_uris** | **List[str]** | A web application&#39;s acceptable list of post-logout redirect URIs | [optional] 

## Example

```python
from finbourne_identity.models.create_application_request import CreateApplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApplicationRequest from a JSON string
create_application_request_instance = CreateApplicationRequest.from_json(json)
# print the JSON string representation of the object
print CreateApplicationRequest.to_json()

# convert the object into a dict
create_application_request_dict = create_application_request_instance.to_dict()
# create an instance of CreateApplicationRequest from a dict
create_application_request_form_dict = create_application_request.from_dict(create_application_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


