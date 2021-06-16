# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1238
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AgreementResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'name': 'str',
        'signed_by': 'str',
        'signed_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'signed_by': 'signedBy',
        'signed_at': 'signedAt'
    }

    required_map = {
        'name': 'optional',
        'signed_by': 'optional',
        'signed_at': 'optional'
    }

    def __init__(self, name=None, signed_by=None, signed_at=None):  # noqa: E501
        """
        AgreementResponse - a model defined in OpenAPI

        :param name:  Name of the agreement
        :type name: str
        :param signed_by:  UserID (obfuscated) of the user who signed this agreement
        :type signed_by: str
        :param signed_at:  Datetime at which the agreement was signed
        :type signed_at: datetime

        """  # noqa: E501

        self._name = None
        self._signed_by = None
        self._signed_at = None
        self.discriminator = None

        self.name = name
        self.signed_by = signed_by
        if signed_at is not None:
            self.signed_at = signed_at

    @property
    def name(self):
        """Gets the name of this AgreementResponse.  # noqa: E501

        Name of the agreement  # noqa: E501

        :return: The name of this AgreementResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgreementResponse.

        Name of the agreement  # noqa: E501

        :param name: The name of this AgreementResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def signed_by(self):
        """Gets the signed_by of this AgreementResponse.  # noqa: E501

        UserID (obfuscated) of the user who signed this agreement  # noqa: E501

        :return: The signed_by of this AgreementResponse.  # noqa: E501
        :rtype: str
        """
        return self._signed_by

    @signed_by.setter
    def signed_by(self, signed_by):
        """Sets the signed_by of this AgreementResponse.

        UserID (obfuscated) of the user who signed this agreement  # noqa: E501

        :param signed_by: The signed_by of this AgreementResponse.  # noqa: E501
        :type: str
        """

        self._signed_by = signed_by

    @property
    def signed_at(self):
        """Gets the signed_at of this AgreementResponse.  # noqa: E501

        Datetime at which the agreement was signed  # noqa: E501

        :return: The signed_at of this AgreementResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._signed_at

    @signed_at.setter
    def signed_at(self, signed_at):
        """Sets the signed_at of this AgreementResponse.

        Datetime at which the agreement was signed  # noqa: E501

        :param signed_at: The signed_at of this AgreementResponse.  # noqa: E501
        :type: datetime
        """

        self._signed_at = signed_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AgreementResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
