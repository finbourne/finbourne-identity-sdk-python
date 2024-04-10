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
from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator

class OAuthApplication(BaseModel):
    """
    OAuthApplication
    """
    id: constr(strict=True, min_length=1) = Field(...)
    type: constr(strict=True, min_length=1) = Field(...)
    display_name: constr(strict=True, max_length=512, min_length=1) = Field(..., alias="displayName")
    secret: Optional[StrictStr] = None
    client_id: constr(strict=True, min_length=1) = Field(..., alias="clientId")
    issuer: constr(strict=True, min_length=1) = Field(...)
    __properties = ["id", "type", "displayName", "secret", "clientId", "issuer"]

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
    def from_json(cls, json_str: str) -> OAuthApplication:
        """Create an instance of OAuthApplication from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if secret (nullable) is None
        # and __fields_set__ contains the field
        if self.secret is None and "secret" in self.__fields_set__:
            _dict['secret'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OAuthApplication:
        """Create an instance of OAuthApplication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OAuthApplication.parse_obj(obj)

        _obj = OAuthApplication.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "display_name": obj.get("displayName"),
            "secret": obj.get("secret"),
            "client_id": obj.get("clientId"),
            "issuer": obj.get("issuer")
        })
        return _obj
