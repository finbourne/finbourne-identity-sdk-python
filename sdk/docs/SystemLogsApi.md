# finbourne_identity.SystemLogsApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_logs**](SystemLogsApi.md#list_logs) | **GET** /api/logs | [BETA] ListLogs: Lists system logs for a domain


# **list_logs**
> ResourceListOfSystemLog list_logs(since=since, until=until, after=after, filter=filter, query=query, limit=limit, sort_order=sort_order)

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
    SystemLogsApi
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
    api_instance = api_client_factory.build(SystemLogsApi)
    since = '2013-10-20T19:20:30+01:00' # datetime | Lower bound of log events published property (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime | Upper bound of log events published property (optional)
    after = 'after_example' # str | Page token (optional)
    filter = 'filter_example' # str | Okta filter expression (optional)
    query = 'query_example' # str | Filters log events results by one or more case insensitive keywords (optional)
    limit = 56 # int | Max number of results returned (optional)
    sort_order = 'sort_order_example' # str | Order of events by published property. Either ASCENDING or DESCENDING (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_logs(since=since, until=until, after=after, filter=filter, query=query, limit=limit, sort_order=sort_order, opts=opts)

        # [BETA] ListLogs: Lists system logs for a domain
        api_response = api_instance.list_logs(since=since, until=until, after=after, filter=filter, query=query, limit=limit, sort_order=sort_order)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling SystemLogsApi->list_logs: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| Lower bound of log events published property | [optional] 
 **until** | **datetime**| Upper bound of log events published property | [optional] 
 **after** | **str**| Page token | [optional] 
 **filter** | **str**| Okta filter expression | [optional] 
 **query** | **str**| Filters log events results by one or more case insensitive keywords | [optional] 
 **limit** | **int**| Max number of results returned | [optional] 
 **sort_order** | **str**| Order of events by published property. Either ASCENDING or DESCENDING | [optional] 

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

