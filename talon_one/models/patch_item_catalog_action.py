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


class PatchItemCatalogAction(object):
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
        'sku': 'str',
        'price': 'float',
        'attributes': 'object',
        'create_if_not_exists': 'bool'
    }

    attribute_map = {
        'sku': 'sku',
        'price': 'price',
        'attributes': 'attributes',
        'create_if_not_exists': 'createIfNotExists'
    }

    def __init__(self, sku=None, price=None, attributes=None, create_if_not_exists=False, local_vars_configuration=None):  # noqa: E501
        """PatchItemCatalogAction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sku = None
        self._price = None
        self._attributes = None
        self._create_if_not_exists = None
        self.discriminator = None

        self.sku = sku
        if price is not None:
            self.price = price
        if attributes is not None:
            self.attributes = attributes
        if create_if_not_exists is not None:
            self.create_if_not_exists = create_if_not_exists

    @property
    def sku(self):
        """Gets the sku of this PatchItemCatalogAction.  # noqa: E501

        The unique SKU of the item to patch.  # noqa: E501

        :return: The sku of this PatchItemCatalogAction.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this PatchItemCatalogAction.

        The unique SKU of the item to patch.  # noqa: E501

        :param sku: The sku of this PatchItemCatalogAction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sku is None:  # noqa: E501
            raise ValueError("Invalid value for `sku`, must not be `None`")  # noqa: E501

        self._sku = sku

    @property
    def price(self):
        """Gets the price of this PatchItemCatalogAction.  # noqa: E501

        Price of the item.  # noqa: E501

        :return: The price of this PatchItemCatalogAction.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PatchItemCatalogAction.

        Price of the item.  # noqa: E501

        :param price: The price of this PatchItemCatalogAction.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def attributes(self):
        """Gets the attributes of this PatchItemCatalogAction.  # noqa: E501

        The attributes of the item to patch.  # noqa: E501

        :return: The attributes of this PatchItemCatalogAction.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this PatchItemCatalogAction.

        The attributes of the item to patch.  # noqa: E501

        :param attributes: The attributes of this PatchItemCatalogAction.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def create_if_not_exists(self):
        """Gets the create_if_not_exists of this PatchItemCatalogAction.  # noqa: E501

        Indicates whether to create an item if the SKU does not exist.  # noqa: E501

        :return: The create_if_not_exists of this PatchItemCatalogAction.  # noqa: E501
        :rtype: bool
        """
        return self._create_if_not_exists

    @create_if_not_exists.setter
    def create_if_not_exists(self, create_if_not_exists):
        """Sets the create_if_not_exists of this PatchItemCatalogAction.

        Indicates whether to create an item if the SKU does not exist.  # noqa: E501

        :param create_if_not_exists: The create_if_not_exists of this PatchItemCatalogAction.  # noqa: E501
        :type: bool
        """

        self._create_if_not_exists = create_if_not_exists

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
        if not isinstance(other, PatchItemCatalogAction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchItemCatalogAction):
            return True

        return self.to_dict() != other.to_dict()
