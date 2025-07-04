# SupportRole

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**role_identifier** | **Dict[str, str]** |  | [optional] 
**internal_identifier** | **str** |  | [optional] 
## Example

```python
from finbourne_identity.models.support_role import SupportRole
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

label: Optional[StrictStr] = "example_label"
description: Optional[StrictStr] = "example_description"
role_identifier: Optional[Dict[str, StrictStr]] = # Replace with your value
internal_identifier: Optional[StrictStr] = "example_internal_identifier"
support_role_instance = SupportRole(label=label, description=description, role_identifier=role_identifier, internal_identifier=internal_identifier)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

