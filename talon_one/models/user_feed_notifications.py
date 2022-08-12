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


class UserFeedNotifications(object):
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
        'last_update': 'datetime',
        'notifications': 'list[FeedNotification]'
    }

    attribute_map = {
        'last_update': 'lastUpdate',
        'notifications': 'notifications'
    }

    def __init__(self, last_update=None, notifications=None, local_vars_configuration=None):  # noqa: E501
        """UserFeedNotifications - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._last_update = None
        self._notifications = None
        self.discriminator = None

        self.last_update = last_update
        self.notifications = notifications

    @property
    def last_update(self):
        """Gets the last_update of this UserFeedNotifications.  # noqa: E501

        Timestamp of the last request for this list.  # noqa: E501

        :return: The last_update of this UserFeedNotifications.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this UserFeedNotifications.

        Timestamp of the last request for this list.  # noqa: E501

        :param last_update: The last_update of this UserFeedNotifications.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_update is None:  # noqa: E501
            raise ValueError("Invalid value for `last_update`, must not be `None`")  # noqa: E501

        self._last_update = last_update

    @property
    def notifications(self):
        """Gets the notifications of this UserFeedNotifications.  # noqa: E501

        List of all notifications to notify the user about.  # noqa: E501

        :return: The notifications of this UserFeedNotifications.  # noqa: E501
        :rtype: list[FeedNotification]
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this UserFeedNotifications.

        List of all notifications to notify the user about.  # noqa: E501

        :param notifications: The notifications of this UserFeedNotifications.  # noqa: E501
        :type: list[FeedNotification]
        """
        if self.local_vars_configuration.client_side_validation and notifications is None:  # noqa: E501
            raise ValueError("Invalid value for `notifications`, must not be `None`")  # noqa: E501

        self._notifications = notifications

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
        if not isinstance(other, UserFeedNotifications):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserFeedNotifications):
            return True

        return self.to_dict() != other.to_dict()
