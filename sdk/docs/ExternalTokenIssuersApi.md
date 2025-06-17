# finbourne_identity.ExternalTokenIssuersApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_token_issuer**](ExternalTokenIssuersApi.md#create_external_token_issuer) | **POST** /api/externaltokenissuers | [EARLY ACCESS] CreateExternalTokenIssuer: Create an External Token Issuer
[**delete_external_token_issuer**](ExternalTokenIssuersApi.md#delete_external_token_issuer) | **DELETE** /api/externaltokenissuers/{code} | [EARLY ACCESS] DeleteExternalTokenIssuer: Deletes an External Token Issuer by code
[**get_external_token_issuer**](ExternalTokenIssuersApi.md#get_external_token_issuer) | **GET** /api/externaltokenissuers/{code} | [EARLY ACCESS] GetExternalTokenIssuer: Gets an External Token Issuer with code
[**list_external_token_issuers**](ExternalTokenIssuersApi.md#list_external_token_issuers) | **GET** /api/externaltokenissuers | [EARLY ACCESS] ListExternalTokenIssuers: Lists all External Token Issuers for a domain
[**update_external_token_issuer**](ExternalTokenIssuersApi.md#update_external_token_issuer) | **PUT** /api/externaltokenissuers/{code} | [EARLY ACCESS] UpdateExternalTokenIssuer: Updates an existing External Token Issuer


# **create_external_token_issuer**
> ExternalTokenIssuerResponse create_external_token_issuer(create_external_token_issuer_request)

[EARLY ACCESS] CreateExternalTokenIssuer: Create an External Token Issuer

Creates an External Token Issuer

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    ExternalTokenIssuersApi
)

def main():

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

    # Use the finbourne_identity SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ExternalTokenIssuersApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_external_token_issuer_request = CreateExternalTokenIssuerRequest.from_json("")
    # create_external_token_issuer_request = CreateExternalTokenIssuerRequest.from_dict({})
    create_external_token_issuer_request = CreateExternalTokenIssuerRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_external_token_issuer(create_external_token_issuer_request, opts=opts)

        # [EARLY ACCESS] CreateExternalTokenIssuer: Create an External Token Issuer
        api_response = api_instance.create_external_token_issuer(create_external_token_issuer_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ExternalTokenIssuersApi->create_external_token_issuer: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_external_token_issuer_request** | [**CreateExternalTokenIssuerRequest**](CreateExternalTokenIssuerRequest.md)|  | 

### Return type

[**ExternalTokenIssuerResponse**](ExternalTokenIssuerResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create External Token Issuer |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_external_token_issuer**
> delete_external_token_issuer(code)

[EARLY ACCESS] DeleteExternalTokenIssuer: Deletes an External Token Issuer by code

Deletes an External Token Issuer

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    ExternalTokenIssuersApi
)

def main():

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

    # Use the finbourne_identity SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ExternalTokenIssuersApi)
    code = 'code_example' # str | Identifier of the External Token Issuer to delete

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_external_token_issuer(code, opts=opts)

        # [EARLY ACCESS] DeleteExternalTokenIssuer: Deletes an External Token Issuer by code
        api_instance.delete_external_token_issuer(code)
    except ApiException as e:
        print("Exception when calling ExternalTokenIssuersApi->delete_external_token_issuer: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Identifier of the External Token Issuer to delete | 

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

# **get_external_token_issuer**
> ExternalTokenIssuerResponse get_external_token_issuer(code)

[EARLY ACCESS] GetExternalTokenIssuer: Gets an External Token Issuer with code

Gets an External Token Issuer

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    ExternalTokenIssuersApi
)

def main():

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

    # Use the finbourne_identity SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ExternalTokenIssuersApi)
    code = 'code_example' # str | Identifier of the External Token Issuer

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_external_token_issuer(code, opts=opts)

        # [EARLY ACCESS] GetExternalTokenIssuer: Gets an External Token Issuer with code
        api_response = api_instance.get_external_token_issuer(code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ExternalTokenIssuersApi->get_external_token_issuer: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Identifier of the External Token Issuer | 

### Return type

[**ExternalTokenIssuerResponse**](ExternalTokenIssuerResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get External Token Issuer |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_external_token_issuers**
> List[ExternalTokenIssuerResponse] list_external_token_issuers()

[EARLY ACCESS] ListExternalTokenIssuers: Lists all External Token Issuers for a domain

Lists all External Token Issuers

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    ExternalTokenIssuersApi
)

def main():

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

    # Use the finbourne_identity SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ExternalTokenIssuersApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_external_token_issuers(opts=opts)

        # [EARLY ACCESS] ListExternalTokenIssuers: Lists all External Token Issuers for a domain
        api_response = api_instance.list_external_token_issuers()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ExternalTokenIssuersApi->list_external_token_issuers: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ExternalTokenIssuerResponse]**](ExternalTokenIssuerResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List External Token Issuers |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_external_token_issuer**
> ExternalTokenIssuerResponse update_external_token_issuer(code, update_external_token_issuer_request)

[EARLY ACCESS] UpdateExternalTokenIssuer: Updates an existing External Token Issuer

Updates an External Token Issuer

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    ExternalTokenIssuersApi
)

def main():

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

    # Use the finbourne_identity SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(ExternalTokenIssuersApi)
    code = 'code_example' # str | Identifier of the External Token Issuer to update

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_external_token_issuer_request = UpdateExternalTokenIssuerRequest.from_json("")
    # update_external_token_issuer_request = UpdateExternalTokenIssuerRequest.from_dict({})
    update_external_token_issuer_request = UpdateExternalTokenIssuerRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_external_token_issuer(code, update_external_token_issuer_request, opts=opts)

        # [EARLY ACCESS] UpdateExternalTokenIssuer: Updates an existing External Token Issuer
        api_response = api_instance.update_external_token_issuer(code, update_external_token_issuer_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ExternalTokenIssuersApi->update_external_token_issuer: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Identifier of the External Token Issuer to update | 
 **update_external_token_issuer_request** | [**UpdateExternalTokenIssuerRequest**](UpdateExternalTokenIssuerRequest.md)|  | 

### Return type

[**ExternalTokenIssuerResponse**](ExternalTokenIssuerResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update External Token Issuer |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

