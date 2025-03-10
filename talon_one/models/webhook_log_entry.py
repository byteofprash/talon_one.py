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


class WebhookLogEntry(object):
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
        'id': 'str',
        'integration_request_uuid': 'str',
        'webhook_id': 'int',
        'application_id': 'int',
        'url': 'str',
        'request': 'str',
        'response': 'str',
        'status': 'int',
        'request_time': 'datetime',
        'response_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'integration_request_uuid': 'integrationRequestUuid',
        'webhook_id': 'webhookId',
        'application_id': 'applicationId',
        'url': 'url',
        'request': 'request',
        'response': 'response',
        'status': 'status',
        'request_time': 'requestTime',
        'response_time': 'responseTime'
    }

    def __init__(self, id=None, integration_request_uuid=None, webhook_id=None, application_id=None, url=None, request=None, response=None, status=None, request_time=None, response_time=None, local_vars_configuration=None):  # noqa: E501
        """WebhookLogEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._integration_request_uuid = None
        self._webhook_id = None
        self._application_id = None
        self._url = None
        self._request = None
        self._response = None
        self._status = None
        self._request_time = None
        self._response_time = None
        self.discriminator = None

        self.id = id
        self.integration_request_uuid = integration_request_uuid
        self.webhook_id = webhook_id
        if application_id is not None:
            self.application_id = application_id
        self.url = url
        self.request = request
        if response is not None:
            self.response = response
        if status is not None:
            self.status = status
        self.request_time = request_time
        if response_time is not None:
            self.response_time = response_time

    @property
    def id(self):
        """Gets the id of this WebhookLogEntry.  # noqa: E501

        UUID reference of the webhook request.  # noqa: E501

        :return: The id of this WebhookLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookLogEntry.

        UUID reference of the webhook request.  # noqa: E501

        :param id: The id of this WebhookLogEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def integration_request_uuid(self):
        """Gets the integration_request_uuid of this WebhookLogEntry.  # noqa: E501

        UUID reference of the integration request linked to this webhook request.  # noqa: E501

        :return: The integration_request_uuid of this WebhookLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._integration_request_uuid

    @integration_request_uuid.setter
    def integration_request_uuid(self, integration_request_uuid):
        """Sets the integration_request_uuid of this WebhookLogEntry.

        UUID reference of the integration request linked to this webhook request.  # noqa: E501

        :param integration_request_uuid: The integration_request_uuid of this WebhookLogEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and integration_request_uuid is None:  # noqa: E501
            raise ValueError("Invalid value for `integration_request_uuid`, must not be `None`")  # noqa: E501

        self._integration_request_uuid = integration_request_uuid

    @property
    def webhook_id(self):
        """Gets the webhook_id of this WebhookLogEntry.  # noqa: E501

        ID of the webhook that triggered the request.  # noqa: E501

        :return: The webhook_id of this WebhookLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._webhook_id

    @webhook_id.setter
    def webhook_id(self, webhook_id):
        """Sets the webhook_id of this WebhookLogEntry.

        ID of the webhook that triggered the request.  # noqa: E501

        :param webhook_id: The webhook_id of this WebhookLogEntry.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and webhook_id is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook_id`, must not be `None`")  # noqa: E501

        self._webhook_id = webhook_id

    @property
    def application_id(self):
        """Gets the application_id of this WebhookLogEntry.  # noqa: E501

        ID of the application that triggered the webhook.  # noqa: E501

        :return: The application_id of this WebhookLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this WebhookLogEntry.

        ID of the application that triggered the webhook.  # noqa: E501

        :param application_id: The application_id of this WebhookLogEntry.  # noqa: E501
        :type: int
        """

        self._application_id = application_id

    @property
    def url(self):
        """Gets the url of this WebhookLogEntry.  # noqa: E501

        Target url of request  # noqa: E501

        :return: The url of this WebhookLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookLogEntry.

        Target url of request  # noqa: E501

        :param url: The url of this WebhookLogEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def request(self):
        """Gets the request of this WebhookLogEntry.  # noqa: E501

        Request message  # noqa: E501

        :return: The request of this WebhookLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this WebhookLogEntry.

        Request message  # noqa: E501

        :param request: The request of this WebhookLogEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and request is None:  # noqa: E501
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501

        self._request = request

    @property
    def response(self):
        """Gets the response of this WebhookLogEntry.  # noqa: E501

        Response message  # noqa: E501

        :return: The response of this WebhookLogEntry.  # noqa: E501
        :rtype: str
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this WebhookLogEntry.

        Response message  # noqa: E501

        :param response: The response of this WebhookLogEntry.  # noqa: E501
        :type: str
        """

        self._response = response

    @property
    def status(self):
        """Gets the status of this WebhookLogEntry.  # noqa: E501

        HTTP status code of response.  # noqa: E501

        :return: The status of this WebhookLogEntry.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WebhookLogEntry.

        HTTP status code of response.  # noqa: E501

        :param status: The status of this WebhookLogEntry.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def request_time(self):
        """Gets the request_time of this WebhookLogEntry.  # noqa: E501

        Timestamp of request  # noqa: E501

        :return: The request_time of this WebhookLogEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        """Sets the request_time of this WebhookLogEntry.

        Timestamp of request  # noqa: E501

        :param request_time: The request_time of this WebhookLogEntry.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and request_time is None:  # noqa: E501
            raise ValueError("Invalid value for `request_time`, must not be `None`")  # noqa: E501

        self._request_time = request_time

    @property
    def response_time(self):
        """Gets the response_time of this WebhookLogEntry.  # noqa: E501

        Timestamp of response  # noqa: E501

        :return: The response_time of this WebhookLogEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._response_time

    @response_time.setter
    def response_time(self, response_time):
        """Sets the response_time of this WebhookLogEntry.

        Timestamp of response  # noqa: E501

        :param response_time: The response_time of this WebhookLogEntry.  # noqa: E501
        :type: datetime
        """

        self._response_time = response_time

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
        if not isinstance(other, WebhookLogEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebhookLogEntry):
            return True

        return self.to_dict() != other.to_dict()
