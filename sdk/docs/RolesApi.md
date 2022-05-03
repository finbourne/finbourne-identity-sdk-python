# finbourne_identity.RolesApi

All URIs are relative to *https://fbn-ci.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_role**](RolesApi.md#add_user_to_role) | **PUT** /api/roles/{id}/users/{userId} | [EARLY ACCESS] AddUserToRole: Add User to Role
[**create_role**](RolesApi.md#create_role) | **POST** /api/roles | [EARLY ACCESS] CreateRole: Create Role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /api/roles/{id} | [EARLY ACCESS] DeleteRole: Delete Role
[**get_role**](RolesApi.md#get_role) | **GET** /api/roles/{id} | [EARLY ACCESS] GetRole: Get Role
[**list_roles**](RolesApi.md#list_roles) | **GET** /api/roles | [EARLY ACCESS] ListRoles: List Roles
[**list_users_in_role**](RolesApi.md#list_users_in_role) | **GET** /api/roles/{id}/users | [EARLY ACCESS] ListUsersInRole: Get the users in the specified role.
[**remove_user_from_role**](RolesApi.md#remove_user_from_role) | **DELETE** /api/roles/{id}/users/{userId} | [EARLY ACCESS] RemoveUserFromRole: Remove User from Role
[**update_role**](RolesApi.md#update_role) | **PUT** /api/roles/{id} | [EARLY ACCESS] UpdateRole: Update Role


# **add_user_to_role**
> add_user_to_role(id, user_id)

[EARLY ACCESS] AddUserToRole: Add User to Role

Adds the User to the specified Role

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier for the Role
user_id = 'user_id_example' # str | The unique identifier for the User

    try:
        # [EARLY ACCESS] AddUserToRole: Add User to Role
        api_instance.add_user_to_role(id, user_id)
    except ApiException as e:
        print("Exception when calling RolesApi->add_user_to_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the Role | 
 **user_id** | **str**| The unique identifier for the User | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> RoleResponse create_role(create_role_request)

[EARLY ACCESS] CreateRole: Create Role

Creates a new Role

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.RolesApi(api_client)
    create_role_request = {"name":"LUSID:FrontOfficeAdministrator","description":"Front office administration role"} # CreateRoleRequest | Details of the role to be created

    try:
        # [EARLY ACCESS] CreateRole: Create Role
        api_response = api_instance.create_role(create_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_role_request** | [**CreateRoleRequest**](CreateRoleRequest.md)| Details of the role to be created | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a new role |  -  |
**409** | A role with the same Name already exists. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(id)

[EARLY ACCESS] DeleteRole: Delete Role

Delete the specified role

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier for the role

    try:
        # [EARLY ACCESS] DeleteRole: Delete Role
        api_instance.delete_role(id)
    except ApiException as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleResponse get_role(id)

[EARLY ACCESS] GetRole: Get Role

Get the specified role

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier for the role

    try:
        # [EARLY ACCESS] GetRole: Get Role
        api_response = api_instance.get_role(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the specified role |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> list[RoleResponse] list_roles()

[EARLY ACCESS] ListRoles: List Roles

List the available Roles

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.RolesApi(api_client)
    
    try:
        # [EARLY ACCESS] ListRoles: List Roles
        api_response = api_instance.list_roles()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RoleResponse]**](RoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the available roles |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_in_role**
> list[UserResponse] list_users_in_role(id)

[EARLY ACCESS] ListUsersInRole: Get the users in the specified role.

List all Users in the specified Role

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier for the Role

    try:
        # [EARLY ACCESS] ListUsersInRole: Get the users in the specified role.
        api_response = api_instance.list_users_in_role(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_users_in_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the Role | 

### Return type

[**list[UserResponse]**](UserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The users in the role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_role**
> remove_user_from_role(id, user_id)

[EARLY ACCESS] RemoveUserFromRole: Remove User from Role

Removes the User from the specified Role

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier for the Role
user_id = 'user_id_example' # str | The unique identifier for the User

    try:
        # [EARLY ACCESS] RemoveUserFromRole: Remove User from Role
        api_instance.remove_user_from_role(id, user_id)
    except ApiException as e:
        print("Exception when calling RolesApi->remove_user_from_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the Role | 
 **user_id** | **str**| The unique identifier for the User | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> RoleResponse update_role(id, update_role_request=update_role_request)

[EARLY ACCESS] UpdateRole: Update Role

Update the specified Role

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.RolesApi(api_client)
    id = 'id_example' # str | The unique identifier for the role to be updated
update_role_request = {"description":"Front office administration role"} # UpdateRoleRequest | The new definition of the role (optional)

    try:
        # [EARLY ACCESS] UpdateRole: Update Role
        api_response = api_instance.update_role(id, update_role_request=update_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role to be updated | 
 **update_role_request** | [**UpdateRoleRequest**](UpdateRoleRequest.md)| The new definition of the role | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a role |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

