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


class LoyaltyStatistics(object):
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
        'date': 'datetime',
        'total_active_points': 'float',
        'total_pending_points': 'float',
        'total_spent_points': 'float',
        'total_expired_points': 'float',
        'total_members': 'float',
        'new_members': 'float',
        'spent_points': 'LoyaltyDashboardPointsBreakdown',
        'earned_points': 'LoyaltyDashboardPointsBreakdown'
    }

    attribute_map = {
        'date': 'date',
        'total_active_points': 'totalActivePoints',
        'total_pending_points': 'totalPendingPoints',
        'total_spent_points': 'totalSpentPoints',
        'total_expired_points': 'totalExpiredPoints',
        'total_members': 'totalMembers',
        'new_members': 'newMembers',
        'spent_points': 'spentPoints',
        'earned_points': 'earnedPoints'
    }

    def __init__(self, date=None, total_active_points=None, total_pending_points=None, total_spent_points=None, total_expired_points=None, total_members=None, new_members=None, spent_points=None, earned_points=None, local_vars_configuration=None):  # noqa: E501
        """LoyaltyStatistics - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._total_active_points = None
        self._total_pending_points = None
        self._total_spent_points = None
        self._total_expired_points = None
        self._total_members = None
        self._new_members = None
        self._spent_points = None
        self._earned_points = None
        self.discriminator = None

        self.date = date
        self.total_active_points = total_active_points
        self.total_pending_points = total_pending_points
        self.total_spent_points = total_spent_points
        self.total_expired_points = total_expired_points
        self.total_members = total_members
        self.new_members = new_members
        self.spent_points = spent_points
        self.earned_points = earned_points

    @property
    def date(self):
        """Gets the date of this LoyaltyStatistics.  # noqa: E501

        Date at which data point was collected.  # noqa: E501

        :return: The date of this LoyaltyStatistics.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this LoyaltyStatistics.

        Date at which data point was collected.  # noqa: E501

        :param date: The date of this LoyaltyStatistics.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def total_active_points(self):
        """Gets the total_active_points of this LoyaltyStatistics.  # noqa: E501

        Total of active points for this loyalty program.  # noqa: E501

        :return: The total_active_points of this LoyaltyStatistics.  # noqa: E501
        :rtype: float
        """
        return self._total_active_points

    @total_active_points.setter
    def total_active_points(self, total_active_points):
        """Sets the total_active_points of this LoyaltyStatistics.

        Total of active points for this loyalty program.  # noqa: E501

        :param total_active_points: The total_active_points of this LoyaltyStatistics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_active_points is None:  # noqa: E501
            raise ValueError("Invalid value for `total_active_points`, must not be `None`")  # noqa: E501

        self._total_active_points = total_active_points

    @property
    def total_pending_points(self):
        """Gets the total_pending_points of this LoyaltyStatistics.  # noqa: E501

        Total of pending points for this loyalty program.  # noqa: E501

        :return: The total_pending_points of this LoyaltyStatistics.  # noqa: E501
        :rtype: float
        """
        return self._total_pending_points

    @total_pending_points.setter
    def total_pending_points(self, total_pending_points):
        """Sets the total_pending_points of this LoyaltyStatistics.

        Total of pending points for this loyalty program.  # noqa: E501

        :param total_pending_points: The total_pending_points of this LoyaltyStatistics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_pending_points is None:  # noqa: E501
            raise ValueError("Invalid value for `total_pending_points`, must not be `None`")  # noqa: E501

        self._total_pending_points = total_pending_points

    @property
    def total_spent_points(self):
        """Gets the total_spent_points of this LoyaltyStatistics.  # noqa: E501

        Total of spent points for this loyalty program.  # noqa: E501

        :return: The total_spent_points of this LoyaltyStatistics.  # noqa: E501
        :rtype: float
        """
        return self._total_spent_points

    @total_spent_points.setter
    def total_spent_points(self, total_spent_points):
        """Sets the total_spent_points of this LoyaltyStatistics.

        Total of spent points for this loyalty program.  # noqa: E501

        :param total_spent_points: The total_spent_points of this LoyaltyStatistics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_spent_points is None:  # noqa: E501
            raise ValueError("Invalid value for `total_spent_points`, must not be `None`")  # noqa: E501

        self._total_spent_points = total_spent_points

    @property
    def total_expired_points(self):
        """Gets the total_expired_points of this LoyaltyStatistics.  # noqa: E501

        Total of expired points for this loyalty program.  # noqa: E501

        :return: The total_expired_points of this LoyaltyStatistics.  # noqa: E501
        :rtype: float
        """
        return self._total_expired_points

    @total_expired_points.setter
    def total_expired_points(self, total_expired_points):
        """Sets the total_expired_points of this LoyaltyStatistics.

        Total of expired points for this loyalty program.  # noqa: E501

        :param total_expired_points: The total_expired_points of this LoyaltyStatistics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_expired_points is None:  # noqa: E501
            raise ValueError("Invalid value for `total_expired_points`, must not be `None`")  # noqa: E501

        self._total_expired_points = total_expired_points

    @property
    def total_members(self):
        """Gets the total_members of this LoyaltyStatistics.  # noqa: E501

        Number of loyalty program members.  # noqa: E501

        :return: The total_members of this LoyaltyStatistics.  # noqa: E501
        :rtype: float
        """
        return self._total_members

    @total_members.setter
    def total_members(self, total_members):
        """Sets the total_members of this LoyaltyStatistics.

        Number of loyalty program members.  # noqa: E501

        :param total_members: The total_members of this LoyaltyStatistics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and total_members is None:  # noqa: E501
            raise ValueError("Invalid value for `total_members`, must not be `None`")  # noqa: E501

        self._total_members = total_members

    @property
    def new_members(self):
        """Gets the new_members of this LoyaltyStatistics.  # noqa: E501

        Number of members who joined on this day.  # noqa: E501

        :return: The new_members of this LoyaltyStatistics.  # noqa: E501
        :rtype: float
        """
        return self._new_members

    @new_members.setter
    def new_members(self, new_members):
        """Sets the new_members of this LoyaltyStatistics.

        Number of members who joined on this day.  # noqa: E501

        :param new_members: The new_members of this LoyaltyStatistics.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and new_members is None:  # noqa: E501
            raise ValueError("Invalid value for `new_members`, must not be `None`")  # noqa: E501

        self._new_members = new_members

    @property
    def spent_points(self):
        """Gets the spent_points of this LoyaltyStatistics.  # noqa: E501


        :return: The spent_points of this LoyaltyStatistics.  # noqa: E501
        :rtype: LoyaltyDashboardPointsBreakdown
        """
        return self._spent_points

    @spent_points.setter
    def spent_points(self, spent_points):
        """Sets the spent_points of this LoyaltyStatistics.


        :param spent_points: The spent_points of this LoyaltyStatistics.  # noqa: E501
        :type: LoyaltyDashboardPointsBreakdown
        """
        if self.local_vars_configuration.client_side_validation and spent_points is None:  # noqa: E501
            raise ValueError("Invalid value for `spent_points`, must not be `None`")  # noqa: E501

        self._spent_points = spent_points

    @property
    def earned_points(self):
        """Gets the earned_points of this LoyaltyStatistics.  # noqa: E501


        :return: The earned_points of this LoyaltyStatistics.  # noqa: E501
        :rtype: LoyaltyDashboardPointsBreakdown
        """
        return self._earned_points

    @earned_points.setter
    def earned_points(self, earned_points):
        """Sets the earned_points of this LoyaltyStatistics.


        :param earned_points: The earned_points of this LoyaltyStatistics.  # noqa: E501
        :type: LoyaltyDashboardPointsBreakdown
        """
        if self.local_vars_configuration.client_side_validation and earned_points is None:  # noqa: E501
            raise ValueError("Invalid value for `earned_points`, must not be `None`")  # noqa: E501

        self._earned_points = earned_points

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
        if not isinstance(other, LoyaltyStatistics):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoyaltyStatistics):
            return True

        return self.to_dict() != other.to_dict()
