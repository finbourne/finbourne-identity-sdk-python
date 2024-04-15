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

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from finbourne_identity.models.add_scim_response import AddScimResponse
from pprint import pprint

import os
from finbourne_identity import (
    ApiClientFactory,
    IdentityProviderApi,
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
    api_instance = api_client_factory.build(finbourne_identity.IdentityProviderApi)
    api_token_action = 'api_token_action_example' # str | The action to take. For the API token. Defaults to \"ensure\" (optional)
    old_api_token_deactivation = '2013-10-20T19:20:30+01:00' # datetime | Optional deactivation date for the old API token. Only used if apiTokenAction is \"regenerate\" (optional)

    try:
        # AddScim: Add SCIM
        api_response = await api_instance.add_scim(api_token_action=api_token_action, old_api_token_deactivation=old_api_token_deactivation)
        print("The response of IdentityProviderApi->add_scim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderApi->add_scim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token_action** | **str**| The action to take. For the API token. Defaults to \&quot;ensure\&quot; | [optional] 
 **old_api_token_deactivation** | **datetime**| Optional deactivation date for the old API token. Only used if apiTokenAction is \&quot;regenerate\&quot; | [optional] 

### Return type

[**AddScimResponse**](AddScimResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The base URL and API token to be used |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_scim**
> remove_scim()

RemoveScim: Remove SCIM

Deactivates any existing SCIM API token

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
    IdentityProviderApi,
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
    api_instance = api_client_factory.build(finbourne_identity.IdentityProviderApi)

    try:
        # RemoveScim: Remove SCIM
        await api_instance.remove_scim()
    except Exception as e:
        print("Exception when calling IdentityProviderApi->remove_scim: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

