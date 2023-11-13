# finbourne_identity.MeApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_info**](MeApi.md#get_user_info) | **GET** /api/me | [EARLY ACCESS] GetUserInfo: Get User Info
[**set_password**](MeApi.md#set_password) | **PUT** /api/me/password | SetPassword: Set password of current user


# **get_user_info**
> CurrentUserResponse get_user_info()

[EARLY ACCESS] GetUserInfo: Get User Info

Get the requesting user's basic info

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_identity
from finbourne_identity.rest import ApiException
from finbourne_identity.models.current_user_response import CurrentUserResponse
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
    api_instance = api_client_factory.build(finbourne_identity.MeApi)

    try:
        # [EARLY ACCESS] GetUserInfo: Get User Info
        api_response = await api_instance.get_user_info()
        print("The response of MeApi->get_user_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->get_user_info: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentUserResponse**](CurrentUserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the specified user&#39;s info |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_password**
> SetPasswordResponse set_password(set_password)

SetPassword: Set password of current user

Set the password of the current user to the specified value.                Note this is feature is only available to Service users authenticated using OpenID. For further information  relating to usage of this feature please consult the documentation.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import os
import finbourne_identity
from finbourne_identity.rest import ApiException
from finbourne_identity.models.set_password import SetPassword
from finbourne_identity.models.set_password_response import SetPasswordResponse
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
    api_instance = api_client_factory.build(finbourne_identity.MeApi)
    set_password = {"value":""} # SetPassword | The request containing the new password value

    try:
        # SetPassword: Set password of current user
        api_response = await api_instance.set_password(set_password)
        print("The response of MeApi->set_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MeApi->set_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_password** | [**SetPassword**](SetPassword.md)| The request containing the new password value | 

### Return type

[**SetPasswordResponse**](SetPasswordResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set the current user&#39;s password |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

