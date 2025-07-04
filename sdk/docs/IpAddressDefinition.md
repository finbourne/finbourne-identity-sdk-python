# IpAddressDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**value** | **str** |  | 
## Example

```python
from finbourne_identity.models.ip_address_definition import IpAddressDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

type: Optional[StrictStr] = "example_type"
description: Optional[StrictStr] = "example_description"
value: StrictStr = "example_value"
ip_address_definition_instance = IpAddressDefinition(type=type, description=description, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

