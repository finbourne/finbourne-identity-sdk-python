# UserSchemaProperty

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
## Example

```python
from finbourne_identity.models.user_schema_property import UserSchemaProperty
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

name: StrictStr = "example_name"
description: StrictStr = "example_description"
user_schema_property_instance = UserSchemaProperty(name=name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

