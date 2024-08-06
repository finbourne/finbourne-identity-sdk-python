# finbourne_identity.MeApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_info**](MeApi.md#get_user_info) | **GET** /api/me | GetUserInfo: Get User Info
[**set_password**](MeApi.md#set_password) | **PUT** /api/me/password | SetPassword: Set password of current user


# **get_user_info**
> CurrentUserResponse get_user_info()

GetUserInfo: Get User Info

Get the requesting user's basic info

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    MeApi
)

async def main():

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

    # Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(MeApi)

        try:
            # GetUserInfo: Get User Info
            api_response = await api_instance.get_user_info()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling MeApi->get_user_info: %s\n" % e)

asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CurrentUserResponse**](CurrentUserResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the specified user&#39;s info |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_password**
> SetPasswordResponse set_password(set_password)

SetPassword: Set password of current user

Set the password of the current user to the specified value.                Note this is feature is only available to Service users authenticated using OpenID. For further information  relating to usage of this feature please consult the documentation.

### Example

```python
import asyncio
from finbourne_identity.exceptions import ApiException
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    ApiClientFactory,
    MeApi
)

async def main():

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

    # Use the finbourne_identity ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(MeApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # set_password = SetPassword()
        # set_password = SetPassword.from_json("")
        set_password = SetPassword.from_dict({"value":""}) # SetPassword | The request containing the new password value

        try:
            # SetPassword: Set password of current user
            api_response = await api_instance.set_password(set_password)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling MeApi->set_password: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_password** | [**SetPassword**](SetPassword.md)| The request containing the new password value | 

### Return type

[**SetPasswordResponse**](SetPasswordResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set the current user&#39;s password |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

