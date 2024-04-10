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
from pydantic.v1 import BaseModel, Field, conint

class UpdatePasswordPolicyRequestAge(BaseModel):
    """
    UpdatePasswordPolicyRequestAge
    """
    max_age_days: conint(strict=True, le=999, ge=0) = Field(..., alias="maxAgeDays", description="The maximum age (in days) a password can be before expiring and needing to be changed.  0 indicates no limit")
    history_count: conint(strict=True, le=30, ge=0) = Field(..., alias="historyCount", description="The number of unique passwords that need to be used before a previous password is permitted again.  0 indicates none")
    __properties = ["maxAgeDays", "historyCount"]

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
    def from_json(cls, json_str: str) -> UpdatePasswordPolicyRequestAge:
        """Create an instance of UpdatePasswordPolicyRequestAge from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdatePasswordPolicyRequestAge:
        """Create an instance of UpdatePasswordPolicyRequestAge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdatePasswordPolicyRequestAge.parse_obj(obj)

        _obj = UpdatePasswordPolicyRequestAge.parse_obj({
            "max_age_days": obj.get("maxAgeDays"),
            "history_count": obj.get("historyCount")
        })
        return _obj
