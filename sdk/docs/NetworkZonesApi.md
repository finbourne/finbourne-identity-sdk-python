# finbourne_identity.NetworkZonesApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_zone**](NetworkZonesApi.md#create_network_zone) | **POST** /api/networkzones | [EARLY ACCESS] CreateNetworkZone: Creates a network zone
[**delete_network_zone**](NetworkZonesApi.md#delete_network_zone) | **DELETE** /api/networkzones/{code} | [EARLY ACCESS] DeleteNetworkZone: Deletes a network zone
[**get_network_zone**](NetworkZonesApi.md#get_network_zone) | **GET** /api/networkzones/{code} | [EARLY ACCESS] GetNetworkZone: Retrieve a Network Zone
[**list_network_zones**](NetworkZonesApi.md#list_network_zones) | **GET** /api/networkzones | [EARLY ACCESS] ListNetworkZones: Lists all network zones for a domain
[**update_network_zone**](NetworkZonesApi.md#update_network_zone) | **PUT** /api/networkzones/{code} | [EARLY ACCESS] UpdateNetworkZone: Updates an existing network zone


# **create_network_zone**
> NetworkZoneDefinitionResponse create_network_zone(create_network_zone_request)

[EARLY ACCESS] CreateNetworkZone: Creates a network zone

By default, the network zone will have its hierarchy set to last on creation.

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    NetworkZonesApi
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
    api_instance = api_client_factory.build(NetworkZonesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # create_network_zone_request = CreateNetworkZoneRequest.from_json("")
    # create_network_zone_request = CreateNetworkZoneRequest.from_dict({})
    create_network_zone_request = CreateNetworkZoneRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_network_zone(create_network_zone_request, opts=opts)

        # [EARLY ACCESS] CreateNetworkZone: Creates a network zone
        api_response = api_instance.create_network_zone(create_network_zone_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling NetworkZonesApi->create_network_zone: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_network_zone_request** | [**CreateNetworkZoneRequest**](CreateNetworkZoneRequest.md)| The details of the network zone to define | 

### Return type

[**NetworkZoneDefinitionResponse**](NetworkZoneDefinitionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create Network Zone |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_network_zone**
> delete_network_zone(code)

[EARLY ACCESS] DeleteNetworkZone: Deletes a network zone

Will return a success if network zone already deleted

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    NetworkZonesApi
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
    api_instance = api_client_factory.build(NetworkZonesApi)
    code = 'code_example' # str | The unique identifier of the network zone to delete

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_network_zone(code, opts=opts)

        # [EARLY ACCESS] DeleteNetworkZone: Deletes a network zone
        api_instance.delete_network_zone(code)
    except ApiException as e:
        print("Exception when calling NetworkZonesApi->delete_network_zone: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The unique identifier of the network zone to delete | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_network_zone**
> NetworkZoneDefinitionResponse get_network_zone(code)

[EARLY ACCESS] GetNetworkZone: Retrieve a Network Zone

Retrieves a Network Zone

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    NetworkZonesApi
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
    api_instance = api_client_factory.build(NetworkZonesApi)
    code = 'code_example' # str | The unique identifier of the network zone

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_network_zone(code, opts=opts)

        # [EARLY ACCESS] GetNetworkZone: Retrieve a Network Zone
        api_response = api_instance.get_network_zone(code)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling NetworkZonesApi->get_network_zone: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The unique identifier of the network zone | 

### Return type

[**NetworkZoneDefinitionResponse**](NetworkZoneDefinitionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Network Zone |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_network_zones**
> List[NetworkZoneDefinitionResponse] list_network_zones()

[EARLY ACCESS] ListNetworkZones: Lists all network zones for a domain

Lists all network zones for a domain

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    NetworkZonesApi
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
    api_instance = api_client_factory.build(NetworkZonesApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_network_zones(opts=opts)

        # [EARLY ACCESS] ListNetworkZones: Lists all network zones for a domain
        api_response = api_instance.list_network_zones()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling NetworkZonesApi->list_network_zones: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[NetworkZoneDefinitionResponse]**](NetworkZoneDefinitionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Network Zones |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_network_zone**
> NetworkZoneDefinitionResponse update_network_zone(code, update_network_zone_request)

[EARLY ACCESS] UpdateNetworkZone: Updates an existing network zone

Updates an existing network zone

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    NetworkZonesApi
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
    api_instance = api_client_factory.build(NetworkZonesApi)
    code = 'code_example' # str | The unique identifier of the network zone

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # update_network_zone_request = UpdateNetworkZoneRequest.from_json("")
    # update_network_zone_request = UpdateNetworkZoneRequest.from_dict({})
    update_network_zone_request = UpdateNetworkZoneRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_network_zone(code, update_network_zone_request, opts=opts)

        # [EARLY ACCESS] UpdateNetworkZone: Updates an existing network zone
        api_response = api_instance.update_network_zone(code, update_network_zone_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling NetworkZonesApi->update_network_zone: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The unique identifier of the network zone | 
 **update_network_zone_request** | [**UpdateNetworkZoneRequest**](UpdateNetworkZoneRequest.md)| The updated definition of the network zone | 

### Return type

[**NetworkZoneDefinitionResponse**](NetworkZoneDefinitionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update Network Zone |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

