# finbourne_identity.PersonalAuthenticationTokensApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](PersonalAuthenticationTokensApi.md#create_api_key) | **POST** /api/keys | [EARLY ACCESS] CreateApiKey: Create a Personal Access Token
[**delete_api_key**](PersonalAuthenticationTokensApi.md#delete_api_key) | **DELETE** /api/keys/{id} | [EARLY ACCESS] DeleteApiKey: Invalidate a Personal Access Token
[**list_own_api_keys**](PersonalAuthenticationTokensApi.md#list_own_api_keys) | **GET** /api/keys | [EARLY ACCESS] ListOwnApiKeys: Gets the meta data for all of the user&#39;s existing Personal Access Tokens.


# **create_api_key**
> CreatedApiKey create_api_key(create_api_key)

[EARLY ACCESS] CreateApiKey: Create a Personal Access Token

Generates a Personal Access Token and returns the new key and its associated metadata.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_identity
from finbourne_identity.rest import ApiException
from finbourne_identity.models.create_api_key import CreateApiKey
from finbourne_identity.models.created_api_key import CreatedApiKey
from pprint import pprint

from finbourne_identity import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(finbourne_identity.PersonalAuthenticationTokensApi)
    create_api_key = {"displayName":"My API Key","deactivationDate":"2022-12-08T13:30:12.0000000+00:00"} # CreateApiKey | The request to create a new Personal Access Token

    try:
        # [EARLY ACCESS] CreateApiKey: Create a Personal Access Token
        api_response = await api_instance.create_api_key(create_api_key)
        print("The response of PersonalAuthenticationTokensApi->create_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalAuthenticationTokensApi->create_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key** | [**CreateApiKey**](CreateApiKey.md)| The request to create a new Personal Access Token | 

### Return type

[**CreatedApiKey**](CreatedApiKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Personal Access Token and associated meta data. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> ApiKey delete_api_key(id)

[EARLY ACCESS] DeleteApiKey: Invalidate a Personal Access Token

Immediately invalidates the specified Personal Access Token

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_identity
from finbourne_identity.rest import ApiException
from finbourne_identity.models.api_key import ApiKey
from pprint import pprint

from finbourne_identity import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(finbourne_identity.PersonalAuthenticationTokensApi)
    id = 'id_example' # str | The id of the Personal Access Token to delete

    try:
        # [EARLY ACCESS] DeleteApiKey: Invalidate a Personal Access Token
        api_response = await api_instance.delete_api_key(id)
        print("The response of PersonalAuthenticationTokensApi->delete_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalAuthenticationTokensApi->delete_api_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Personal Access Token to delete | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invalidates a Personal Access Token |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_own_api_keys**
> List[ApiKey] list_own_api_keys()

[EARLY ACCESS] ListOwnApiKeys: Gets the meta data for all of the user's existing Personal Access Tokens.

Gets the meta data for all of the user's Personal Access Tokens that have not been deleted. They may be  invalid due to the deactivation date having passed.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_identity
from finbourne_identity.rest import ApiException
from finbourne_identity.models.api_key import ApiKey
from pprint import pprint

from finbourne_identity import (
	  ApiClientFactory,
	  ApplicationMetadataApi,
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
    api_instance = api_client_factory.build(finbourne_identity.PersonalAuthenticationTokensApi)

    try:
        # [EARLY ACCESS] ListOwnApiKeys: Gets the meta data for all of the user's existing Personal Access Tokens.
        api_response = await api_instance.list_own_api_keys()
        print("The response of PersonalAuthenticationTokensApi->list_own_api_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersonalAuthenticationTokensApi->list_own_api_keys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ApiKey]**](ApiKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of user&#39;s existing Personal Access Tokens |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

