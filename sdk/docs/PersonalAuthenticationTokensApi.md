# finbourne_identity.PersonalAuthenticationTokensApi

All URIs are relative to *https://fbn-ci.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key**](PersonalAuthenticationTokensApi.md#create_api_key) | **POST** /api/keys | [EXPERIMENTAL] Create a Personal Access Token
[**delete_api_key**](PersonalAuthenticationTokensApi.md#delete_api_key) | **DELETE** /api/keys/{id} | [EXPERIMENTAL] Invalidate a Personal Access Token
[**list_own_api_keys**](PersonalAuthenticationTokensApi.md#list_own_api_keys) | **GET** /api/keys | [EXPERIMENTAL] Gets the meta data for all of the user&#39;s existing Personal Access Tokens.


# **create_api_key**
> CreatedApiKey create_api_key(create_api_key)

[EXPERIMENTAL] Create a Personal Access Token

Generates a Personal Access Token and returns the new key and its associated metadata.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
configuration = finbourne_identity.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-ci.lusid.com/identity
configuration.host = "https://fbn-ci.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.PersonalAuthenticationTokensApi(finbourne_identity.ApiClient(configuration))
create_api_key = {"displayName":"My API Key","deactivationDate":"2022-12-08T13:30:12.0000000+00:00"} # CreateApiKey | The request to create a new Personal Access Token

try:
    # [EXPERIMENTAL] Create a Personal Access Token
    api_response = api_instance.create_api_key(create_api_key)
    pprint(api_response)
except ApiException as e:
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
**201** | The Personal Access Token and associated meta data. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> ApiKey delete_api_key(id)

[EXPERIMENTAL] Invalidate a Personal Access Token

Immediately invalidates the specified Personal Access Token

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
configuration = finbourne_identity.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-ci.lusid.com/identity
configuration.host = "https://fbn-ci.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.PersonalAuthenticationTokensApi(finbourne_identity.ApiClient(configuration))
id = 'id_example' # str | The id of the Personal Access Token to delete

try:
    # [EXPERIMENTAL] Invalidate a Personal Access Token
    api_response = api_instance.delete_api_key(id)
    pprint(api_response)
except ApiException as e:
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
> list[ApiKey] list_own_api_keys()

[EXPERIMENTAL] Gets the meta data for all of the user's existing Personal Access Tokens.

Gets the meta data for all of the user's Personal Access Tokens that have not been deleted. They may be  invalid due to the deactivation date having passed.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
configuration = finbourne_identity.Configuration()
# Configure OAuth2 access token for authorization: oauth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://fbn-ci.lusid.com/identity
configuration.host = "https://fbn-ci.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.PersonalAuthenticationTokensApi(finbourne_identity.ApiClient(configuration))

try:
    # [EXPERIMENTAL] Gets the meta data for all of the user's existing Personal Access Tokens.
    api_response = api_instance.list_own_api_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PersonalAuthenticationTokensApi->list_own_api_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ApiKey]**](ApiKey.md)

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

