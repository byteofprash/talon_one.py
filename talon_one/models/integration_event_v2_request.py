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


class IntegrationEventV2Request(object):
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
        'profile_id': 'str',
        'type': 'str',
        'attributes': 'object',
        'response_content': 'list[str]'
    }

    attribute_map = {
        'profile_id': 'profileId',
        'type': 'type',
        'attributes': 'attributes',
        'response_content': 'responseContent'
    }

    def __init__(self, profile_id=None, type=None, attributes=None, response_content=None, local_vars_configuration=None):  # noqa: E501
        """IntegrationEventV2Request - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._profile_id = None
        self._type = None
        self._attributes = None
        self._response_content = None
        self.discriminator = None

        if profile_id is not None:
            self.profile_id = profile_id
        self.type = type
        if attributes is not None:
            self.attributes = attributes
        if response_content is not None:
            self.response_content = response_content

    @property
    def profile_id(self):
        """Gets the profile_id of this IntegrationEventV2Request.  # noqa: E501

        ID of the customer profile set by your integration layer.  **Note:** If the customer does not yet have a known `profileId`, we recommend you use a guest `profileId`.   # noqa: E501

        :return: The profile_id of this IntegrationEventV2Request.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this IntegrationEventV2Request.

        ID of the customer profile set by your integration layer.  **Note:** If the customer does not yet have a known `profileId`, we recommend you use a guest `profileId`.   # noqa: E501

        :param profile_id: The profile_id of this IntegrationEventV2Request.  # noqa: E501
        :type: str
        """

        self._profile_id = profile_id

    @property
    def type(self):
        """Gets the type of this IntegrationEventV2Request.  # noqa: E501

        A string representing the event. Must not be a reserved event name.  # noqa: E501

        :return: The type of this IntegrationEventV2Request.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IntegrationEventV2Request.

        A string representing the event. Must not be a reserved event name.  # noqa: E501

        :param type: The type of this IntegrationEventV2Request.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def attributes(self):
        """Gets the attributes of this IntegrationEventV2Request.  # noqa: E501

        Arbitrary additional JSON data associated with the event.  # noqa: E501

        :return: The attributes of this IntegrationEventV2Request.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this IntegrationEventV2Request.

        Arbitrary additional JSON data associated with the event.  # noqa: E501

        :param attributes: The attributes of this IntegrationEventV2Request.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def response_content(self):
        """Gets the response_content of this IntegrationEventV2Request.  # noqa: E501

        Optional list of requested information to be present on the response related to the tracking custom event.   # noqa: E501

        :return: The response_content of this IntegrationEventV2Request.  # noqa: E501
        :rtype: list[str]
        """
        return self._response_content

    @response_content.setter
    def response_content(self, response_content):
        """Sets the response_content of this IntegrationEventV2Request.

        Optional list of requested information to be present on the response related to the tracking custom event.   # noqa: E501

        :param response_content: The response_content of this IntegrationEventV2Request.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["customerProfile", "triggeredCampaigns", "loyalty", "event", "awardedGiveaways", "ruleFailureReasons"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(response_content).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `response_content` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(response_content) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._response_content = response_content

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
        if not isinstance(other, IntegrationEventV2Request):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegrationEventV2Request):
            return True

        return self.to_dict() != other.to_dict()
