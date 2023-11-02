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
from pydantic import BaseModel, Field, StrictStr

class ErrorDetail(BaseModel):
    """
    Provides details about an entity error that occured  # noqa: E501
    """
    id: Optional[StrictStr] = Field(None, description="Id of the entity this error relates to")
    type: Optional[StrictStr] = Field(None, description="Error type")
    detail: Optional[StrictStr] = Field(None, description="Human readable description of the error")
    __properties = ["id", "type", "detail"]

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
    def from_json(cls, json_str: str) -> ErrorDetail:
        """Create an instance of ErrorDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if id (nullable) is None
        # and __fields_set__ contains the field
        if self.id is None and "id" in self.__fields_set__:
            _dict['id'] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if detail (nullable) is None
        # and __fields_set__ contains the field
        if self.detail is None and "detail" in self.__fields_set__:
            _dict['detail'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ErrorDetail:
        """Create an instance of ErrorDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorDetail.parse_obj(obj)

        _obj = ErrorDetail.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "detail": obj.get("detail")
        })
        return _obj
