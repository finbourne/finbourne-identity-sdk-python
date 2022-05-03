# finbourne_identity.ApplicationsApi

All URIs are relative to *https://fbn-ci.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationsApi.md#create_application) | **POST** /api/applications | [EARLY ACCESS] CreateApplication: Create Application
[**delete_application**](ApplicationsApi.md#delete_application) | **DELETE** /api/applications/{id} | [EARLY ACCESS] DeleteApplication: Delete Application
[**get_application**](ApplicationsApi.md#get_application) | **GET** /api/applications/{id} | [EARLY ACCESS] GetApplication: Get Application
[**list_applications**](ApplicationsApi.md#list_applications) | **GET** /api/applications | [EARLY ACCESS] ListApplications: List Applications
[**rotate_application_secrets**](ApplicationsApi.md#rotate_application_secrets) | **POST** /api/applications/{id}/lifecycle/$newsecret | [EXPERIMENTAL] RotateApplicationSecrets: Rotate Application Secrets


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
    api_instance = finbourne_identity.ApplicationsApi(api_client)
    create_application_request = {"displayName":"My First Application","clientId":"my-first-application","type":"Native"} # CreateApplicationRequest | Details of the application to be created (optional)

    try:
        # [EARLY ACCESS] CreateApplication: Create Application
        api_response = api_instance.create_application(create_application_request=create_application_request)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = finbourne_identity.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier for the application

    try:
        # [EARLY ACCESS] DeleteApplication: Delete Application
        api_instance.delete_application(id)
    except ApiException as e:
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
**204** | Success |  -  |
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
    api_instance = finbourne_identity.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier for the application
include_secret = True # bool | Optional. If set to true, the application secrets will be returned in plain text (optional)

    try:
        # [EARLY ACCESS] GetApplication: Get Application
        api_response = api_instance.get_application(id, include_secret=include_secret)
        pprint(api_response)
    except ApiException as e:
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
> list[OAuthApplication] list_applications()

[EARLY ACCESS] ListApplications: List Applications

List the available applications

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
    api_instance = finbourne_identity.ApplicationsApi(api_client)
    
    try:
        # [EARLY ACCESS] ListApplications: List Applications
        api_response = api_instance.list_applications()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationsApi->list_applications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OAuthApplication]**](OAuthApplication.md)

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

[EXPERIMENTAL] RotateApplicationSecrets: Rotate Application Secrets

Rotate the secrets for the specified application

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
    api_instance = finbourne_identity.ApplicationsApi(api_client)
    id = 'id_example' # str | The unique identifier for the application

    try:
        # [EXPERIMENTAL] RotateApplicationSecrets: Rotate Application Secrets
        api_response = api_instance.rotate_application_secrets(id)
        pprint(api_response)
    except ApiException as e:
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

