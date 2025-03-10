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


class UpdateRole(object):
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
        'name': 'str',
        'description': 'str',
        'acl': 'str',
        'members': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'acl': 'acl',
        'members': 'members'
    }

    def __init__(self, name=None, description=None, acl=None, members=None, local_vars_configuration=None):  # noqa: E501
        """UpdateRole - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._acl = None
        self._members = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if acl is not None:
            self.acl = acl
        if members is not None:
            self.members = members

    @property
    def name(self):
        """Gets the name of this UpdateRole.  # noqa: E501

        Name of the role.  # noqa: E501

        :return: The name of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateRole.

        Name of the role.  # noqa: E501

        :param name: The name of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateRole.  # noqa: E501

        Description of the role.  # noqa: E501

        :return: The description of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateRole.

        Description of the role.  # noqa: E501

        :param description: The description of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def acl(self):
        """Gets the acl of this UpdateRole.  # noqa: E501

        Role Policy this should be a stringified blob of json.  # noqa: E501

        :return: The acl of this UpdateRole.  # noqa: E501
        :rtype: str
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this UpdateRole.

        Role Policy this should be a stringified blob of json.  # noqa: E501

        :param acl: The acl of this UpdateRole.  # noqa: E501
        :type: str
        """

        self._acl = acl

    @property
    def members(self):
        """Gets the members of this UpdateRole.  # noqa: E501

        An array of user identifiers.  # noqa: E501

        :return: The members of this UpdateRole.  # noqa: E501
        :rtype: list[int]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this UpdateRole.

        An array of user identifiers.  # noqa: E501

        :param members: The members of this UpdateRole.  # noqa: E501
        :type: list[int]
        """

        self._members = members

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
        if not isinstance(other, UpdateRole):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateRole):
            return True

        return self.to_dict() != other.to_dict()
