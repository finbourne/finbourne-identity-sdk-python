# finbourne_identity.RolesApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_to_role**](RolesApi.md#add_user_to_role) | **PUT** /api/roles/{id}/users/{userId} | AddUserToRole: Add User to Role
[**create_role**](RolesApi.md#create_role) | **POST** /api/roles | CreateRole: Create Role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /api/roles/{id} | DeleteRole: Delete Role
[**get_role**](RolesApi.md#get_role) | **GET** /api/roles/{id} | GetRole: Get Role
[**list_roles**](RolesApi.md#list_roles) | **GET** /api/roles | ListRoles: List Roles
[**list_users_in_role**](RolesApi.md#list_users_in_role) | **GET** /api/roles/{id}/users | ListUsersInRole: Get the users in the specified role.
[**remove_user_from_role**](RolesApi.md#remove_user_from_role) | **DELETE** /api/roles/{id}/users/{userId} | RemoveUserFromRole: Remove User from Role
[**update_role**](RolesApi.md#update_role) | **PUT** /api/roles/{id} | UpdateRole: Update Role


# **add_user_to_role**
> add_user_to_role(id, user_id)

AddUserToRole: Add User to Role

Adds the User to the specified Role

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    RolesApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "identityUrl":"https://<your-domain>.lusid.com/identity",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        id = 'id_example' # str | The unique identifier for the Role
        user_id = 'user_id_example' # str | The unique identifier for the User

        try:
            # AddUserToRole: Add User to Role
            await api_instance.add_user_to_role(id, user_id)        except ApiException as e:
            print("Exception when calling RolesApi->add_user_to_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the Role | 
 **user_id** | **str**| The unique identifier for the User | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_role**
> RoleResponse create_role(create_role_request)

CreateRole: Create Role

Creates a new Role

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    RolesApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "identityUrl":"https://<your-domain>.lusid.com/identity",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_role_request = CreateRoleRequest()
        # create_role_request = CreateRoleRequest.from_json("")
        create_role_request = CreateRoleRequest.from_dict({"name":"LUSID:FrontOfficeAdministrator","description":"Front office administration role"}) # CreateRoleRequest | Details of the role to be created

        try:
            # CreateRole: Create Role
            api_response = await api_instance.create_role(create_role_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->create_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_role_request** | [**CreateRoleRequest**](CreateRoleRequest.md)| Details of the role to be created | 

### Return type

[**RoleResponse**](RoleResponse.md)

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

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_role**
> delete_role(id)

DeleteRole: Delete Role

Delete the specified role

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    RolesApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "identityUrl":"https://<your-domain>.lusid.com/identity",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        id = 'id_example' # str | The unique identifier for the role

        try:
            # DeleteRole: Delete Role
            await api_instance.delete_role(id)        except ApiException as e:
            print("Exception when calling RolesApi->delete_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_role**
> RoleResponse get_role(id)

GetRole: Get Role

Get the specified role

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    RolesApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "identityUrl":"https://<your-domain>.lusid.com/identity",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        id = 'id_example' # str | The unique identifier for the role

        try:
            # GetRole: Get Role
            api_response = await api_instance.get_role(id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->get_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role | 

### Return type

[**RoleResponse**](RoleResponse.md)

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

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_roles**
> List[RoleResponse] list_roles()

ListRoles: List Roles

List the available Roles

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    RolesApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "identityUrl":"https://<your-domain>.lusid.com/identity",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)

        try:
            # ListRoles: List Roles
            api_response = await api_instance.list_roles()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->list_roles: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RoleResponse]**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the available roles |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_users_in_role**
> List[UserResponse] list_users_in_role(id)

ListUsersInRole: Get the users in the specified role.

List all Users in the specified Role

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    RolesApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "identityUrl":"https://<your-domain>.lusid.com/identity",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        id = 'id_example' # str | The unique identifier for the Role

        try:
            # ListUsersInRole: Get the users in the specified role.
            api_response = await api_instance.list_users_in_role(id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->list_users_in_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the Role | 

### Return type

[**List[UserResponse]**](UserResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The users in the role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **remove_user_from_role**
> remove_user_from_role(id, user_id)

RemoveUserFromRole: Remove User from Role

Removes the User from the specified Role

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    RolesApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "identityUrl":"https://<your-domain>.lusid.com/identity",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        id = 'id_example' # str | The unique identifier for the Role
        user_id = 'user_id_example' # str | The unique identifier for the User

        try:
            # RemoveUserFromRole: Remove User from Role
            await api_instance.remove_user_from_role(id, user_id)        except ApiException as e:
            print("Exception when calling RolesApi->remove_user_from_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the Role | 
 **user_id** | **str**| The unique identifier for the User | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_role**
> RoleResponse update_role(id, update_role_request=update_role_request)

UpdateRole: Update Role

Update the specified Role

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    RolesApi
)

async def main():

    with open("secrets.json", "w") as file:
        file.write('''
{
    "api":
    {
        "tokenUrl":"<your-token-url>",
        "identityUrl":"https://<your-domain>.lusid.com/identity",
        "username":"<your-username>",
        "password":"<your-password>",
        "clientId":"<your-client-id>",
        "clientSecret":"<your-client-secret>"
    }
}''')

    # Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        id = 'id_example' # str | The unique identifier for the role to be updated

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_role_request = UpdateRoleRequest()
        # update_role_request = UpdateRoleRequest.from_json("")
        update_role_request = UpdateRoleRequest.from_dict({"description":"Front office administration role"}) # UpdateRoleRequest | The new definition of the role (optional)

        try:
            # UpdateRole: Update Role
            api_response = await api_instance.update_role(id, update_role_request=update_role_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->update_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role to be updated | 
 **update_role_request** | [**UpdateRoleRequest**](UpdateRoleRequest.md)| The new definition of the role | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

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

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

