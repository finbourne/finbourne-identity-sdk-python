# finbourne_identity.MCPToolsApi

All URIs are relative to *https://fbn-prd.lusid.com/identity*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mcp_tool**](MCPToolsApi.md#create_mcp_tool) | **POST** /api/mcptools/{scope}/{code} | [EARLY ACCESS] CreateMcpTool: Create an MCP Tool
[**delete_mcp_tool**](MCPToolsApi.md#delete_mcp_tool) | **DELETE** /api/mcptools/{scope}/{code} | [EARLY ACCESS] DeleteMcpTool: Delete an MCP Tool
[**get_mcp_tool**](MCPToolsApi.md#get_mcp_tool) | **GET** /api/mcptools/{scope}/{code} | [EARLY ACCESS] GetMcpTool: Get an MCP Tool
[**list_mcp_tools**](MCPToolsApi.md#list_mcp_tools) | **GET** /api/mcptools | [EARLY ACCESS] ListMcpTools: List all MCP Tools
[**update_mcp_tool**](MCPToolsApi.md#update_mcp_tool) | **PUT** /api/mcptools/{scope}/{code} | [EARLY ACCESS] UpdateMcpTool: Update an MCP Tool


# **create_mcp_tool**
> McpToolResponse create_mcp_tool(scope, code, upsert_mcp_tool_request)

[EARLY ACCESS] CreateMcpTool: Create an MCP Tool

Creates a new MCP tool definition

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    MCPToolsApi
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
    api_instance = api_client_factory.build(MCPToolsApi)
    scope = 'scope_example' # str | The scope of the MCP tool
    code = 'code_example' # str | The code of the MCP tool

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_mcp_tool_request = UpsertMcpToolRequest.from_json("")
    # upsert_mcp_tool_request = UpsertMcpToolRequest.from_dict({})
    upsert_mcp_tool_request = UpsertMcpToolRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_mcp_tool(scope, code, upsert_mcp_tool_request, opts=opts)

        # [EARLY ACCESS] CreateMcpTool: Create an MCP Tool
        api_response = api_instance.create_mcp_tool(scope, code, upsert_mcp_tool_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MCPToolsApi->create_mcp_tool: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the MCP tool | 
 **code** | **str**| The code of the MCP tool | 
 **upsert_mcp_tool_request** | [**UpsertMcpToolRequest**](UpsertMcpToolRequest.md)| The MCP tool definition | 

### Return type

[**McpToolResponse**](McpToolResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create MCP Tool |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_mcp_tool**
> delete_mcp_tool(scope, code)

[EARLY ACCESS] DeleteMcpTool: Delete an MCP Tool

Deletes an MCP tool (soft delete - closes the current version)

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    MCPToolsApi
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
    api_instance = api_client_factory.build(MCPToolsApi)
    scope = 'scope_example' # str | The scope of the MCP tool
    code = 'code_example' # str | The code of the MCP tool

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_mcp_tool(scope, code, opts=opts)

        # [EARLY ACCESS] DeleteMcpTool: Delete an MCP Tool
        api_instance.delete_mcp_tool(scope, code)
    except ApiException as e:
        print("Exception when calling MCPToolsApi->delete_mcp_tool: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the MCP tool | 
 **code** | **str**| The code of the MCP tool | 

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

# **get_mcp_tool**
> McpToolResponse get_mcp_tool(scope, code, version=version)

[EARLY ACCESS] GetMcpTool: Get an MCP Tool

Retrieves an MCP tool. If version is specified, retrieves that specific version for audit purposes. Otherwise, retrieves the current version.

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    MCPToolsApi
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
    api_instance = api_client_factory.build(MCPToolsApi)
    scope = 'scope_example' # str | The scope of the MCP tool
    code = 'code_example' # str | The code of the MCP tool
    version = 56 # int | Optional version number to retrieve. If not specified, returns the current version. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_mcp_tool(scope, code, version=version, opts=opts)

        # [EARLY ACCESS] GetMcpTool: Get an MCP Tool
        api_response = api_instance.get_mcp_tool(scope, code, version=version)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MCPToolsApi->get_mcp_tool: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the MCP tool | 
 **code** | **str**| The code of the MCP tool | 
 **version** | **int**| Optional version number to retrieve. If not specified, returns the current version. | [optional] 

### Return type

[**McpToolResponse**](McpToolResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get MCP Tool |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_mcp_tools**
> List[McpToolResponse] list_mcp_tools()

[EARLY ACCESS] ListMcpTools: List all MCP Tools

Lists all current MCP tools for the domain

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    MCPToolsApi
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
    api_instance = api_client_factory.build(MCPToolsApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_mcp_tools(opts=opts)

        # [EARLY ACCESS] ListMcpTools: List all MCP Tools
        api_response = api_instance.list_mcp_tools()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MCPToolsApi->list_mcp_tools: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[McpToolResponse]**](McpToolResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List MCP Tools |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_mcp_tool**
> McpToolResponse update_mcp_tool(scope, code, upsert_mcp_tool_request)

[EARLY ACCESS] UpdateMcpTool: Update an MCP Tool

Updates an existing MCP tool, creating a new version

### Example

```python
from finbourne_identity.exceptions import ApiException
from finbourne_identity.extensions.configuration_options import ConfigurationOptions
from finbourne_identity.models import *
from pprint import pprint
from finbourne_identity import (
    SyncApiClientFactory,
    MCPToolsApi
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
    api_instance = api_client_factory.build(MCPToolsApi)
    scope = 'scope_example' # str | The scope of the MCP tool
    code = 'code_example' # str | The code of the MCP tool

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # upsert_mcp_tool_request = UpsertMcpToolRequest.from_json("")
    # upsert_mcp_tool_request = UpsertMcpToolRequest.from_dict({})
    upsert_mcp_tool_request = UpsertMcpToolRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_mcp_tool(scope, code, upsert_mcp_tool_request, opts=opts)

        # [EARLY ACCESS] UpdateMcpTool: Update an MCP Tool
        api_response = api_instance.update_mcp_tool(scope, code, upsert_mcp_tool_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling MCPToolsApi->update_mcp_tool: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the MCP tool | 
 **code** | **str**| The code of the MCP tool | 
 **upsert_mcp_tool_request** | [**UpsertMcpToolRequest**](UpsertMcpToolRequest.md)| The updated MCP tool definition | 

### Return type

[**McpToolResponse**](McpToolResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update MCP Tool |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

