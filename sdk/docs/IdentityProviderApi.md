# finbourne_identity.IdentityProviderApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scim**](IdentityProviderApi.md#add_scim) | **PUT** /api/identityprovider/scim | AddScim: Add SCIM
[**remove_scim**](IdentityProviderApi.md#remove_scim) | **DELETE** /api/identityprovider/scim | RemoveScim: Remove SCIM


# **add_scim**
> AddScimResponse add_scim(api_token_action=api_token_action, old_api_token_deactivation=old_api_token_deactivation)

AddScim: Add SCIM

Generates an API token to be used for SCIM

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    IdentityProviderApi
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
        api_instance = api_client_factory.build(IdentityProviderApi)
        api_token_action = 'api_token_action_example' # str | The action to take. For the API token. Defaults to \"ensure\" (optional)
        old_api_token_deactivation = '2013-10-20T19:20:30+01:00' # datetime | Optional deactivation date for the old API token. Only used if apiTokenAction is \"regenerate\" (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.add_scim(api_token_action=api_token_action, old_api_token_deactivation=old_api_token_deactivation, opts=opts)

            # AddScim: Add SCIM
            api_response = await api_instance.add_scim(api_token_action=api_token_action, old_api_token_deactivation=old_api_token_deactivation)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling IdentityProviderApi->add_scim: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token_action** | **str**| The action to take. For the API token. Defaults to \&quot;ensure\&quot; | [optional] 
 **old_api_token_deactivation** | **datetime**| Optional deactivation date for the old API token. Only used if apiTokenAction is \&quot;regenerate\&quot; | [optional] 

### Return type

[**AddScimResponse**](AddScimResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The base URL and API token to be used |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **remove_scim**
> remove_scim()

RemoveScim: Remove SCIM

Deactivates any existing SCIM API token

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    IdentityProviderApi
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
        api_instance = api_client_factory.build(IdentityProviderApi)

        try:
            # uncomment the below to set overrides at the request level
            # await api_instance.remove_scim(opts=opts)

            # RemoveScim: Remove SCIM
            await api_instance.remove_scim()        except ApiException as e:
            print("Exception when calling IdentityProviderApi->remove_scim: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

