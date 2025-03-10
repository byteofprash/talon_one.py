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


class CampaignTemplateParams(object):
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
        'type': 'str',
        'description': 'str',
        'attribute_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'attribute_id': 'attributeId'
    }

    def __init__(self, name=None, type=None, description=None, attribute_id=None, local_vars_configuration=None):  # noqa: E501
        """CampaignTemplateParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._type = None
        self._description = None
        self._attribute_id = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.description = description
        if attribute_id is not None:
            self.attribute_id = attribute_id

    @property
    def name(self):
        """Gets the name of this CampaignTemplateParams.  # noqa: E501

        Name of the campaign template parameter.  # noqa: E501

        :return: The name of this CampaignTemplateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CampaignTemplateParams.

        Name of the campaign template parameter.  # noqa: E501

        :param name: The name of this CampaignTemplateParams.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this CampaignTemplateParams.  # noqa: E501

        Defines the type of parameter value.  # noqa: E501

        :return: The type of this CampaignTemplateParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CampaignTemplateParams.

        Defines the type of parameter value.  # noqa: E501

        :param type: The type of this CampaignTemplateParams.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["string", "number", "boolean", "percent", "(list string)", "time"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def description(self):
        """Gets the description of this CampaignTemplateParams.  # noqa: E501

        Explains the meaning of this template parameter and the placeholder value that will define it. It is used on campaign creation from this template.  # noqa: E501

        :return: The description of this CampaignTemplateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CampaignTemplateParams.

        Explains the meaning of this template parameter and the placeholder value that will define it. It is used on campaign creation from this template.  # noqa: E501

        :param description: The description of this CampaignTemplateParams.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def attribute_id(self):
        """Gets the attribute_id of this CampaignTemplateParams.  # noqa: E501

        ID of the corresponding attribute.  # noqa: E501

        :return: The attribute_id of this CampaignTemplateParams.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this CampaignTemplateParams.

        ID of the corresponding attribute.  # noqa: E501

        :param attribute_id: The attribute_id of this CampaignTemplateParams.  # noqa: E501
        :type: int
        """

        self._attribute_id = attribute_id

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
        if not isinstance(other, CampaignTemplateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CampaignTemplateParams):
            return True

        return self.to_dict() != other.to_dict()
