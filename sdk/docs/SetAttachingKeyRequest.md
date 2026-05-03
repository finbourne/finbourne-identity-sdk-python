# SetAttachingKeyRequest

Request body for setting the Attaching Key on a child cell. The three values together identify the parent admin domain, the parent's cell database row, and the PAT used to authenticate the attachment handshake.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pat** | **str** | Attaching Key PAT issued by the parent admin portal&#39;s &#x60;BeginCellRegistration&#x60; endpoint. Length bounds match admin-ui&#39;s &#x60;RegisterDomainPatRequest&#x60;. We apply &#x60;StringSecurityCheck&#x60; (the Finbourne.Validation catch-all that the recorded baseline tolerates for opaque strings) AND a stricter regex restricting the value to the opaque-token character set so the request body cannot smuggle in HTML/SQL/ script content even if the catch-all is later relaxed. | 
**parent_domain_name** | **str** | Parent admin domain name (as entered alongside the Attaching Key by the user). Used only as the initial proposal value; the admin domain stored in the DB is the source of truth for all later operations (anti-redirection). | 
**parent_assigned_cell_id** | **int** | Database identifier of this cell in the parent admin-ui&#39;s &#x60;cell&#x60; table. Returned alongside the Attaching Key by the parent&#39;s &#x60;BeginCellRegistration&#x60; response and required to call &#x60;POST /admin-ui/api/domains/{cellId}/register&#x60; during the Finbourne.Lydia.Postgres.Database.DTO.RegistrationStep.PatPushed step. | [optional] 
## Example

```python
from finbourne_identity.models.set_attaching_key_request import SetAttachingKeyRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

pat: StrictStr = "example_pat"
parent_domain_name: StrictStr = "example_parent_domain_name"
parent_assigned_cell_id: Optional[StrictInt] = # Replace with your value
set_attaching_key_request_instance = SetAttachingKeyRequest(pat=pat, parent_domain_name=parent_domain_name, parent_assigned_cell_id=parent_assigned_cell_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

