# McpToolLuminescePayload

Payload data for a Luminesce query MCP tool
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | The Luminesce query to execute | 
## Example

```python
from finbourne_identity.models.mcp_tool_luminesce_payload import McpToolLuminescePayload
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

query: StrictStr = "example_query"
mcp_tool_luminesce_payload_instance = McpToolLuminescePayload(query=query)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

