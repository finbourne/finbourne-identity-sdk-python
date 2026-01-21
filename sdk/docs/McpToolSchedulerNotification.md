# McpToolSchedulerNotification

A notification configuration for a scheduler job
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of notification (e.g., \&quot;Email\&quot;, \&quot;Webhook\&quot;) | 
**target** | **str** | The target of the notification (e.g., email address, webhook URL) | 
**trigger** | **str** | When to send the notification (e.g., \&quot;OnSuccess\&quot;, \&quot;OnFailure\&quot;, \&quot;Always\&quot;) | 
## Example

```python
from finbourne_identity.models.mcp_tool_scheduler_notification import McpToolSchedulerNotification
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

type: StrictStr = "example_type"
target: StrictStr = "example_target"
trigger: StrictStr = "example_trigger"
mcp_tool_scheduler_notification_instance = McpToolSchedulerNotification(type=type, target=target, trigger=trigger)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

