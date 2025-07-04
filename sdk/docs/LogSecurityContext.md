# LogSecurityContext

Represents a LogSecurityContext resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **int** |  | [optional] 
**as_org** | **str** |  | [optional] 
**isp** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**is_proxy** | **bool** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_security_context import LogSecurityContext
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr

as_number: Optional[StrictInt] = # Replace with your value
as_number: Optional[StrictInt] = None
as_org: Optional[StrictStr] = "example_as_org"
isp: Optional[StrictStr] = "example_isp"
domain: Optional[StrictStr] = "example_domain"
is_proxy: Optional[StrictBool] = # Replace with your value
is_proxy:Optional[StrictBool] = None
log_security_context_instance = LogSecurityContext(as_number=as_number, as_org=as_org, isp=isp, domain=domain, is_proxy=is_proxy)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

