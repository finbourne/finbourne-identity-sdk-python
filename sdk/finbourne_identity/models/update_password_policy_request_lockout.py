# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2996
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_identity.configuration import Configuration


class UpdatePasswordPolicyRequestLockout(object):
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
        'max_attempts': 'int'
    }

    attribute_map = {
        'max_attempts': 'maxAttempts'
    }

    required_map = {
        'max_attempts': 'required'
    }

    def __init__(self, max_attempts=None, local_vars_configuration=None):  # noqa: E501
        """UpdatePasswordPolicyRequestLockout - a model defined in OpenAPI"
        
        :param max_attempts:  The maximum number of unsuccessful attempts before the user is locked out of their account.  0 indicates no limit (required)
        :type max_attempts: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._max_attempts = None
        self.discriminator = None

        self.max_attempts = max_attempts

    @property
    def max_attempts(self):
        """Gets the max_attempts of this UpdatePasswordPolicyRequestLockout.  # noqa: E501

        The maximum number of unsuccessful attempts before the user is locked out of their account.  0 indicates no limit  # noqa: E501

        :return: The max_attempts of this UpdatePasswordPolicyRequestLockout.  # noqa: E501
        :rtype: int
        """
        return self._max_attempts

    @max_attempts.setter
    def max_attempts(self, max_attempts):
        """Sets the max_attempts of this UpdatePasswordPolicyRequestLockout.

        The maximum number of unsuccessful attempts before the user is locked out of their account.  0 indicates no limit  # noqa: E501

        :param max_attempts: The max_attempts of this UpdatePasswordPolicyRequestLockout.  # noqa: E501
        :type max_attempts: int
        """
        if self.local_vars_configuration.client_side_validation and max_attempts is None:  # noqa: E501
            raise ValueError("Invalid value for `max_attempts`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_attempts is not None and max_attempts > 100):  # noqa: E501
            raise ValueError("Invalid value for `max_attempts`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_attempts is not None and max_attempts < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_attempts`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_attempts = max_attempts

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdatePasswordPolicyRequestLockout):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdatePasswordPolicyRequestLockout):
            return True

        return self.to_dict() != other.to_dict()
