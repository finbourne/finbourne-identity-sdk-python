# finbourne_identity.CellManagementApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_cell_attachment**](CellManagementApi.md#accept_cell_attachment) | **POST** /api/cellmanagement/acceptattachment | [EARLY ACCESS] AcceptCellAttachment: Accept (or retry) a cell attachment
[**detach_parent_cell**](CellManagementApi.md#detach_parent_cell) | **PUT** /api/cellmanagement/detach | [EARLY ACCESS] DetachParentCell: Detach this cell from its parent
[**get_cell_parent_status**](CellManagementApi.md#get_cell_parent_status) | **GET** /api/cellmanagement/parentcell | [EARLY ACCESS] GetCellParentStatus: Get cell parent status
[**refuse_cell_attachment**](CellManagementApi.md#refuse_cell_attachment) | **POST** /api/cellmanagement/refuseattachment | [EARLY ACCESS] RefuseCellAttachment: Refuse a Proposed cell attachment
[**remove_primary_domain**](CellManagementApi.md#remove_primary_domain) | **DELETE** /api/cellmanagement/primarydomain | [EARLY ACCESS] RemovePrimaryDomain: Remove primary domain
[**set_attaching_key**](CellManagementApi.md#set_attaching_key) | **PUT** /api/cellmanagement/attachingkey | [EARLY ACCESS] SetAttachingKey: Store the Attaching Key pasted from the parent admin portal
[**set_parent_cell**](CellManagementApi.md#set_parent_cell) | **PUT** /api/cellmanagement/parentcell | [EARLY ACCESS] SetParentCell: Set parent cell
[**set_primary_domain**](CellManagementApi.md#set_primary_domain) | **PUT** /api/cellmanagement/primarydomain | [EARLY ACCESS] SetPrimaryDomain: Set primary domain


# **accept_cell_attachment**
> CellParentStatusResponse accept_cell_attachment()

[EARLY ACCESS] AcceptCellAttachment: Accept (or retry) a cell attachment

Confirms a Proposed attachment, or retries one that previously failed: transitions the cell to Attaching and runs the shared registration service to provision the parent-cell service user, mint a PAT, and push it to the parent admin domain. Accepted starting states are `Proposed` (the normal first confirm — anti-circumvention is enforced by requiring a prior `SetAttachingKey`) and `Failed` (recovery from a previous failed attempt). The registration service is idempotent and resumes from the persisted `RegistrationStep` checkpoint, so this is safe to call any number of times after a failure. To abandon a failed attempt instead of retrying, call `Detach`. Only the designated primary domain may call this. Requires JWT authentication.

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    CellManagementApi
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
    api_instance = api_client_factory.build(CellManagementApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.accept_cell_attachment(opts=opts)

        # [EARLY ACCESS] AcceptCellAttachment: Accept (or retry) a cell attachment
        api_response = api_instance.accept_cell_attachment()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CellManagementApi->accept_cell_attachment: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **detach_parent_cell**
> CellParentStatusResponse detach_parent_cell(detach_parent_cell_request)

[EARLY ACCESS] DetachParentCell: Detach this cell from its parent

Double-invoke pattern. First call with `Confirm=false` transitions the cell into Detaching; second call with `Confirm=true` executes: deactivates the parent-cell service user, deletes the Attaching Key from ParameterStore, and best-effort notifies the parent admin domain. Accepts `Attached`, `Attaching`, `Failed`, and `Detaching` as valid starting states (call `AcceptAttachment` instead if you'd rather retry a Failed cell than abandon it). Only the designated primary domain may call this. Requires JWT authentication.

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    CellManagementApi
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
    api_instance = api_client_factory.build(CellManagementApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # detach_parent_cell_request = DetachParentCellRequest.from_json("")
    # detach_parent_cell_request = DetachParentCellRequest.from_dict({})
    detach_parent_cell_request = DetachParentCellRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.detach_parent_cell(detach_parent_cell_request, opts=opts)

        # [EARLY ACCESS] DetachParentCell: Detach this cell from its parent
        api_response = api_instance.detach_parent_cell(detach_parent_cell_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CellManagementApi->detach_parent_cell: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detach_parent_cell_request** | [**DetachParentCellRequest**](DetachParentCellRequest.md)|  | 

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_cell_parent_status**
> CellParentStatusResponse get_cell_parent_status()

[EARLY ACCESS] GetCellParentStatus: Get cell parent status

Returns the current cell parent relationship status including primary domain, admin domain name, and attachment status.

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    CellManagementApi
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
    api_instance = api_client_factory.build(CellManagementApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_cell_parent_status(opts=opts)

        # [EARLY ACCESS] GetCellParentStatus: Get cell parent status
        api_response = api_instance.get_cell_parent_status()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CellManagementApi->get_cell_parent_status: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cell parent status |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **refuse_cell_attachment**
> CellParentStatusResponse refuse_cell_attachment()

[EARLY ACCESS] RefuseCellAttachment: Refuse a Proposed cell attachment

Rejects a Proposed attachment, deletes the Attaching Key from ParameterStore, and returns the cell to Standalone. Only the designated primary domain may call this. Requires JWT authentication.

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    CellManagementApi
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
    api_instance = api_client_factory.build(CellManagementApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.refuse_cell_attachment(opts=opts)

        # [EARLY ACCESS] RefuseCellAttachment: Refuse a Proposed cell attachment
        api_response = api_instance.refuse_cell_attachment()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CellManagementApi->refuse_cell_attachment: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **remove_primary_domain**
> CellParentStatusResponse remove_primary_domain()

[EARLY ACCESS] RemovePrimaryDomain: Remove primary domain

Removes the primary domain designation for this cell. Only the current primary domain or FINBOURNE staff can perform this. Requires JWT authentication (PAT tokens are rejected).

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    CellManagementApi
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
    api_instance = api_client_factory.build(CellManagementApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.remove_primary_domain(opts=opts)

        # [EARLY ACCESS] RemovePrimaryDomain: Remove primary domain
        api_response = api_instance.remove_primary_domain()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CellManagementApi->remove_primary_domain: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_attaching_key**
> CellParentStatusResponse set_attaching_key(set_attaching_key_request)

[EARLY ACCESS] SetAttachingKey: Store the Attaching Key pasted from the parent admin portal

Persists the Attaching Key PAT to the cell's ParameterStore / Azure Key Vault and records a Proposed attachment against the provided parent admin domain. Only the designated primary domain may call this. Requires JWT authentication (PAT tokens are rejected).

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    CellManagementApi
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
    api_instance = api_client_factory.build(CellManagementApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # set_attaching_key_request = SetAttachingKeyRequest.from_json("")
    # set_attaching_key_request = SetAttachingKeyRequest.from_dict({})
    set_attaching_key_request = SetAttachingKeyRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_attaching_key(set_attaching_key_request, opts=opts)

        # [EARLY ACCESS] SetAttachingKey: Store the Attaching Key pasted from the parent admin portal
        api_response = api_instance.set_attaching_key(set_attaching_key_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CellManagementApi->set_attaching_key: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_attaching_key_request** | [**SetAttachingKeyRequest**](SetAttachingKeyRequest.md)|  | 

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_parent_cell**
> CellParentStatusResponse set_parent_cell(set_parent_cell_request)

[EARLY ACCESS] SetParentCell: Set parent cell

Sets the parent cell for this cell. Uses a double-invoke pattern: first call (confirm=false) sets status to Proposed, second call (confirm=true) transitions to Attaching. Only the designated primary domain can call this. Requires JWT authentication (PAT tokens are rejected).

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    CellManagementApi
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
    api_instance = api_client_factory.build(CellManagementApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # set_parent_cell_request = SetParentCellRequest.from_json("")
    # set_parent_cell_request = SetParentCellRequest.from_dict({})
    set_parent_cell_request = SetParentCellRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_parent_cell(set_parent_cell_request, opts=opts)

        # [EARLY ACCESS] SetParentCell: Set parent cell
        api_response = api_instance.set_parent_cell(set_parent_cell_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CellManagementApi->set_parent_cell: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_parent_cell_request** | [**SetParentCellRequest**](SetParentCellRequest.md)|  | 

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **set_primary_domain**
> CellParentStatusResponse set_primary_domain()

[EARLY ACCESS] SetPrimaryDomain: Set primary domain

Designates the calling domain as the primary domain for this cell. Requires JWT authentication (PAT tokens are rejected).

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    CellManagementApi
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
    api_instance = api_client_factory.build(CellManagementApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.set_primary_domain(opts=opts)

        # [EARLY ACCESS] SetPrimaryDomain: Set primary domain
        api_response = api_instance.set_primary_domain()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling CellManagementApi->set_primary_domain: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CellParentStatusResponse**](CellParentStatusResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated cell parent status |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

