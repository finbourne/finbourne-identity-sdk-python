# finbourne_identity.IdentityProviderApi

All URIs are relative to *https://fbn-ci.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scim**](IdentityProviderApi.md#add_scim) | **PUT** /api/identityprovider/scim | [EARLY ACCESS] AddScim: Add SCIM
[**remove_scim**](IdentityProviderApi.md#remove_scim) | **DELETE** /api/identityprovider/scim | [EARLY ACCESS] RemoveScim: Remove SCIM


# **add_scim**
> AddScimResponse add_scim(api_token_action=api_token_action, old_api_token_deactivation=old_api_token_deactivation)

[EARLY ACCESS] AddScim: Add SCIM

Generates an API token to be used for SCIM

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.IdentityProviderApi(api_client)
    api_token_action = 'api_token_action_example' # str | The action to take. For the API token. Defaults to \"ensure\" (optional)
old_api_token_deactivation = '2013-10-20T19:20:30+01:00' # datetime | Optional deactivation date for the old API token. Only used if apiTokenAction is \"regenerate\" (optional)

    try:
        # [EARLY ACCESS] AddScim: Add SCIM
        api_response = api_instance.add_scim(api_token_action=api_token_action, old_api_token_deactivation=old_api_token_deactivation)
        pprint(api_response)
    except ApiException as e:
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

[EARLY ACCESS] RemoveScim: Remove SCIM

Deactivates any existing SCIM API token

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_identity
from finbourne_identity.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/identity
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_identity.Configuration(
    host = "https://fbn-ci.lusid.com/identity"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_identity.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_identity.IdentityProviderApi(api_client)
    
    try:
        # [EARLY ACCESS] RemoveScim: Remove SCIM
        api_instance.remove_scim()
    except ApiException as e:
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

