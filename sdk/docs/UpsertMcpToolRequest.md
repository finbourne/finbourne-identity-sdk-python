# UpsertMcpToolRequest

Request to create or update an MCP tool
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the MCP tool (alphanumeric, underscore, and hyphen) | 
**title** | **str** | The title of the MCP tool | 
**description** | **str** | The description of the MCP tool | 
**destructive** | **bool** | Whether the tool is destructive | [optional] 
**idempotent** | **bool** | Whether the tool is idempotent | [optional] 
**open_world** | **bool** | Whether the tool operates in open world | [optional] 
**read_only** | **bool** | Whether the tool is read-only | [optional] 
**parameters** | [**List[McpToolParameter]**](McpToolParameter.md) | The parameters for this MCP tool | [optional] 
**luminesce_payload** | [**McpToolLuminescePayload**](McpToolLuminescePayload.md) |  | [optional] 
**scheduler_payload** | [**McpToolSchedulerPayload**](McpToolSchedulerPayload.md) |  | [optional] 
**destructive_action_summary_template** | **str** | Template for human-readable destructive action summary. Uses {paramName} single-brace placeholders (e.g. \&quot;Delete file &#39;{filePath}&#39;\&quot;). Required when Destructive is true. | [optional] 
## Example

```python
from finbourne_identity.models.upsert_mcp_tool_request import UpsertMcpToolRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
title: StrictStr = "example_title"
description: StrictStr = "example_description"
destructive: Optional[StrictBool] = # Replace with your value
destructive:Optional[StrictBool] = None
idempotent: Optional[StrictBool] = # Replace with your value
idempotent:Optional[StrictBool] = None
open_world: Optional[StrictBool] = # Replace with your value
open_world:Optional[StrictBool] = None
read_only: Optional[StrictBool] = # Replace with your value
read_only:Optional[StrictBool] = None
parameters: Optional[List[McpToolParameter]] = # Replace with your value
luminesce_payload: Optional[McpToolLuminescePayload] = # Replace with your value
scheduler_payload: Optional[McpToolSchedulerPayload] = # Replace with your value
destructive_action_summary_template: Optional[StrictStr] = "example_destructive_action_summary_template"
upsert_mcp_tool_request_instance = UpsertMcpToolRequest(name=name, title=title, description=description, destructive=destructive, idempotent=idempotent, open_world=open_world, read_only=read_only, parameters=parameters, luminesce_payload=luminesce_payload, scheduler_payload=scheduler_payload, destructive_action_summary_template=destructive_action_summary_template)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

