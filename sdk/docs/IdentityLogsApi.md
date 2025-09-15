# finbourne_identity.IdentityLogsApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_logs**](IdentityLogsApi.md#list_logs) | **GET** /api/logs | [BETA] ListLogs: Lists system logs for a domain
[**list_user_logs**](IdentityLogsApi.md#list_user_logs) | **GET** /api/logs/me | ListUserLogs: Lists user logs


# **list_logs**
> ResourceListOfSystemLog list_logs(okta_since=okta_since, okta_until=okta_until, okta_filter=okta_filter, okta_query=okta_query, okta_limit=okta_limit, okta_sort_order=okta_sort_order, okta_after=okta_after)

[BETA] ListLogs: Lists system logs for a domain

Lists system logs for a domain

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    IdentityLogsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "identityUrl":"https://<your-domain>.lusid.com/identity",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_identity SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(IdentityLogsApi)
    okta_since = '2013-10-20T19:20:30+01:00' # datetime | Lower bound of log events published property (optional)
    okta_until = '2013-10-20T19:20:30+01:00' # datetime | Upper bound of log events published property (optional)
    okta_filter = 'okta_filter_example' # str | Okta filter expression (optional)
    okta_query = 'okta_query_example' # str | Filters log events results by one or more case insensitive keywords (optional)
    okta_limit = 56 # int | Max number of results returned (optional)
    okta_sort_order = 'okta_sort_order_example' # str | Order of events by published property. Either ASCENDING or DESCENDING (optional)
    okta_after = 'okta_after_example' # str | Okta Page token (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_logs(okta_since=okta_since, okta_until=okta_until, okta_filter=okta_filter, okta_query=okta_query, okta_limit=okta_limit, okta_sort_order=okta_sort_order, okta_after=okta_after, opts=opts)

        # [BETA] ListLogs: Lists system logs for a domain
        api_response = api_instance.list_logs(okta_since=okta_since, okta_until=okta_until, okta_filter=okta_filter, okta_query=okta_query, okta_limit=okta_limit, okta_sort_order=okta_sort_order, okta_after=okta_after)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling IdentityLogsApi->list_logs: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **okta_since** | **datetime**| Lower bound of log events published property | [optional] 
 **okta_until** | **datetime**| Upper bound of log events published property | [optional] 
 **okta_filter** | **str**| Okta filter expression | [optional] 
 **okta_query** | **str**| Filters log events results by one or more case insensitive keywords | [optional] 
 **okta_limit** | **int**| Max number of results returned | [optional] 
 **okta_sort_order** | **str**| Order of events by published property. Either ASCENDING or DESCENDING | [optional] 
 **okta_after** | **str**| Okta Page token | [optional] 

### Return type

[**ResourceListOfSystemLog**](ResourceListOfSystemLog.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Logs |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_user_logs**
> ResourceListOfSystemLog list_user_logs(okta_since=okta_since, okta_until=okta_until, okta_limit=okta_limit, okta_sort_order=okta_sort_order, okta_after=okta_after)

ListUserLogs: Lists user logs

Lists account related system logs for the calling user

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    IdentityLogsApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "identityUrl":"https://<your-domain>.lusid.com/identity",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_identity SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(IdentityLogsApi)
    okta_since = '2013-10-20T19:20:30+01:00' # datetime | Lower bound of log events published property (optional)
    okta_until = '2013-10-20T19:20:30+01:00' # datetime | Upper bound of log events published property (optional)
    okta_limit = 56 # int | Max number of results returned (optional)
    okta_sort_order = 'okta_sort_order_example' # str | Order of events by published property. Either ASCENDING or DESCENDING (optional)
    okta_after = 'okta_after_example' # str | Okta Page token (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_user_logs(okta_since=okta_since, okta_until=okta_until, okta_limit=okta_limit, okta_sort_order=okta_sort_order, okta_after=okta_after, opts=opts)

        # ListUserLogs: Lists user logs
        api_response = api_instance.list_user_logs(okta_since=okta_since, okta_until=okta_until, okta_limit=okta_limit, okta_sort_order=okta_sort_order, okta_after=okta_after)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling IdentityLogsApi->list_user_logs: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **okta_since** | **datetime**| Lower bound of log events published property | [optional] 
 **okta_until** | **datetime**| Upper bound of log events published property | [optional] 
 **okta_limit** | **int**| Max number of results returned | [optional] 
 **okta_sort_order** | **str**| Order of events by published property. Either ASCENDING or DESCENDING | [optional] 
 **okta_after** | **str**| Okta Page token | [optional] 

### Return type

[**ResourceListOfSystemLog**](ResourceListOfSystemLog.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List User Logs |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

