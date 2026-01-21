# McpToolResponse

The response representation of an MCP tool
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the MCP tool | [optional] 
**code** | **str** | The code of the MCP tool | [optional] 
**name** | **str** | The name of the MCP tool | [optional] 
**version** | **int** | The version number of this MCP tool | [optional] 
**title** | **str** | The title of the MCP tool | [optional] 
**description** | **str** | The description of the MCP tool | [optional] 
**destructive** | **bool** | Whether the tool is destructive | [optional] 
**idempotent** | **bool** | Whether the tool is idempotent | [optional] 
**open_world** | **bool** | Whether the tool operates in open world | [optional] 
**read_only** | **bool** | Whether the tool is read-only | [optional] 
**parameters** | [**List[McpToolParameter]**](McpToolParameter.md) | The parameters for this MCP tool | [optional] 
**payload_type** | **str** | The type of payload (Luminesce or Scheduler) | [optional] 
**luminesce_payload** | [**McpToolLuminescePayload**](McpToolLuminescePayload.md) |  | [optional] 
**scheduler_payload** | [**McpToolSchedulerPayload**](McpToolSchedulerPayload.md) |  | [optional] 
**created_at** | **datetime** | When the MCP tool was created | [optional] 
**created_by** | **str** | Who created the MCP tool | [optional] 
**updated_at** | **datetime** | When the MCP tool was last updated | [optional] 
**updated_by** | **str** | Who last updated the MCP tool | [optional] 
## Example

```python
from finbourne_identity.models.mcp_tool_response import McpToolResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
name: Optional[StrictStr] = "example_name"
version: Optional[StrictInt] = # Replace with your value
version: Optional[StrictInt] = None
title: Optional[StrictStr] = "example_title"
description: Optional[StrictStr] = "example_description"
destructive: Optional[StrictBool] = # Replace with your value
destructive:Optional[StrictBool] = None
idempotent: Optional[StrictBool] = # Replace with your value
idempotent:Optional[StrictBool] = None
open_world: Optional[StrictBool] = # Replace with your value
open_world:Optional[StrictBool] = None
read_only: Optional[StrictBool] = # Replace with your value
read_only:Optional[StrictBool] = None
parameters: Optional[List[McpToolParameter]] = # Replace with your value
payload_type: Optional[StrictStr] = "example_payload_type"
luminesce_payload: Optional[McpToolLuminescePayload] = # Replace with your value
scheduler_payload: Optional[McpToolSchedulerPayload] = # Replace with your value
created_at: Optional[datetime] = # Replace with your value
created_by: Optional[StrictStr] = "example_created_by"
updated_at: Optional[datetime] = # Replace with your value
updated_by: Optional[StrictStr] = "example_updated_by"
mcp_tool_response_instance = McpToolResponse(scope=scope, code=code, name=name, version=version, title=title, description=description, destructive=destructive, idempotent=idempotent, open_world=open_world, read_only=read_only, parameters=parameters, payload_type=payload_type, luminesce_payload=luminesce_payload, scheduler_payload=scheduler_payload, created_at=created_at, created_by=created_by, updated_at=updated_at, updated_by=updated_by)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

