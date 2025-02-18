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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr 

class SupportRole(BaseModel):
    """
    SupportRole
    """
    label:  Optional[StrictStr] = Field(None,alias="label") 
    description:  Optional[StrictStr] = Field(None,alias="description") 
    role_identifier: Optional[Dict[str, StrictStr]] = Field(None, alias="roleIdentifier")
    internal_identifier:  Optional[StrictStr] = Field(None,alias="internalIdentifier") 
    __properties = ["label", "description", "roleIdentifier", "internalIdentifier"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SupportRole:
        """Create an instance of SupportRole from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict['label'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if role_identifier (nullable) is None
        # and __fields_set__ contains the field
        if self.role_identifier is None and "role_identifier" in self.__fields_set__:
            _dict['roleIdentifier'] = None

        # set to None if internal_identifier (nullable) is None
        # and __fields_set__ contains the field
        if self.internal_identifier is None and "internal_identifier" in self.__fields_set__:
            _dict['internalIdentifier'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SupportRole:
        """Create an instance of SupportRole from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SupportRole.parse_obj(obj)

        _obj = SupportRole.parse_obj({
            "label": obj.get("label"),
            "description": obj.get("description"),
            "role_identifier": obj.get("roleIdentifier"),
            "internal_identifier": obj.get("internalIdentifier")
        })
        return _obj
