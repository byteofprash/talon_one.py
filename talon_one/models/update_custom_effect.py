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


class UpdateCustomEffect(object):
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
        'application_ids': 'list[int]',
        'name': 'str',
        'title': 'str',
        'payload': 'str',
        'description': 'str',
        'enabled': 'bool',
        'params': 'list[TemplateArgDef]'
    }

    attribute_map = {
        'application_ids': 'applicationIds',
        'name': 'name',
        'title': 'title',
        'payload': 'payload',
        'description': 'description',
        'enabled': 'enabled',
        'params': 'params'
    }

    def __init__(self, application_ids=None, name=None, title=None, payload=None, description=None, enabled=None, params=None, local_vars_configuration=None):  # noqa: E501
        """UpdateCustomEffect - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._application_ids = None
        self._name = None
        self._title = None
        self._payload = None
        self._description = None
        self._enabled = None
        self._params = None
        self.discriminator = None

        self.application_ids = application_ids
        self.name = name
        self.title = title
        self.payload = payload
        if description is not None:
            self.description = description
        self.enabled = enabled
        if params is not None:
            self.params = params

    @property
    def application_ids(self):
        """Gets the application_ids of this UpdateCustomEffect.  # noqa: E501

        The IDs of the applications that are related to this entity.  # noqa: E501

        :return: The application_ids of this UpdateCustomEffect.  # noqa: E501
        :rtype: list[int]
        """
        return self._application_ids

    @application_ids.setter
    def application_ids(self, application_ids):
        """Sets the application_ids of this UpdateCustomEffect.

        The IDs of the applications that are related to this entity.  # noqa: E501

        :param application_ids: The application_ids of this UpdateCustomEffect.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and application_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `application_ids`, must not be `None`")  # noqa: E501

        self._application_ids = application_ids

    @property
    def name(self):
        """Gets the name of this UpdateCustomEffect.  # noqa: E501

        The name of this effect.  # noqa: E501

        :return: The name of this UpdateCustomEffect.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCustomEffect.

        The name of this effect.  # noqa: E501

        :param name: The name of this UpdateCustomEffect.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z](\w|\s)*$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z](\w|\s)*$/`")  # noqa: E501

        self._name = name

    @property
    def title(self):
        """Gets the title of this UpdateCustomEffect.  # noqa: E501

        The title of this effect.  # noqa: E501

        :return: The title of this UpdateCustomEffect.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdateCustomEffect.

        The title of this effect.  # noqa: E501

        :param title: The title of this UpdateCustomEffect.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and not re.search(r'^[^[:cntrl:]\s][^[:cntrl:]]*$', title)):  # noqa: E501
            raise ValueError(r"Invalid value for `title`, must be a follow pattern or equal to `/^[^[:cntrl:]\s][^[:cntrl:]]*$/`")  # noqa: E501

        self._title = title

    @property
    def payload(self):
        """Gets the payload of this UpdateCustomEffect.  # noqa: E501

        The JSON payload of this effect.  # noqa: E501

        :return: The payload of this UpdateCustomEffect.  # noqa: E501
        :rtype: str
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this UpdateCustomEffect.

        The JSON payload of this effect.  # noqa: E501

        :param payload: The payload of this UpdateCustomEffect.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payload is None:  # noqa: E501
            raise ValueError("Invalid value for `payload`, must not be `None`")  # noqa: E501

        self._payload = payload

    @property
    def description(self):
        """Gets the description of this UpdateCustomEffect.  # noqa: E501

        The description of this effect.  # noqa: E501

        :return: The description of this UpdateCustomEffect.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCustomEffect.

        The description of this effect.  # noqa: E501

        :param description: The description of this UpdateCustomEffect.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this UpdateCustomEffect.  # noqa: E501

        Determines if this effect is active.  # noqa: E501

        :return: The enabled of this UpdateCustomEffect.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UpdateCustomEffect.

        Determines if this effect is active.  # noqa: E501

        :param enabled: The enabled of this UpdateCustomEffect.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and enabled is None:  # noqa: E501
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def params(self):
        """Gets the params of this UpdateCustomEffect.  # noqa: E501

        Array of template argument definitions.  # noqa: E501

        :return: The params of this UpdateCustomEffect.  # noqa: E501
        :rtype: list[TemplateArgDef]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this UpdateCustomEffect.

        Array of template argument definitions.  # noqa: E501

        :param params: The params of this UpdateCustomEffect.  # noqa: E501
        :type: list[TemplateArgDef]
        """

        self._params = params

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
        if not isinstance(other, UpdateCustomEffect):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateCustomEffect):
            return True

        return self.to_dict() != other.to_dict()
