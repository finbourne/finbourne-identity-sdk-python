# finbourne_identity.MeApi

All URIs are relative to *https://fbn-ci.lusid.com/identity*

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
    api_instance = finbourne_identity.MeApi(api_client)
    
    try:
        # [EARLY ACCESS] GetUserInfo: Get User Info
        api_response = api_instance.get_user_info()
        pprint(api_response)
    except ApiException as e:
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
    api_instance = finbourne_identity.MeApi(api_client)
    set_password = {"value":""} # SetPassword | The request containing the new password value

    try:
        # SetPassword: Set password of current user
        api_response = api_instance.set_password(set_password)
        pprint(api_response)
    except ApiException as e:
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

