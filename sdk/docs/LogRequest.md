# LogRequest

Represents a LogRequest resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_chain** | [**List[LogIpChainEntry]**](LogIpChainEntry.md) |  | [optional] 
## Example

```python
from finbourne_identity.models.log_request import LogRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

ip_chain: Optional[conlist(LogIpChainEntry)] = # Replace with your value
log_request_instance = LogRequest(ip_chain=ip_chain)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

