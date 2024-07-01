# coding: utf-8

"""
    FINBOURNE Identity Service API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2974
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


class UpdatePasswordPolicyRequestAge(object):
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
        'max_age_days': 'int',
        'history_count': 'int'
    }

    attribute_map = {
        'max_age_days': 'maxAgeDays',
        'history_count': 'historyCount'
    }

    required_map = {
        'max_age_days': 'required',
        'history_count': 'required'
    }

    def __init__(self, max_age_days=None, history_count=None, local_vars_configuration=None):  # noqa: E501
        """UpdatePasswordPolicyRequestAge - a model defined in OpenAPI"
        
        :param max_age_days:  The maximum age (in days) a password can be before expiring and needing to be changed.  0 indicates no limit (required)
        :type max_age_days: int
        :param history_count:  The number of unique passwords that need to be used before a previous password is permitted again.  0 indicates none (required)
        :type history_count: int

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._max_age_days = None
        self._history_count = None
        self.discriminator = None

        self.max_age_days = max_age_days
        self.history_count = history_count

    @property
    def max_age_days(self):
        """Gets the max_age_days of this UpdatePasswordPolicyRequestAge.  # noqa: E501

        The maximum age (in days) a password can be before expiring and needing to be changed.  0 indicates no limit  # noqa: E501

        :return: The max_age_days of this UpdatePasswordPolicyRequestAge.  # noqa: E501
        :rtype: int
        """
        return self._max_age_days

    @max_age_days.setter
    def max_age_days(self, max_age_days):
        """Sets the max_age_days of this UpdatePasswordPolicyRequestAge.

        The maximum age (in days) a password can be before expiring and needing to be changed.  0 indicates no limit  # noqa: E501

        :param max_age_days: The max_age_days of this UpdatePasswordPolicyRequestAge.  # noqa: E501
        :type max_age_days: int
        """
        if self.local_vars_configuration.client_side_validation and max_age_days is None:  # noqa: E501
            raise ValueError("Invalid value for `max_age_days`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_age_days is not None and max_age_days > 999):  # noqa: E501
            raise ValueError("Invalid value for `max_age_days`, must be a value less than or equal to `999`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                max_age_days is not None and max_age_days < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_age_days`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_age_days = max_age_days

    @property
    def history_count(self):
        """Gets the history_count of this UpdatePasswordPolicyRequestAge.  # noqa: E501

        The number of unique passwords that need to be used before a previous password is permitted again.  0 indicates none  # noqa: E501

        :return: The history_count of this UpdatePasswordPolicyRequestAge.  # noqa: E501
        :rtype: int
        """
        return self._history_count

    @history_count.setter
    def history_count(self, history_count):
        """Sets the history_count of this UpdatePasswordPolicyRequestAge.

        The number of unique passwords that need to be used before a previous password is permitted again.  0 indicates none  # noqa: E501

        :param history_count: The history_count of this UpdatePasswordPolicyRequestAge.  # noqa: E501
        :type history_count: int
        """
        if self.local_vars_configuration.client_side_validation and history_count is None:  # noqa: E501
            raise ValueError("Invalid value for `history_count`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                history_count is not None and history_count > 30):  # noqa: E501
            raise ValueError("Invalid value for `history_count`, must be a value less than or equal to `30`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                history_count is not None and history_count < 0):  # noqa: E501
            raise ValueError("Invalid value for `history_count`, must be a value greater than or equal to `0`")  # noqa: E501

        self._history_count = history_count

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
        if not isinstance(other, UpdatePasswordPolicyRequestAge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdatePasswordPolicyRequestAge):
            return True

        return self.to_dict() != other.to_dict()
