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


class CustomerProfileSearchQuery(object):
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
        'attributes': 'object',
        'integration_i_ds': 'list[str]',
        'profile_i_ds': 'list[int]'
    }

    attribute_map = {
        'attributes': 'attributes',
        'integration_i_ds': 'integrationIDs',
        'profile_i_ds': 'profileIDs'
    }

    def __init__(self, attributes=None, integration_i_ds=None, profile_i_ds=None, local_vars_configuration=None):  # noqa: E501
        """CustomerProfileSearchQuery - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attributes = None
        self._integration_i_ds = None
        self._profile_i_ds = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if integration_i_ds is not None:
            self.integration_i_ds = integration_i_ds
        if profile_i_ds is not None:
            self.profile_i_ds = profile_i_ds

    @property
    def attributes(self):
        """Gets the attributes of this CustomerProfileSearchQuery.  # noqa: E501

        Properties to match against a customer profile. All provided attributes will be exactly matched against profile attributes.  # noqa: E501

        :return: The attributes of this CustomerProfileSearchQuery.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CustomerProfileSearchQuery.

        Properties to match against a customer profile. All provided attributes will be exactly matched against profile attributes.  # noqa: E501

        :param attributes: The attributes of this CustomerProfileSearchQuery.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def integration_i_ds(self):
        """Gets the integration_i_ds of this CustomerProfileSearchQuery.  # noqa: E501


        :return: The integration_i_ds of this CustomerProfileSearchQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._integration_i_ds

    @integration_i_ds.setter
    def integration_i_ds(self, integration_i_ds):
        """Sets the integration_i_ds of this CustomerProfileSearchQuery.


        :param integration_i_ds: The integration_i_ds of this CustomerProfileSearchQuery.  # noqa: E501
        :type: list[str]
        """

        self._integration_i_ds = integration_i_ds

    @property
    def profile_i_ds(self):
        """Gets the profile_i_ds of this CustomerProfileSearchQuery.  # noqa: E501


        :return: The profile_i_ds of this CustomerProfileSearchQuery.  # noqa: E501
        :rtype: list[int]
        """
        return self._profile_i_ds

    @profile_i_ds.setter
    def profile_i_ds(self, profile_i_ds):
        """Sets the profile_i_ds of this CustomerProfileSearchQuery.


        :param profile_i_ds: The profile_i_ds of this CustomerProfileSearchQuery.  # noqa: E501
        :type: list[int]
        """

        self._profile_i_ds = profile_i_ds

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
        if not isinstance(other, CustomerProfileSearchQuery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CustomerProfileSearchQuery):
            return True

        return self.to_dict() != other.to_dict()
