# CreateApplicationRequest

A request to create an application for authenticating the source of token requests
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The Display Name of the application | 
**client_id** | **str** | The OpenID Connect ClientId of the application | 
**type** | **str** | The Type of the application. This must be either Native or Web | 
**redirect_uris** | **List[str]** | A web application&#39;s acceptable list of post-login redirect URIs | [optional] 
**post_logout_redirect_uris** | **List[str]** | A web application&#39;s acceptable list of post-logout redirect URIs | [optional] 
## Example

```python
from finbourne_identity.models.create_application_request import CreateApplicationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

display_name: StrictStr = "example_display_name"
client_id: StrictStr = "example_client_id"
type: StrictStr = "example_type"
redirect_uris: Optional[List[StrictStr]] = # Replace with your value
post_logout_redirect_uris: Optional[List[StrictStr]] = # Replace with your value
create_application_request_instance = CreateApplicationRequest(display_name=display_name, client_id=client_id, type=type, redirect_uris=redirect_uris, post_logout_redirect_uris=post_logout_redirect_uris)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

