# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerSession](https://docs.talon.one/integration-api/#operation/updateCustomerSessionV2) endpoint is `https://mycompany.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from talon_one.configuration import Configuration


class CouponCreatedEffectProps(object):
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
    """
    openapi_types = {
        'value': 'str',
        'profile_id': 'str'
    }

    attribute_map = {
        'value': 'value',
        'profile_id': 'profileId'
    }

    def __init__(self, value=None, profile_id=None, local_vars_configuration=None):  # noqa: E501
        """CouponCreatedEffectProps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._profile_id = None
        self.discriminator = None

        self.value = value
        self.profile_id = profile_id

    @property
    def value(self):
        """Gets the value of this CouponCreatedEffectProps.  # noqa: E501

        The coupon code that was created.  # noqa: E501

        :return: The value of this CouponCreatedEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CouponCreatedEffectProps.

        The coupon code that was created.  # noqa: E501

        :param value: The value of this CouponCreatedEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def profile_id(self):
        """Gets the profile_id of this CouponCreatedEffectProps.  # noqa: E501

        The integration identifier of the customer for whom this coupon was created.  # noqa: E501

        :return: The profile_id of this CouponCreatedEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this CouponCreatedEffectProps.

        The integration identifier of the customer for whom this coupon was created.  # noqa: E501

        :param profile_id: The profile_id of this CouponCreatedEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and profile_id is None:  # noqa: E501
            raise ValueError("Invalid value for `profile_id`, must not be `None`")  # noqa: E501

        self._profile_id = profile_id

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
        if not isinstance(other, CouponCreatedEffectProps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CouponCreatedEffectProps):
            return True

        return self.to_dict() != other.to_dict()
