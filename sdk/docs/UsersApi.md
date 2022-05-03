# finbourne_identity.UsersApi

All URIs are relative to *https://fbn-ci.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /api/users | [EARLY ACCESS] CreateUser: Create User
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /api/users/{id} | [EARLY ACCESS] DeleteUser: Delete User
[**expire_password**](UsersApi.md#expire_password) | **POST** /api/users/{id}/lifecycle/$expirepassword | [BETA] ExpirePassword: Reset the user&#39;s password to a temporary one
[**find_users_by_id**](UsersApi.md#find_users_by_id) | **GET** /api/directory | [EARLY ACCESS] FindUsersById: Find users by id endpoint
[**get_user**](UsersApi.md#get_user) | **GET** /api/users/{id} | [EARLY ACCESS] GetUser: Get User
[**list_users**](UsersApi.md#list_users) | **GET** /api/users | [EARLY ACCESS] ListUsers: List Users
[**reset_factors**](UsersApi.md#reset_factors) | **POST** /api/users/{id}/lifecycle/$resetfactors | [BETA] ResetFactors: Reset MFA factors
[**reset_password**](UsersApi.md#reset_password) | **POST** /api/users/{id}/lifecycle/$resetpassword | [BETA] ResetPassword: Reset Password
[**send_activation_email**](UsersApi.md#send_activation_email) | **POST** /api/users/{id}/lifecycle/$activate | [BETA] SendActivationEmail: Sends an activation email to the User
[**unlock_user**](UsersApi.md#unlock_user) | **POST** /api/users/{id}/lifecycle/$unlock | [BETA] UnlockUser: Unlock User
[**update_user**](UsersApi.md#update_user) | **PUT** /api/users/{id} | [EARLY ACCESS] UpdateUser: Update User


# **create_user**
> UserResponse create_user(create_user_request, wait_for_reindex=wait_for_reindex)

[EARLY ACCESS] CreateUser: Create User

Create a new User

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
    api_instance = finbourne_identity.UsersApi(api_client)
    create_user_request = {"firstName":"Joe","lastName":"Bloggs","emailAddress":"joe.bloggs@myco.com","login":"joe.bloggs@myco.com","type":"Personal"} # CreateUserRequest | Details of the User to be created
wait_for_reindex = False # bool | Should the request wait until the newly created User is indexed (available in List) before returning (optional) (default to False)

    try:
        # [EARLY ACCESS] CreateUser: Create User
        api_response = api_instance.create_user(create_user_request, wait_for_reindex=wait_for_reindex)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)| Details of the User to be created | 
 **wait_for_reindex** | **bool**| Should the request wait until the newly created User is indexed (available in List) before returning | [optional] [default to False]

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a new user |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(id, purge=purge)

[EARLY ACCESS] DeleteUser: Delete User

By default the user will be de-provisioned and inactive, however their record will remain in the identity  provider for audit purposes. If this is not desirable and removal of all trace of the user is required,  the purge parameter can be specified to indicate the details should be purged completely.

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
    api_instance = finbourne_identity.UsersApi(api_client)
    id = 'id_example' # str | The unique identifier for the user
purge = True # bool | Whether to purge any trace of the user from the identity provider (will affect audit) (optional)

    try:
        # [EARLY ACCESS] DeleteUser: Delete User
        api_instance.delete_user(id, purge=purge)
    except ApiException as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the user | 
 **purge** | **bool**| Whether to purge any trace of the user from the identity provider (will affect audit) | [optional] 

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

# **expire_password**
> TemporaryPassword expire_password(id)

[BETA] ExpirePassword: Reset the user's password to a temporary one

Resets the user's password to a temporary one which is then expired

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
    api_instance = finbourne_identity.UsersApi(api_client)
    id = 'id_example' # str | The unique identifier for the User having its password reset

    try:
        # [BETA] ExpirePassword: Reset the user's password to a temporary one
        api_response = api_instance.expire_password(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->expire_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User having its password reset | 

### Return type

[**TemporaryPassword**](TemporaryPassword.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reset the user&#39;s password |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_users_by_id**
> ListUsersResponse find_users_by_id(id)

[EARLY ACCESS] FindUsersById: Find users by id endpoint

Finds a maximum of 50 users by ID

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
    api_instance = finbourne_identity.UsersApi(api_client)
    id = ['id_example'] # list[str] | A list of unique identifiers for the users

    try:
        # [EARLY ACCESS] FindUsersById: Find users by id endpoint
        api_response = api_instance.find_users_by_id(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->find_users_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[str]**](str.md)| A list of unique identifiers for the users | 

### Return type

[**ListUsersResponse**](ListUsersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user(id, include_roles=include_roles)

[EARLY ACCESS] GetUser: Get User

Get the specified User

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
    api_instance = finbourne_identity.UsersApi(api_client)
    id = 'id_example' # str | The unique identifier for the User
include_roles = True # bool | Flag indicating that the users roles should be included in the response (optional)

    try:
        # [EARLY ACCESS] GetUser: Get User
        api_response = api_instance.get_user(id, include_roles=include_roles)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User | 
 **include_roles** | **bool**| Flag indicating that the users roles should be included in the response | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the specified user |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> list[UserResponse] list_users(include_roles=include_roles, include_deactivated=include_deactivated)

[EARLY ACCESS] ListUsers: List Users

List the available Users

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
    api_instance = finbourne_identity.UsersApi(api_client)
    include_roles = False # bool | Flag indicating that the users roles should be included in the response (optional) (default to False)
include_deactivated = False # bool | Include previously deleted (not purged) users (optional) (default to False)

    try:
        # [EARLY ACCESS] ListUsers: List Users
        api_response = api_instance.list_users(include_roles=include_roles, include_deactivated=include_deactivated)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_roles** | **bool**| Flag indicating that the users roles should be included in the response | [optional] [default to False]
 **include_deactivated** | **bool**| Include previously deleted (not purged) users | [optional] [default to False]

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
**200** | List the available users |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_factors**
> reset_factors(id)

[BETA] ResetFactors: Reset MFA factors

Resets the MFA factors of the specified User

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
    api_instance = finbourne_identity.UsersApi(api_client)
    id = 'id_example' # str | The unique identifier for the User having their MFA factors reset

    try:
        # [BETA] ResetFactors: Reset MFA factors
        api_instance.reset_factors(id)
    except ApiException as e:
        print("Exception when calling UsersApi->reset_factors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User having their MFA factors reset | 

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

# **reset_password**
> reset_password(id)

[BETA] ResetPassword: Reset Password

Resets the password of the specified User

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
    api_instance = finbourne_identity.UsersApi(api_client)
    id = 'id_example' # str | The unique identifier for the User having their password reset

    try:
        # [BETA] ResetPassword: Reset Password
        api_instance.reset_password(id)
    except ApiException as e:
        print("Exception when calling UsersApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User having their password reset | 

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

# **send_activation_email**
> send_activation_email(id)

[BETA] SendActivationEmail: Sends an activation email to the User

Sends an activation email to the specified User

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
    api_instance = finbourne_identity.UsersApi(api_client)
    id = 'id_example' # str | The unique identifier for the User to be activated

    try:
        # [BETA] SendActivationEmail: Sends an activation email to the User
        api_instance.send_activation_email(id)
    except ApiException as e:
        print("Exception when calling UsersApi->send_activation_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User to be activated | 

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

# **unlock_user**
> unlock_user(id)

[BETA] UnlockUser: Unlock User

Unlocks the specified User

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
    api_instance = finbourne_identity.UsersApi(api_client)
    id = 'id_example' # str | The unique identifier for the User to be unlocked

    try:
        # [BETA] UnlockUser: Unlock User
        api_instance.unlock_user(id)
    except ApiException as e:
        print("Exception when calling UsersApi->unlock_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User to be unlocked | 

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

# **update_user**
> UserResponse update_user(id, update_user_request)

[EARLY ACCESS] UpdateUser: Update User

Updates the specified User

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
    api_instance = finbourne_identity.UsersApi(api_client)
    id = 'id_example' # str | The unique identifier for the User to be updated
update_user_request = {"firstName":"Joe","lastName":"Bloggs","emailAddress":"joe.bloggs@myco.com","login":"joe.bloggs@myco.com"} # UpdateUserRequest | The new definition of the User

    try:
        # [EARLY ACCESS] UpdateUser: Update User
        api_response = api_instance.update_user(id, update_user_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the User to be updated | 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)| The new definition of the User | 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a user |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

