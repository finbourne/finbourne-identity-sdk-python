# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1226
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class CreateApiKey(object):
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
        'display_name': 'str',
        'deactivation_date': 'datetime'
    }

    attribute_map = {
        'display_name': 'displayName',
        'deactivation_date': 'deactivationDate'
    }

    required_map = {
        'display_name': 'required',
        'deactivation_date': 'optional'
    }

    def __init__(self, display_name=None, deactivation_date=None):  # noqa: E501
        """
        CreateApiKey - a model defined in OpenAPI

        :param display_name:  The display name for the API key (required)
        :type display_name: str
        :param deactivation_date:  The optional date at which the key should deactivate
        :type deactivation_date: datetime

        """  # noqa: E501

        self._display_name = None
        self._deactivation_date = None
        self.discriminator = None

        self.display_name = display_name
        self.deactivation_date = deactivation_date

    @property
    def display_name(self):
        """Gets the display_name of this CreateApiKey.  # noqa: E501

        The display name for the API key  # noqa: E501

        :return: The display_name of this CreateApiKey.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateApiKey.

        The display name for the API key  # noqa: E501

        :param display_name: The display_name of this CreateApiKey.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if display_name is not None and len(display_name) > 512:
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `512`")  # noqa: E501
        if display_name is not None and len(display_name) < 1:
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501
        if (display_name is not None and not re.search(r'^[\s\S]*$', display_name)):  # noqa: E501
            raise ValueError(r"Invalid value for `display_name`, must be a follow pattern or equal to `/^[\s\S]*$/`")  # noqa: E501

        self._display_name = display_name

    @property
    def deactivation_date(self):
        """Gets the deactivation_date of this CreateApiKey.  # noqa: E501

        The optional date at which the key should deactivate  # noqa: E501

        :return: The deactivation_date of this CreateApiKey.  # noqa: E501
        :rtype: datetime
        """
        return self._deactivation_date

    @deactivation_date.setter
    def deactivation_date(self, deactivation_date):
        """Sets the deactivation_date of this CreateApiKey.

        The optional date at which the key should deactivate  # noqa: E501

        :param deactivation_date: The deactivation_date of this CreateApiKey.  # noqa: E501
        :type: datetime
        """

        self._deactivation_date = deactivation_date

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
        if not isinstance(other, CreateApiKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
