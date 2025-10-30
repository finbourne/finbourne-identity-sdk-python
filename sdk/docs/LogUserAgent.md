# LogUserAgent

Represents a LogUserAgent resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw_user_agent** | **str** |  | [optional] 
**operating_system** | **str** |  | [optional] 
**browser** | **str** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_user_agent import LogUserAgent
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

raw_user_agent: Optional[StrictStr] = "example_raw_user_agent"
operating_system: Optional[StrictStr] = "example_operating_system"
browser: Optional[StrictStr] = "example_browser"
log_user_agent_instance = LogUserAgent(raw_user_agent=raw_user_agent, operating_system=operating_system, browser=browser)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

