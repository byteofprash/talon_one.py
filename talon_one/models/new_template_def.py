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


class NewTemplateDef(object):
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
        'title': 'str',
        'description': 'str',
        'help': 'str',
        'category': 'str',
        'expr': 'list[object]',
        'args': 'list[TemplateArgDef]',
        'expose': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'help': 'help',
        'category': 'category',
        'expr': 'expr',
        'args': 'args',
        'expose': 'expose'
    }

    def __init__(self, title=None, description=None, help=None, category=None, expr=None, args=None, expose=False, local_vars_configuration=None):  # noqa: E501
        """NewTemplateDef - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._title = None
        self._description = None
        self._help = None
        self._category = None
        self._expr = None
        self._args = None
        self._expose = None
        self.discriminator = None

        self.title = title
        if description is not None:
            self.description = description
        if help is not None:
            self.help = help
        self.category = category
        self.expr = expr
        self.args = args
        if expose is not None:
            self.expose = expose

    @property
    def title(self):
        """Gets the title of this NewTemplateDef.  # noqa: E501

        Campaigner-friendly name for the template that will be shown in the rule editor.  # noqa: E501

        :return: The title of this NewTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NewTemplateDef.

        Campaigner-friendly name for the template that will be shown in the rule editor.  # noqa: E501

        :param title: The title of this NewTemplateDef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                title is not None and len(title) < 1):
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this NewTemplateDef.  # noqa: E501

        A short description of the template that will be shown in the rule editor.  # noqa: E501

        :return: The description of this NewTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewTemplateDef.

        A short description of the template that will be shown in the rule editor.  # noqa: E501

        :param description: The description of this NewTemplateDef.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def help(self):
        """Gets the help of this NewTemplateDef.  # noqa: E501

        Extended help text for the template.  # noqa: E501

        :return: The help of this NewTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._help

    @help.setter
    def help(self, help):
        """Sets the help of this NewTemplateDef.

        Extended help text for the template.  # noqa: E501

        :param help: The help of this NewTemplateDef.  # noqa: E501
        :type: str
        """

        self._help = help

    @property
    def category(self):
        """Gets the category of this NewTemplateDef.  # noqa: E501

        Used for grouping templates in the rule editor sidebar.  # noqa: E501

        :return: The category of this NewTemplateDef.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this NewTemplateDef.

        Used for grouping templates in the rule editor sidebar.  # noqa: E501

        :param category: The category of this NewTemplateDef.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) < 1):
            raise ValueError("Invalid value for `category`, length must be greater than or equal to `1`")  # noqa: E501

        self._category = category

    @property
    def expr(self):
        """Gets the expr of this NewTemplateDef.  # noqa: E501

        A Talang expression that contains variable bindings referring to args.  # noqa: E501

        :return: The expr of this NewTemplateDef.  # noqa: E501
        :rtype: list[object]
        """
        return self._expr

    @expr.setter
    def expr(self, expr):
        """Sets the expr of this NewTemplateDef.

        A Talang expression that contains variable bindings referring to args.  # noqa: E501

        :param expr: The expr of this NewTemplateDef.  # noqa: E501
        :type: list[object]
        """
        if self.local_vars_configuration.client_side_validation and expr is None:  # noqa: E501
            raise ValueError("Invalid value for `expr`, must not be `None`")  # noqa: E501

        self._expr = expr

    @property
    def args(self):
        """Gets the args of this NewTemplateDef.  # noqa: E501

        An array of argument definitions.  # noqa: E501

        :return: The args of this NewTemplateDef.  # noqa: E501
        :rtype: list[TemplateArgDef]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this NewTemplateDef.

        An array of argument definitions.  # noqa: E501

        :param args: The args of this NewTemplateDef.  # noqa: E501
        :type: list[TemplateArgDef]
        """
        if self.local_vars_configuration.client_side_validation and args is None:  # noqa: E501
            raise ValueError("Invalid value for `args`, must not be `None`")  # noqa: E501

        self._args = args

    @property
    def expose(self):
        """Gets the expose of this NewTemplateDef.  # noqa: E501

        A flag to control exposure in Rule Builder.  # noqa: E501

        :return: The expose of this NewTemplateDef.  # noqa: E501
        :rtype: bool
        """
        return self._expose

    @expose.setter
    def expose(self, expose):
        """Sets the expose of this NewTemplateDef.

        A flag to control exposure in Rule Builder.  # noqa: E501

        :param expose: The expose of this NewTemplateDef.  # noqa: E501
        :type: bool
        """

        self._expose = expose

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
        if not isinstance(other, NewTemplateDef):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NewTemplateDef):
            return True

        return self.to_dict() != other.to_dict()
