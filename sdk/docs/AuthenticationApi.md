# finbourne_identity.AuthenticationApi

All URIs are relative to *https://fbn-ci.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_authentication_information**](AuthenticationApi.md#get_authentication_information) | **GET** /api/authentication/information | GetAuthenticationInformation: Gets AuthenticationInformation
[**get_support_access_history**](AuthenticationApi.md#get_support_access_history) | **GET** /api/authentication/support | [EARLY ACCESS] GetSupportAccessHistory: Get the history of all support access granted and any information pertaining to their termination
[**grant_support_access**](AuthenticationApi.md#grant_support_access) | **POST** /api/authentication/support | [EARLY ACCESS] GrantSupportAccess: Grants FINBOURNE support access to your account
[**invalidate_support_access**](AuthenticationApi.md#invalidate_support_access) | **DELETE** /api/authentication/support | [EARLY ACCESS] InvalidateSupportAccess: Revoke any FINBOURNE support access to your account


# **get_authentication_information**
> AuthenticationInformation get_authentication_information()

GetAuthenticationInformation: Gets AuthenticationInformation

Get the AuthenticationInformation associated with the current domain. This includes all the  necessary information to login to this domain.

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
    api_instance = finbourne_identity.AuthenticationApi(api_client)
    
    try:
        # GetAuthenticationInformation: Gets AuthenticationInformation
        api_response = api_instance.get_authentication_information()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_authentication_information: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationInformation**](AuthenticationInformation.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get authentication information |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_support_access_history**
> list[SupportAccessResponse] get_support_access_history()

[EARLY ACCESS] GetSupportAccessHistory: Get the history of all support access granted and any information pertaining to their termination

The active and inactive support requests will be returned, inactive support requests will have information pertaining to their termination  including obfuscated userIds of those who created and terminated the request

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
    api_instance = finbourne_identity.AuthenticationApi(api_client)
    
    try:
        # [EARLY ACCESS] GetSupportAccessHistory: Get the history of all support access granted and any information pertaining to their termination
        api_response = api_instance.get_support_access_history()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->get_support_access_history: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SupportAccessResponse]**](SupportAccessResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get support access history |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grant_support_access**
> SupportAccessResponse grant_support_access(support_access_request)

[EARLY ACCESS] GrantSupportAccess: Grants FINBOURNE support access to your account

Granting support access will allow FINBOURNE employees full access to your data with the express intent to investigate support issues  You can revoke this (and all) access at any time using the InvalidateSupportAccess endpoint.

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
    api_instance = finbourne_identity.AuthenticationApi(api_client)
    support_access_request = {"duration":"PT24H","description":"Investigate issues detailed in support ticket 0604"} # SupportAccessRequest | Request detailing the duration and reasons for supplying support access

    try:
        # [EARLY ACCESS] GrantSupportAccess: Grants FINBOURNE support access to your account
        api_response = api_instance.grant_support_access(support_access_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->grant_support_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support_access_request** | [**SupportAccessRequest**](SupportAccessRequest.md)| Request detailing the duration and reasons for supplying support access | 

### Return type

[**SupportAccessResponse**](SupportAccessResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Grant Support Access |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_support_access**
> list[SupportAccessResponse] invalidate_support_access()

[EARLY ACCESS] InvalidateSupportAccess: Revoke any FINBOURNE support access to your account

This will result in a loss of access to your data for all FINBOURNE support agents

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
    api_instance = finbourne_identity.AuthenticationApi(api_client)
    
    try:
        # [EARLY ACCESS] InvalidateSupportAccess: Revoke any FINBOURNE support access to your account
        api_response = api_instance.invalidate_support_access()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->invalidate_support_access: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SupportAccessResponse]**](SupportAccessResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Invalidate all currently active support requests |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

