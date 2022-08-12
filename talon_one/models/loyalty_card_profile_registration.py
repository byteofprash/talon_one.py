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


class LoyaltyCardProfileRegistration(object):
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
        'integration_id': 'str',
        'timestamp': 'datetime'
    }

    attribute_map = {
        'integration_id': 'integrationId',
        'timestamp': 'timestamp'
    }

    def __init__(self, integration_id=None, timestamp=None, local_vars_configuration=None):  # noqa: E501
        """LoyaltyCardProfileRegistration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._integration_id = None
        self._timestamp = None
        self.discriminator = None

        self.integration_id = integration_id
        self.timestamp = timestamp

    @property
    def integration_id(self):
        """Gets the integration_id of this LoyaltyCardProfileRegistration.  # noqa: E501

        Integration ID of the customer associated with the card.  # noqa: E501

        :return: The integration_id of this LoyaltyCardProfileRegistration.  # noqa: E501
        :rtype: str
        """
        return self._integration_id

    @integration_id.setter
    def integration_id(self, integration_id):
        """Sets the integration_id of this LoyaltyCardProfileRegistration.

        Integration ID of the customer associated with the card.  # noqa: E501

        :param integration_id: The integration_id of this LoyaltyCardProfileRegistration.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and integration_id is None:  # noqa: E501
            raise ValueError("Invalid value for `integration_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                integration_id is not None and len(integration_id) > 1000):
            raise ValueError("Invalid value for `integration_id`, length must be less than or equal to `1000`")  # noqa: E501

        self._integration_id = integration_id

    @property
    def timestamp(self):
        """Gets the timestamp of this LoyaltyCardProfileRegistration.  # noqa: E501

        Timestamp of the registration to the card.  # noqa: E501

        :return: The timestamp of this LoyaltyCardProfileRegistration.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this LoyaltyCardProfileRegistration.

        Timestamp of the registration to the card.  # noqa: E501

        :param timestamp: The timestamp of this LoyaltyCardProfileRegistration.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

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
        if not isinstance(other, LoyaltyCardProfileRegistration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoyaltyCardProfileRegistration):
            return True

        return self.to_dict() != other.to_dict()
