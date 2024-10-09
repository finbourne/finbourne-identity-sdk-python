# finbourne_identity.AuthenticationApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authentication_information**](AuthenticationApi.md#get_authentication_information) | **GET** /api/authentication/information | GetAuthenticationInformation: Gets AuthenticationInformation
[**get_password_policy**](AuthenticationApi.md#get_password_policy) | **GET** /api/authentication/password-policy/{userType} | [EXPERIMENTAL] GetPasswordPolicy: Gets password policy for a user type
[**get_support_access_history**](AuthenticationApi.md#get_support_access_history) | **GET** /api/authentication/support | GetSupportAccessHistory: Get the history of all support access granted and any information pertaining to their termination
[**get_support_roles**](AuthenticationApi.md#get_support_roles) | **GET** /api/authentication/support-roles | GetSupportRoles: Get mapping of support roles, the internal representation to a human friendly representation
[**grant_support_access**](AuthenticationApi.md#grant_support_access) | **POST** /api/authentication/support | GrantSupportAccess: Grants FINBOURNE support access to your account
[**invalidate_support_access**](AuthenticationApi.md#invalidate_support_access) | **DELETE** /api/authentication/support | InvalidateSupportAccess: Revoke any FINBOURNE support access to your account
[**update_password_policy**](AuthenticationApi.md#update_password_policy) | **PUT** /api/authentication/password-policy/{userType} | [EXPERIMENTAL] UpdatePasswordPolicy: Updates password policy for a user type


# **get_authentication_information**
> AuthenticationInformation get_authentication_information()

GetAuthenticationInformation: Gets AuthenticationInformation

Get the AuthenticationInformation associated with the current domain. This includes all the  necessary information to login to this domain.

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    AuthenticationApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(AuthenticationApi)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_authentication_information(opts=opts)

            # GetAuthenticationInformation: Gets AuthenticationInformation
            api_response = await api_instance.get_authentication_information()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuthenticationApi->get_authentication_information: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationInformation**](AuthenticationInformation.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get authentication information |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_password_policy**
> PasswordPolicyResponse get_password_policy(user_type)

[EXPERIMENTAL] GetPasswordPolicy: Gets password policy for a user type

Get the password policy for a given user type

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    AuthenticationApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(AuthenticationApi)
        user_type = 'user_type_example' # str | The type of user (should only be personal or service)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_password_policy(user_type, opts=opts)

            # [EXPERIMENTAL] GetPasswordPolicy: Gets password policy for a user type
            api_response = await api_instance.get_password_policy(user_type)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuthenticationApi->get_password_policy: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_type** | **str**| The type of user (should only be personal or service) | 

### Return type

[**PasswordPolicyResponse**](PasswordPolicyResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get password policy |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_support_access_history**
> List[SupportAccessResponse] get_support_access_history(start=start, end=end)

GetSupportAccessHistory: Get the history of all support access granted and any information pertaining to their termination

The active and inactive support requests will be returned, inactive support requests will have information pertaining to their termination  including obfuscated userIds of those who created and terminated the request

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    AuthenticationApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(AuthenticationApi)
        start = '2013-10-20T19:20:30+01:00' # datetime | The start expiry date to query support access requests from (optional)
        end = '2013-10-20T19:20:30+01:00' # datetime | The end expiry date to query support access requests to (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_support_access_history(start=start, end=end, opts=opts)

            # GetSupportAccessHistory: Get the history of all support access granted and any information pertaining to their termination
            api_response = await api_instance.get_support_access_history(start=start, end=end)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuthenticationApi->get_support_access_history: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **datetime**| The start expiry date to query support access requests from | [optional] 
 **end** | **datetime**| The end expiry date to query support access requests to | [optional] 

### Return type

[**List[SupportAccessResponse]**](SupportAccessResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get support access history |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_support_roles**
> SupportRolesResponse get_support_roles()

GetSupportRoles: Get mapping of support roles, the internal representation to a human friendly representation

Get mapping of support roles, the internal representation to a human friendly representation

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    AuthenticationApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(AuthenticationApi)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_support_roles(opts=opts)

            # GetSupportRoles: Get mapping of support roles, the internal representation to a human friendly representation
            api_response = await api_instance.get_support_roles()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuthenticationApi->get_support_roles: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportRolesResponse**](SupportRolesResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get support roles |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **grant_support_access**
> SupportAccessResponse grant_support_access(support_access_request)

GrantSupportAccess: Grants FINBOURNE support access to your account

Granting support access will allow FINBOURNE employees full access to your data with the express intent to investigate support issues  You can revoke this (and all) access at any time using the InvalidateSupportAccess endpoint.

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    AuthenticationApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(AuthenticationApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # support_access_request = SupportAccessRequest.from_json("")
        # support_access_request = SupportAccessRequest.from_dict({})
        support_access_request = SupportAccessRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.grant_support_access(support_access_request, opts=opts)

            # GrantSupportAccess: Grants FINBOURNE support access to your account
            api_response = await api_instance.grant_support_access(support_access_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuthenticationApi->grant_support_access: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_access_request** | [**SupportAccessRequest**](SupportAccessRequest.md)| Request detailing the duration and reasons for supplying support access | 

### Return type

[**SupportAccessResponse**](SupportAccessResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Grant Support Access |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **invalidate_support_access**
> List[SupportAccessResponse] invalidate_support_access()

InvalidateSupportAccess: Revoke any FINBOURNE support access to your account

This will result in a loss of access to your data for all FINBOURNE support agents

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    AuthenticationApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(AuthenticationApi)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.invalidate_support_access(opts=opts)

            # InvalidateSupportAccess: Revoke any FINBOURNE support access to your account
            api_response = await api_instance.invalidate_support_access()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuthenticationApi->invalidate_support_access: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[SupportAccessResponse]**](SupportAccessResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invalidate all currently active support requests |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_password_policy**
> PasswordPolicyResponse update_password_policy(user_type, update_password_policy_request=update_password_policy_request)

[EXPERIMENTAL] UpdatePasswordPolicy: Updates password policy for a user type

Update the password policy for a given user type

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    AuthenticationApi
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

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(AuthenticationApi)
        user_type = 'user_type_example' # str | The type of user (should only be personal or service)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # update_password_policy_request = UpdatePasswordPolicyRequest.from_json("")
        # update_password_policy_request = UpdatePasswordPolicyRequest.from_dict({})
        update_password_policy_request = UpdatePasswordPolicyRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_password_policy(user_type, update_password_policy_request=update_password_policy_request, opts=opts)

            # [EXPERIMENTAL] UpdatePasswordPolicy: Updates password policy for a user type
            api_response = await api_instance.update_password_policy(user_type, update_password_policy_request=update_password_policy_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling AuthenticationApi->update_password_policy: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_type** | **str**| The type of user (should only be personal or service) | 
 **update_password_policy_request** | [**UpdatePasswordPolicyRequest**](UpdatePasswordPolicyRequest.md)| The password policy for the given user type | [optional] 

### Return type

[**PasswordPolicyResponse**](PasswordPolicyResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update password policy |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

