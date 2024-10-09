# finbourne_identity.ApplicationsApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationsApi.md#create_application) | **POST** /api/applications | [EARLY ACCESS] CreateApplication: Create Application
[**delete_application**](ApplicationsApi.md#delete_application) | **DELETE** /api/applications/{id} | [EARLY ACCESS] DeleteApplication: Delete Application
[**get_application**](ApplicationsApi.md#get_application) | **GET** /api/applications/{id} | GetApplication: Get Application
[**list_applications**](ApplicationsApi.md#list_applications) | **GET** /api/applications | ListApplications: List Applications
[**rotate_application_secrets**](ApplicationsApi.md#rotate_application_secrets) | **POST** /api/applications/{id}/lifecycle/$newsecret | [EARLY ACCESS] RotateApplicationSecrets: Rotate Application Secrets


# **create_application**
> OAuthApplication create_application(create_application_request=create_application_request)

[EARLY ACCESS] CreateApplication: Create Application

Create a new Application

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    ApplicationsApi
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
        api_instance = api_client_factory.build(ApplicationsApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # create_application_request = CreateApplicationRequest.from_json("")
        # create_application_request = CreateApplicationRequest.from_dict({})
        create_application_request = CreateApplicationRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_application(create_application_request=create_application_request, opts=opts)

            # [EARLY ACCESS] CreateApplication: Create Application
            api_response = await api_instance.create_application(create_application_request=create_application_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ApplicationsApi->create_application: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_application_request** | [**CreateApplicationRequest**](CreateApplicationRequest.md)| Details of the application to be created | [optional] 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create Application |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_application**
> delete_application(id)

[EARLY ACCESS] DeleteApplication: Delete Application

Delete the specified application

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    ApplicationsApi
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
        api_instance = api_client_factory.build(ApplicationsApi)
        id = 'id_example' # str | The unique identifier for the application

        try:
            # uncomment the below to set overrides at the request level
            # await api_instance.delete_application(id, opts=opts)

            # [EARLY ACCESS] DeleteApplication: Delete Application
            await api_instance.delete_application(id)        except ApiException as e:
            print("Exception when calling ApplicationsApi->delete_application: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the application | 

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

# **get_application**
> OAuthApplication get_application(id, include_secret=include_secret)

GetApplication: Get Application

get the specified application, and optionally the OIDC secret

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    ApplicationsApi
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
        api_instance = api_client_factory.build(ApplicationsApi)
        id = 'id_example' # str | The unique identifier for the application
        include_secret = True # bool | Optional. If set to true, the application secrets will be returned in plain text (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_application(id, include_secret=include_secret, opts=opts)

            # GetApplication: Get Application
            api_response = await api_instance.get_application(id, include_secret=include_secret)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ApplicationsApi->get_application: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the application | 
 **include_secret** | **bool**| Optional. If set to true, the application secrets will be returned in plain text | [optional] 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the specified application |  -  |
**404** | Not Found |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_applications**
> List[OAuthApplication] list_applications()

ListApplications: List Applications

List the available applications

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    ApplicationsApi
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
        api_instance = api_client_factory.build(ApplicationsApi)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_applications(opts=opts)

            # ListApplications: List Applications
            api_response = await api_instance.list_applications()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ApplicationsApi->list_applications: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[OAuthApplication]**](OAuthApplication.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the available applications |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **rotate_application_secrets**
> OAuthApplication rotate_application_secrets(id)

[EARLY ACCESS] RotateApplicationSecrets: Rotate Application Secrets

Rotate the secrets for the specified application

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    ApplicationsApi
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
        api_instance = api_client_factory.build(ApplicationsApi)
        id = 'id_example' # str | The unique identifier for the application

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.rotate_application_secrets(id, opts=opts)

            # [EARLY ACCESS] RotateApplicationSecrets: Rotate Application Secrets
            api_response = await api_instance.rotate_application_secrets(id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ApplicationsApi->rotate_application_secrets: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the application | 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rotate Application Secrets |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

