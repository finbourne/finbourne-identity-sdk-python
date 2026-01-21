# McpToolParameter

A parameter definition for an MCP tool
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the parameter (identifier format) | 
**data_type** | **str** | The data type of the parameter | 
**description** | **str** | A description of what the parameter is used for | [optional] 
## Example

```python
from finbourne_identity.models.mcp_tool_parameter import McpToolParameter
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

name: StrictStr = "example_name"
data_type: StrictStr = "example_data_type"
description: Optional[StrictStr] = "example_description"
mcp_tool_parameter_instance = McpToolParameter(name=name, data_type=data_type, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

