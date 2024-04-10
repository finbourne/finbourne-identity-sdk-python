# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr
from finbourne_identity.models.role_id import RoleId

class RoleResponse(BaseModel):
    """
    RoleResponse
    """
    id: constr(strict=True, min_length=1) = Field(..., description="The role's system supplied unique identifier")
    role_id: RoleId = Field(..., alias="roleId")
    source: constr(strict=True, min_length=1) = Field(..., description="The source of the role")
    name: constr(strict=True, min_length=1) = Field(..., description="The role name, which must be unique within the system.")
    description: Optional[StrictStr] = Field(None, description="The description for this role")
    saml_name: Optional[StrictStr] = Field(None, alias="samlName", description="The name to use on the SAML request if assigning this role via SAML Just in Time (JIT)")
    __properties = ["id", "roleId", "source", "name", "description", "samlName"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RoleResponse:
        """Create an instance of RoleResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of role_id
        if self.role_id:
            _dict['roleId'] = self.role_id.to_dict()
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if saml_name (nullable) is None
        # and __fields_set__ contains the field
        if self.saml_name is None and "saml_name" in self.__fields_set__:
            _dict['samlName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleResponse:
        """Create an instance of RoleResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoleResponse.parse_obj(obj)

        _obj = RoleResponse.parse_obj({
            "id": obj.get("id"),
            "role_id": RoleId.from_dict(obj.get("roleId")) if obj.get("roleId") is not None else None,
            "source": obj.get("source"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "saml_name": obj.get("samlName")
        })
        return _obj
