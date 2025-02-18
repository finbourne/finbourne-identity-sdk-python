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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, constr, validator 

class CreateApiKey(BaseModel):
    """
    Create an API key  # noqa: E501
    """
    display_name:  StrictStr = Field(...,alias="displayName", description="The display name for the API key") 
    deactivation_date: Optional[datetime] = Field(None, alias="deactivationDate", description="The optional date at which the key should deactivate")
    __properties = ["displayName", "deactivationDate"]

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
    def from_json(cls, json_str: str) -> CreateApiKey:
        """Create an instance of CreateApiKey from a JSON string"""
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
    def from_dict(cls, obj: dict) -> CreateApiKey:
        """Create an instance of CreateApiKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateApiKey.parse_obj(obj)

        _obj = CreateApiKey.parse_obj({
            "display_name": obj.get("displayName"),
            "deactivation_date": obj.get("deactivationDate")
        })
        return _obj
