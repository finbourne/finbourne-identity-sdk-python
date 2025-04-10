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
from finbourne_identity.models.log_geolocation import LogGeolocation

class LogGeographicalContext(BaseModel):
    """
    Represents a LogGeographicalContext resource in the Okta API  # noqa: E501
    """
    city:  Optional[StrictStr] = Field(None,alias="city") 
    state:  Optional[StrictStr] = Field(None,alias="state") 
    country:  Optional[StrictStr] = Field(None,alias="country") 
    postal_code:  Optional[StrictStr] = Field(None,alias="postalCode") 
    geolocation: Optional[LogGeolocation] = None
    __properties = ["city", "state", "country", "postalCode", "geolocation"]

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
    def from_json(cls, json_str: str) -> LogGeographicalContext:
        """Create an instance of LogGeographicalContext from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of geolocation
        if self.geolocation:
            _dict['geolocation'] = self.geolocation.to_dict()
        # set to None if city (nullable) is None
        # and __fields_set__ contains the field
        if self.city is None and "city" in self.__fields_set__:
            _dict['city'] = None

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

        # set to None if country (nullable) is None
        # and __fields_set__ contains the field
        if self.country is None and "country" in self.__fields_set__:
            _dict['country'] = None

        # set to None if postal_code (nullable) is None
        # and __fields_set__ contains the field
        if self.postal_code is None and "postal_code" in self.__fields_set__:
            _dict['postalCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LogGeographicalContext:
        """Create an instance of LogGeographicalContext from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LogGeographicalContext.parse_obj(obj)

        _obj = LogGeographicalContext.parse_obj({
            "city": obj.get("city"),
            "state": obj.get("state"),
            "country": obj.get("country"),
            "postal_code": obj.get("postalCode"),
            "geolocation": LogGeolocation.from_dict(obj.get("geolocation")) if obj.get("geolocation") is not None else None
        })
        return _obj
