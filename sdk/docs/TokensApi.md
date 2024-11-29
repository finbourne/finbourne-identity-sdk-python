# finbourne_identity.TokensApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invalidate_token**](TokensApi.md#invalidate_token) | **DELETE** /api/tokens | InvalidateToken: Invalidate current JWT token (sign out)


# **invalidate_token**
> invalidate_token()

InvalidateToken: Invalidate current JWT token (sign out)

Log the current user out of all Finbourne platforms by invalidating the current token

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    TokensApi
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
    api_instance = api_client_factory.build(TokensApi)

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.invalidate_token(opts=opts)

        # InvalidateToken: Invalidate current JWT token (sign out)
        api_instance.invalidate_token()
    except ApiException as e:
        print("Exception when calling TokensApi->invalidate_token: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

