# finbourne_identity.ApplicationsApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationsApi.md#create_application) | **POST** /api/applications | [EARLY ACCESS] CreateApplication: Create Application
[**delete_application**](ApplicationsApi.md#delete_application) | **DELETE** /api/applications/{id} | [EARLY ACCESS] DeleteApplication: Delete Application
[**get_application**](ApplicationsApi.md#get_application) | **GET** /api/applications/{id} | [EARLY ACCESS] GetApplication: Get Application
[**list_applications**](ApplicationsApi.md#list_applications) | **GET** /api/applications | [EARLY ACCESS] ListApplications: List Applications
[**rotate_application_secrets**](ApplicationsApi.md#rotate_application_secrets) | **POST** /api/applications/{id}/lifecycle/$newsecret | [EARLY ACCESS] RotateApplicationSecrets: Rotate Application Secrets


# **create_application**
> OAuthApplication create_application(create_application_request=create_application_request)

[EARLY ACCESS] CreateApplication: Create Application

Create a new Application

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from finbourne_identity.models.create_application_request import CreateApplicationRequest
from finbourne_identity.models.o_auth_application import OAuthApplication
from pprint import pprint

import os
from finbourne_identity import (
    ApiClientFactory,
    ApplicationsApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/identity"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_identity.ApplicationsApi)
    create_application_request = {"displayName":"My First Application","clientId":"my-first-application","type":"Native"} # CreateApplicationRequest | Details of the application to be created (optional)

    try:
        # [EARLY ACCESS] CreateApplication: Create Application
        api_response = await api_instance.create_application(create_application_request=create_application_request)
        print("The response of ApplicationsApi->create_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_application_request** | [**CreateApplicationRequest**](CreateApplicationRequest.md)| Details of the application to be created | [optional] 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create Application |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(id)

[EARLY ACCESS] DeleteApplication: Delete Application

Delete the specified application

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint

import os
from finbourne_identity import (
    ApiClientFactory,
    ApplicationsApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/identity"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_identity.ApplicationsApi)
    id = 'id_example' # str | The unique identifier for the application

    try:
        # [EARLY ACCESS] DeleteApplication: Delete Application
        await api_instance.delete_application(id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the application | 

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
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> OAuthApplication get_application(id, include_secret=include_secret)

[EARLY ACCESS] GetApplication: Get Application

get the specified application, and optionally the OIDC secret

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from finbourne_identity.models.o_auth_application import OAuthApplication
from pprint import pprint

import os
from finbourne_identity import (
    ApiClientFactory,
    ApplicationsApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/identity"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_identity.ApplicationsApi)
    id = 'id_example' # str | The unique identifier for the application
    include_secret = True # bool | Optional. If set to true, the application secrets will be returned in plain text (optional)

    try:
        # [EARLY ACCESS] GetApplication: Get Application
        api_response = await api_instance.get_application(id, include_secret=include_secret)
        print("The response of ApplicationsApi->get_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the application | 
 **include_secret** | **bool**| Optional. If set to true, the application secrets will be returned in plain text | [optional] 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### Authorization

[oauth2](../README.md#oauth2)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_applications**
> List[OAuthApplication] list_applications()

[EARLY ACCESS] ListApplications: List Applications

List the available applications

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from finbourne_identity.models.o_auth_application import OAuthApplication
from pprint import pprint

import os
from finbourne_identity import (
    ApiClientFactory,
    ApplicationsApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/identity"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_identity.ApplicationsApi)

    try:
        # [EARLY ACCESS] ListApplications: List Applications
        api_response = await api_instance.list_applications()
        print("The response of ApplicationsApi->list_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_applications: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[OAuthApplication]**](OAuthApplication.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List the available applications |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rotate_application_secrets**
> OAuthApplication rotate_application_secrets(id)

[EARLY ACCESS] RotateApplicationSecrets: Rotate Application Secrets

Rotate the secrets for the specified application

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from finbourne_identity.models.o_auth_application import OAuthApplication
from pprint import pprint

import os
from finbourne_identity import (
    ApiClientFactory,
    ApplicationsApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/identity"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_identity.ApplicationsApi)
    id = 'id_example' # str | The unique identifier for the application

    try:
        # [EARLY ACCESS] RotateApplicationSecrets: Rotate Application Secrets
        api_response = await api_instance.rotate_application_secrets(id)
        print("The response of ApplicationsApi->rotate_application_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->rotate_application_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the application | 

### Return type

[**OAuthApplication**](OAuthApplication.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rotate Application Secrets |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

