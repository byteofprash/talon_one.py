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


class SetDiscountPerItemEffectProps(object):
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
        'value': 'float',
        'position': 'float',
        'sub_position': 'float',
        'desired_value': 'float',
        'scope': 'str',
        'total_discount': 'float',
        'desired_total_discount': 'float',
        'bundle_index': 'int',
        'bundle_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'position': 'position',
        'sub_position': 'subPosition',
        'desired_value': 'desiredValue',
        'scope': 'scope',
        'total_discount': 'totalDiscount',
        'desired_total_discount': 'desiredTotalDiscount',
        'bundle_index': 'bundleIndex',
        'bundle_name': 'bundleName'
    }

    def __init__(self, name=None, value=None, position=None, sub_position=None, desired_value=None, scope=None, total_discount=None, desired_total_discount=None, bundle_index=None, bundle_name=None, local_vars_configuration=None):  # noqa: E501
        """SetDiscountPerItemEffectProps - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._value = None
        self._position = None
        self._sub_position = None
        self._desired_value = None
        self._scope = None
        self._total_discount = None
        self._desired_total_discount = None
        self._bundle_index = None
        self._bundle_name = None
        self.discriminator = None

        self.name = name
        self.value = value
        self.position = position
        if sub_position is not None:
            self.sub_position = sub_position
        if desired_value is not None:
            self.desired_value = desired_value
        if scope is not None:
            self.scope = scope
        if total_discount is not None:
            self.total_discount = total_discount
        if desired_total_discount is not None:
            self.desired_total_discount = desired_total_discount
        if bundle_index is not None:
            self.bundle_index = bundle_index
        if bundle_name is not None:
            self.bundle_name = bundle_name

    @property
    def name(self):
        """Gets the name of this SetDiscountPerItemEffectProps.  # noqa: E501

        The name of the discount. Contains a hashtag character indicating the index of the position of the item the discount applies to. It is identical to the value of the `position` property.   # noqa: E501

        :return: The name of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SetDiscountPerItemEffectProps.

        The name of the discount. Contains a hashtag character indicating the index of the position of the item the discount applies to. It is identical to the value of the `position` property.   # noqa: E501

        :param name: The name of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this SetDiscountPerItemEffectProps.  # noqa: E501

        The total monetary value of the discount.  # noqa: E501

        :return: The value of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SetDiscountPerItemEffectProps.

        The total monetary value of the discount.  # noqa: E501

        :param value: The value of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def position(self):
        """Gets the position of this SetDiscountPerItemEffectProps.  # noqa: E501

        The index of the item in the cart items list on which this discount should be applied.  # noqa: E501

        :return: The position of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this SetDiscountPerItemEffectProps.

        The index of the item in the cart items list on which this discount should be applied.  # noqa: E501

        :param position: The position of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and position is None:  # noqa: E501
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def sub_position(self):
        """Gets the sub_position of this SetDiscountPerItemEffectProps.  # noqa: E501

        Only used when [cart item flattening](https://docs.talon.one/docs/product/campaigns/campaign-evaluation/#flattened-cart-items) is enabled. Indicates which item the discount applies to for cart items with `quantity` > 1.   # noqa: E501

        :return: The sub_position of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._sub_position

    @sub_position.setter
    def sub_position(self, sub_position):
        """Sets the sub_position of this SetDiscountPerItemEffectProps.

        Only used when [cart item flattening](https://docs.talon.one/docs/product/campaigns/campaign-evaluation/#flattened-cart-items) is enabled. Indicates which item the discount applies to for cart items with `quantity` > 1.   # noqa: E501

        :param sub_position: The sub_position of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: float
        """

        self._sub_position = sub_position

    @property
    def desired_value(self):
        """Gets the desired_value of this SetDiscountPerItemEffectProps.  # noqa: E501

        The original value of the discount.  # noqa: E501

        :return: The desired_value of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._desired_value

    @desired_value.setter
    def desired_value(self, desired_value):
        """Sets the desired_value of this SetDiscountPerItemEffectProps.

        The original value of the discount.  # noqa: E501

        :param desired_value: The desired_value of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: float
        """

        self._desired_value = desired_value

    @property
    def scope(self):
        """Gets the scope of this SetDiscountPerItemEffectProps.  # noqa: E501

        The scope of the discount: - `additionalCosts`: The discount applies to all the additional costs of the item. - `itemTotal`: The discount applies to the price of the item + the additional costs of the item. - `price`: The discount applies to the price of the item.   # noqa: E501

        :return: The scope of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this SetDiscountPerItemEffectProps.

        The scope of the discount: - `additionalCosts`: The discount applies to all the additional costs of the item. - `itemTotal`: The discount applies to the price of the item + the additional costs of the item. - `price`: The discount applies to the price of the item.   # noqa: E501

        :param scope: The scope of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: str
        """

        self._scope = scope

    @property
    def total_discount(self):
        """Gets the total_discount of this SetDiscountPerItemEffectProps.  # noqa: E501

        The total discount given if this effect is a result of a prorated discount.  # noqa: E501

        :return: The total_discount of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._total_discount

    @total_discount.setter
    def total_discount(self, total_discount):
        """Sets the total_discount of this SetDiscountPerItemEffectProps.

        The total discount given if this effect is a result of a prorated discount.  # noqa: E501

        :param total_discount: The total_discount of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: float
        """

        self._total_discount = total_discount

    @property
    def desired_total_discount(self):
        """Gets the desired_total_discount of this SetDiscountPerItemEffectProps.  # noqa: E501

        The original total discount to give if this effect is a result of a prorated discount.  # noqa: E501

        :return: The desired_total_discount of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: float
        """
        return self._desired_total_discount

    @desired_total_discount.setter
    def desired_total_discount(self, desired_total_discount):
        """Sets the desired_total_discount of this SetDiscountPerItemEffectProps.

        The original total discount to give if this effect is a result of a prorated discount.  # noqa: E501

        :param desired_total_discount: The desired_total_discount of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: float
        """

        self._desired_total_discount = desired_total_discount

    @property
    def bundle_index(self):
        """Gets the bundle_index of this SetDiscountPerItemEffectProps.  # noqa: E501

        The position of the bundle in a list of item bundles created from the same bundle definition.  # noqa: E501

        :return: The bundle_index of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: int
        """
        return self._bundle_index

    @bundle_index.setter
    def bundle_index(self, bundle_index):
        """Sets the bundle_index of this SetDiscountPerItemEffectProps.

        The position of the bundle in a list of item bundles created from the same bundle definition.  # noqa: E501

        :param bundle_index: The bundle_index of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: int
        """

        self._bundle_index = bundle_index

    @property
    def bundle_name(self):
        """Gets the bundle_name of this SetDiscountPerItemEffectProps.  # noqa: E501

        The name of the bundle binding.  # noqa: E501

        :return: The bundle_name of this SetDiscountPerItemEffectProps.  # noqa: E501
        :rtype: str
        """
        return self._bundle_name

    @bundle_name.setter
    def bundle_name(self, bundle_name):
        """Sets the bundle_name of this SetDiscountPerItemEffectProps.

        The name of the bundle binding.  # noqa: E501

        :param bundle_name: The bundle_name of this SetDiscountPerItemEffectProps.  # noqa: E501
        :type: str
        """

        self._bundle_name = bundle_name

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
        if not isinstance(other, SetDiscountPerItemEffectProps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SetDiscountPerItemEffectProps):
            return True

        return self.to_dict() != other.to_dict()
