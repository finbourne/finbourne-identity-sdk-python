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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr, validator

class SupportAccessRequest(BaseModel):
    """
    A Request to grant support access to your account  # noqa: E501
    """
    duration: constr(strict=True, max_length=30, min_length=2) = Field(..., description="The duration for which access is requested (in any ISO-8601 format)")
    description: Optional[constr(strict=True, max_length=1024, min_length=0)] = Field(None, description="The description of why the support access has been granted (i.e. support ticket numbers)")
    permitted_roles: Optional[conlist(StrictStr)] = Field(None, alias="permittedRoles")
    __properties = ["duration", "description", "permittedRoles"]

    @validator('duration')
    def duration_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^P(?!$)((\d+Y)|(\d+\.\d+Y$))?((\d+M)|(\d+\.\d+M$))?((\d+W)|(\d+\.\d+W$))?((\d+D)|(\d+\.\d+D$))?(T(?=\d)((\d+H)|(\d+\.\d+H$))?((\d+M)|(\d+\.\d+M$))?(\d+(\.\d+)?S)?)??$", value):
            raise ValueError(r"must validate the regular expression /^P(?!$)((\d+Y)|(\d+\.\d+Y$))?((\d+M)|(\d+\.\d+M$))?((\d+W)|(\d+\.\d+W$))?((\d+D)|(\d+\.\d+D$))?(T(?=\d)((\d+H)|(\d+\.\d+H$))?((\d+M)|(\d+\.\d+M$))?(\d+(\.\d+)?S)?)??$/")
        return value

    @validator('description')
    def description_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[\s\S]*$", value):
            raise ValueError(r"must validate the regular expression /^[\s\S]*$/")
        return value

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
    def from_json(cls, json_str: str) -> SupportAccessRequest:
        """Create an instance of SupportAccessRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if permitted_roles (nullable) is None
        # and __fields_set__ contains the field
        if self.permitted_roles is None and "permitted_roles" in self.__fields_set__:
            _dict['permittedRoles'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SupportAccessRequest:
        """Create an instance of SupportAccessRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SupportAccessRequest.parse_obj(obj)

        _obj = SupportAccessRequest.parse_obj({
            "duration": obj.get("duration"),
            "description": obj.get("description"),
            "permitted_roles": obj.get("permittedRoles")
        })
        return _obj
