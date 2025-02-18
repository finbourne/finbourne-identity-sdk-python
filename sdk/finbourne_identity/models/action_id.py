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


from typing import Any, Dict
from pydantic.v1 import StrictStr, Field, BaseModel, Field, constr 

class ActionId(BaseModel):
    """
    ActionId
    """
    scope:  StrictStr = Field(...,alias="scope") 
    activity:  StrictStr = Field(...,alias="activity") 
    entity:  StrictStr = Field(...,alias="entity") 
    __properties = ["scope", "activity", "entity"]

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
    def from_json(cls, json_str: str) -> ActionId:
        """Create an instance of ActionId from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ActionId:
        """Create an instance of ActionId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ActionId.parse_obj(obj)

        _obj = ActionId.parse_obj({
            "scope": obj.get("scope"),
            "activity": obj.get("activity"),
            "entity": obj.get("entity")
        })
        return _obj
