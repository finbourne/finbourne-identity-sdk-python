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
from pydantic.v1 import BaseModel, Field
from finbourne_identity.models.password_policy_response_conditions import PasswordPolicyResponseConditions

class PasswordPolicyResponse(BaseModel):
    """
    PasswordPolicyResponse
    """
    conditions: PasswordPolicyResponseConditions = Field(...)
    __properties = ["conditions"]

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
    def from_json(cls, json_str: str) -> PasswordPolicyResponse:
        """Create an instance of PasswordPolicyResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of conditions
        if self.conditions:
            _dict['conditions'] = self.conditions.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PasswordPolicyResponse:
        """Create an instance of PasswordPolicyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PasswordPolicyResponse.parse_obj(obj)

        _obj = PasswordPolicyResponse.parse_obj({
            "conditions": PasswordPolicyResponseConditions.from_dict(obj.get("conditions")) if obj.get("conditions") is not None else None
        })
        return _obj
