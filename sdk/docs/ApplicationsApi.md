# finbourne_identity.ApplicationsApi

All URIs are relative to *https://www.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationsApi.md#create_application) | **POST** /api/applications | [EARLY ACCESS] Create Application
[**delete_application**](ApplicationsApi.md#delete_application) | **DELETE** /api/applications/{id} | [EARLY ACCESS] Delete Application
[**get_application**](ApplicationsApi.md#get_application) | **GET** /api/applications/{id} | [EARLY ACCESS] Get Application
[**list_applications**](ApplicationsApi.md#list_applications) | **GET** /api/applications | [EARLY ACCESS] List Applications


# **create_application**
> OAuthApplication create_application(create_application_request=create_application_request)

[EARLY ACCESS] Create Application

Create a new Application

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

# Defining host is optional and default to https://www.lusid.com/identity
configuration.host = "https://www.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.ApplicationsApi(finbourne_identity.ApiClient(configuration))
create_application_request = {"displayName":"My First Application","clientId":"my-first-application","type":"native"} # CreateApplicationRequest | Details of the application to be created (optional)

try:
    # [EARLY ACCESS] Create Application
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
**201** | Create Application |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(id)

[EARLY ACCESS] Delete Application

Delete the specified application

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

# Defining host is optional and default to https://www.lusid.com/identity
configuration.host = "https://www.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.ApplicationsApi(finbourne_identity.ApiClient(configuration))
id = 'id_example' # str | The unique identifier for the application

try:
    # [EARLY ACCESS] Delete Application
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

[EARLY ACCESS] Get Application

get the specified application, and optionally the OIDC secret

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

# Defining host is optional and default to https://www.lusid.com/identity
configuration.host = "https://www.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.ApplicationsApi(finbourne_identity.ApiClient(configuration))
id = 'id_example' # str | The unique identifier for the application
include_secret = True # bool | Optional. If set to true, the application secrets will be returned in plain text (optional)

try:
    # [EARLY ACCESS] Get Application
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

[EARLY ACCESS] List Applications

List the available applications

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

# Defining host is optional and default to https://www.lusid.com/identity
configuration.host = "https://www.lusid.com/identity"
# Create an instance of the API class
api_instance = finbourne_identity.ApplicationsApi(finbourne_identity.ApiClient(configuration))

try:
    # [EARLY ACCESS] List Applications
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

