# LogAuthenticationContext

Represents a LogAuthenticationContext resource in the Okta API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_provider** | **str** |  | [optional] 
**credential_provider** | **List[str]** |  | [optional] 
**credential_type** | **List[str]** |  | [optional] 
**issuer** | [**LogIssuer**](LogIssuer.md) |  | [optional] 
**interface** | **str** |  | [optional] 
**authentication_step** | **int** |  | [optional] 
**external_session_id** | **str** |  | [optional] 
## Example

```python
from finbourne_identity.models.log_authentication_context import LogAuthenticationContext
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr, conlist

authentication_provider: Optional[StrictStr] = "example_authentication_provider"
credential_provider: Optional[conlist(StrictStr)] = # Replace with your value
credential_type: Optional[conlist(StrictStr)] = # Replace with your value
issuer: Optional[LogIssuer] = None
interface: Optional[StrictStr] = "example_interface"
authentication_step: Optional[StrictInt] = # Replace with your value
authentication_step: Optional[StrictInt] = None
external_session_id: Optional[StrictStr] = "example_external_session_id"
log_authentication_context_instance = LogAuthenticationContext(authentication_provider=authentication_provider, credential_provider=credential_provider, credential_type=credential_type, issuer=issuer, interface=interface, authentication_step=authentication_step, external_session_id=external_session_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

