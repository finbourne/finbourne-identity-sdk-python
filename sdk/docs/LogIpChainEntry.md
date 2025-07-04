# LogIpChainEntry

Represents a LogIpChainEntry resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**geographical_context** | [**LogGeographicalContext**](LogGeographicalContext.md) |  | [optional] 
**version** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_ip_chain_entry import LogIpChainEntry
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

ip: Optional[StrictStr] = "example_ip"
geographical_context: Optional[LogGeographicalContext] = # Replace with your value
version: Optional[StrictStr] = "example_version"
source: Optional[StrictStr] = "example_source"
log_ip_chain_entry_instance = LogIpChainEntry(ip=ip, geographical_context=geographical_context, version=version, source=source)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

