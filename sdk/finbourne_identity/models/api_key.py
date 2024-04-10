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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

class ApiKey(BaseModel):
    """
    The metadata of an API key  # noqa: E501
    """
    id: constr(strict=True, max_length=64, min_length=1) = Field(..., description="The unique Id of the API key")
    display_name: constr(strict=True, max_length=512, min_length=1) = Field(..., alias="displayName", description="The display name of the API key")
    created_date: datetime = Field(..., alias="createdDate", description="The creation date of the API key")
    deactivation_date: Optional[datetime] = Field(None, alias="deactivationDate", description="The deactivation date of the API key")
    __properties = ["id", "displayName", "createdDate", "deactivationDate"]

    @validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9\-_]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\-_]+$/")
        return value

    @validator('display_name')
    def display_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
    def from_json(cls, json_str: str) -> ApiKey:
        """Create an instance of ApiKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if deactivation_date (nullable) is None
        # and __fields_set__ contains the field
        if self.deactivation_date is None and "deactivation_date" in self.__fields_set__:
            _dict['deactivationDate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiKey:
        """Create an instance of ApiKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiKey.parse_obj(obj)

        _obj = ApiKey.parse_obj({
            "id": obj.get("id"),
            "display_name": obj.get("displayName"),
            "created_date": obj.get("createdDate"),
            "deactivation_date": obj.get("deactivationDate")
        })
        return _obj
