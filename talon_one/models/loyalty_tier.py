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


class LoyaltyTier(object):
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
        'id': 'int',
        'created': 'datetime',
        'program_id': 'int',
        'name': 'str',
        'min_points': 'float'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'program_id': 'programID',
        'name': 'name',
        'min_points': 'minPoints'
    }

    def __init__(self, id=None, created=None, program_id=None, name=None, min_points=None, local_vars_configuration=None):  # noqa: E501
        """LoyaltyTier - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._program_id = None
        self._name = None
        self._min_points = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.program_id = program_id
        self.name = name
        self.min_points = min_points

    @property
    def id(self):
        """Gets the id of this LoyaltyTier.  # noqa: E501

        Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :return: The id of this LoyaltyTier.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoyaltyTier.

        Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :param id: The id of this LoyaltyTier.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this LoyaltyTier.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this LoyaltyTier.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this LoyaltyTier.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this LoyaltyTier.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def program_id(self):
        """Gets the program_id of this LoyaltyTier.  # noqa: E501

        The ID of the loyalty program that owns this entity.  # noqa: E501

        :return: The program_id of this LoyaltyTier.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this LoyaltyTier.

        The ID of the loyalty program that owns this entity.  # noqa: E501

        :param program_id: The program_id of this LoyaltyTier.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and program_id is None:  # noqa: E501
            raise ValueError("Invalid value for `program_id`, must not be `None`")  # noqa: E501

        self._program_id = program_id

    @property
    def name(self):
        """Gets the name of this LoyaltyTier.  # noqa: E501

        The name of the tier  # noqa: E501

        :return: The name of this LoyaltyTier.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoyaltyTier.

        The name of the tier  # noqa: E501

        :param name: The name of this LoyaltyTier.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def min_points(self):
        """Gets the min_points of this LoyaltyTier.  # noqa: E501

        The minimum amount of points required to be eligible for the tier.  # noqa: E501

        :return: The min_points of this LoyaltyTier.  # noqa: E501
        :rtype: float
        """
        return self._min_points

    @min_points.setter
    def min_points(self, min_points):
        """Sets the min_points of this LoyaltyTier.

        The minimum amount of points required to be eligible for the tier.  # noqa: E501

        :param min_points: The min_points of this LoyaltyTier.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and min_points is None:  # noqa: E501
            raise ValueError("Invalid value for `min_points`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_points is not None and min_points > 999999999999.99):  # noqa: E501
            raise ValueError("Invalid value for `min_points`, must be a value less than or equal to `999999999999.99`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                min_points is not None and min_points < 0):  # noqa: E501
            raise ValueError("Invalid value for `min_points`, must be a value greater than or equal to `0`")  # noqa: E501

        self._min_points = min_points

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
        if not isinstance(other, LoyaltyTier):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoyaltyTier):
            return True

        return self.to_dict() != other.to_dict()
