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
from finbourne_identity.models.update_password_policy_request_age import UpdatePasswordPolicyRequestAge
from finbourne_identity.models.update_password_policy_request_complexity import UpdatePasswordPolicyRequestComplexity
from finbourne_identity.models.update_password_policy_request_lockout import UpdatePasswordPolicyRequestLockout

class UpdatePasswordPolicyRequestConditions(BaseModel):
    """
    Password policy conditions for a password policy  # noqa: E501
    """
    complexity: UpdatePasswordPolicyRequestComplexity = Field(...)
    age: UpdatePasswordPolicyRequestAge = Field(...)
    lockout: UpdatePasswordPolicyRequestLockout = Field(...)
    __properties = ["complexity", "age", "lockout"]

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
    def from_json(cls, json_str: str) -> UpdatePasswordPolicyRequestConditions:
        """Create an instance of UpdatePasswordPolicyRequestConditions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of complexity
        if self.complexity:
            _dict['complexity'] = self.complexity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of age
        if self.age:
            _dict['age'] = self.age.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lockout
        if self.lockout:
            _dict['lockout'] = self.lockout.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdatePasswordPolicyRequestConditions:
        """Create an instance of UpdatePasswordPolicyRequestConditions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UpdatePasswordPolicyRequestConditions.parse_obj(obj)

        _obj = UpdatePasswordPolicyRequestConditions.parse_obj({
            "complexity": UpdatePasswordPolicyRequestComplexity.from_dict(obj.get("complexity")) if obj.get("complexity") is not None else None,
            "age": UpdatePasswordPolicyRequestAge.from_dict(obj.get("age")) if obj.get("age") is not None else None,
            "lockout": UpdatePasswordPolicyRequestLockout.from_dict(obj.get("lockout")) if obj.get("lockout") is not None else None
        })
        return _obj
