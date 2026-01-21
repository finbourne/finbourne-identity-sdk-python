# McpToolSchedulerPayload

Payload data for a Scheduler job MCP tool
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_scope** | **str** | The scope of the scheduler job to run | 
**job_code** | **str** | The code of the scheduler job to run | 
**arguments** | **Dict[str, Optional[str]]** | Arguments to pass to the scheduler job (key-value pairs) | [optional] 
**run_as** | **str** | Optional service user identifier to run the job as (if not the current user) | [optional] 
**notifications** | [**List[McpToolSchedulerNotification]**](McpToolSchedulerNotification.md) | Optional additional notifications for the job | [optional] 
## Example

```python
from finbourne_identity.models.mcp_tool_scheduler_payload import McpToolSchedulerPayload
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

job_scope: StrictStr = "example_job_scope"
job_code: StrictStr = "example_job_code"
arguments: Optional[Dict[str, Optional[StrictStr]]] = # Replace with your value
run_as: Optional[StrictStr] = "example_run_as"
notifications: Optional[List[McpToolSchedulerNotification]] = # Replace with your value
mcp_tool_scheduler_payload_instance = McpToolSchedulerPayload(job_scope=job_scope, job_code=job_code, arguments=arguments, run_as=run_as, notifications=notifications)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

