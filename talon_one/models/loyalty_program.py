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


class LoyaltyProgram(object):
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
        'title': 'str',
        'description': 'str',
        'subscribed_applications': 'list[int]',
        'default_validity': 'str',
        'default_pending': 'str',
        'allow_subledger': 'bool',
        'users_per_card_limit': 'int',
        'account_id': 'int',
        'name': 'str',
        'tiers': 'list[LoyaltyTier]',
        'timezone': 'str',
        'card_based': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'title': 'title',
        'description': 'description',
        'subscribed_applications': 'subscribedApplications',
        'default_validity': 'defaultValidity',
        'default_pending': 'defaultPending',
        'allow_subledger': 'allowSubledger',
        'users_per_card_limit': 'usersPerCardLimit',
        'account_id': 'accountID',
        'name': 'name',
        'tiers': 'tiers',
        'timezone': 'timezone',
        'card_based': 'cardBased'
    }

    def __init__(self, id=None, created=None, title=None, description=None, subscribed_applications=None, default_validity=None, default_pending=None, allow_subledger=None, users_per_card_limit=None, account_id=None, name=None, tiers=None, timezone=None, card_based=False, local_vars_configuration=None):  # noqa: E501
        """LoyaltyProgram - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created = None
        self._title = None
        self._description = None
        self._subscribed_applications = None
        self._default_validity = None
        self._default_pending = None
        self._allow_subledger = None
        self._users_per_card_limit = None
        self._account_id = None
        self._name = None
        self._tiers = None
        self._timezone = None
        self._card_based = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.title = title
        self.description = description
        self.subscribed_applications = subscribed_applications
        self.default_validity = default_validity
        self.default_pending = default_pending
        self.allow_subledger = allow_subledger
        if users_per_card_limit is not None:
            self.users_per_card_limit = users_per_card_limit
        self.account_id = account_id
        self.name = name
        if tiers is not None:
            self.tiers = tiers
        self.timezone = timezone
        self.card_based = card_based

    @property
    def id(self):
        """Gets the id of this LoyaltyProgram.  # noqa: E501

        The ID of loyalty program. Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :return: The id of this LoyaltyProgram.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoyaltyProgram.

        The ID of loyalty program. Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints.  # noqa: E501

        :param id: The id of this LoyaltyProgram.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this LoyaltyProgram.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this LoyaltyProgram.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this LoyaltyProgram.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this LoyaltyProgram.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def title(self):
        """Gets the title of this LoyaltyProgram.  # noqa: E501

        The display title for the Loyalty Program.  # noqa: E501

        :return: The title of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LoyaltyProgram.

        The display title for the Loyalty Program.  # noqa: E501

        :param title: The title of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this LoyaltyProgram.  # noqa: E501

        Description of our Loyalty Program.  # noqa: E501

        :return: The description of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LoyaltyProgram.

        Description of our Loyalty Program.  # noqa: E501

        :param description: The description of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def subscribed_applications(self):
        """Gets the subscribed_applications of this LoyaltyProgram.  # noqa: E501

        A list containing the IDs of all applications that are subscribed to this Loyalty Program.  # noqa: E501

        :return: The subscribed_applications of this LoyaltyProgram.  # noqa: E501
        :rtype: list[int]
        """
        return self._subscribed_applications

    @subscribed_applications.setter
    def subscribed_applications(self, subscribed_applications):
        """Sets the subscribed_applications of this LoyaltyProgram.

        A list containing the IDs of all applications that are subscribed to this Loyalty Program.  # noqa: E501

        :param subscribed_applications: The subscribed_applications of this LoyaltyProgram.  # noqa: E501
        :type: list[int]
        """
        if self.local_vars_configuration.client_side_validation and subscribed_applications is None:  # noqa: E501
            raise ValueError("Invalid value for `subscribed_applications`, must not be `None`")  # noqa: E501

        self._subscribed_applications = subscribed_applications

    @property
    def default_validity(self):
        """Gets the default_validity of this LoyaltyProgram.  # noqa: E501

        Indicates the default duration after which new loyalty points should expire. The format is a number, followed by one letter indicating the unit; like '1h' or '40m'.  # noqa: E501

        :return: The default_validity of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._default_validity

    @default_validity.setter
    def default_validity(self, default_validity):
        """Sets the default_validity of this LoyaltyProgram.

        Indicates the default duration after which new loyalty points should expire. The format is a number, followed by one letter indicating the unit; like '1h' or '40m'.  # noqa: E501

        :param default_validity: The default_validity of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and default_validity is None:  # noqa: E501
            raise ValueError("Invalid value for `default_validity`, must not be `None`")  # noqa: E501

        self._default_validity = default_validity

    @property
    def default_pending(self):
        """Gets the default_pending of this LoyaltyProgram.  # noqa: E501

        Indicates the default duration for the pending time, after which points will be valid. The format is a number followed by a duration unit, like '1h' or '40m'.  # noqa: E501

        :return: The default_pending of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._default_pending

    @default_pending.setter
    def default_pending(self, default_pending):
        """Sets the default_pending of this LoyaltyProgram.

        Indicates the default duration for the pending time, after which points will be valid. The format is a number followed by a duration unit, like '1h' or '40m'.  # noqa: E501

        :param default_pending: The default_pending of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and default_pending is None:  # noqa: E501
            raise ValueError("Invalid value for `default_pending`, must not be `None`")  # noqa: E501

        self._default_pending = default_pending

    @property
    def allow_subledger(self):
        """Gets the allow_subledger of this LoyaltyProgram.  # noqa: E501

        Indicates if this program supports subledgers inside the program.  # noqa: E501

        :return: The allow_subledger of this LoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._allow_subledger

    @allow_subledger.setter
    def allow_subledger(self, allow_subledger):
        """Sets the allow_subledger of this LoyaltyProgram.

        Indicates if this program supports subledgers inside the program.  # noqa: E501

        :param allow_subledger: The allow_subledger of this LoyaltyProgram.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and allow_subledger is None:  # noqa: E501
            raise ValueError("Invalid value for `allow_subledger`, must not be `None`")  # noqa: E501

        self._allow_subledger = allow_subledger

    @property
    def users_per_card_limit(self):
        """Gets the users_per_card_limit of this LoyaltyProgram.  # noqa: E501

        The max amount of user profiles with whom a card can be shared. This can be set to 0 for no limit. This property is only used when `cardBased` is `true`.   # noqa: E501

        :return: The users_per_card_limit of this LoyaltyProgram.  # noqa: E501
        :rtype: int
        """
        return self._users_per_card_limit

    @users_per_card_limit.setter
    def users_per_card_limit(self, users_per_card_limit):
        """Sets the users_per_card_limit of this LoyaltyProgram.

        The max amount of user profiles with whom a card can be shared. This can be set to 0 for no limit. This property is only used when `cardBased` is `true`.   # noqa: E501

        :param users_per_card_limit: The users_per_card_limit of this LoyaltyProgram.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                users_per_card_limit is not None and users_per_card_limit < 0):  # noqa: E501
            raise ValueError("Invalid value for `users_per_card_limit`, must be a value greater than or equal to `0`")  # noqa: E501

        self._users_per_card_limit = users_per_card_limit

    @property
    def account_id(self):
        """Gets the account_id of this LoyaltyProgram.  # noqa: E501

        The ID of the Talon.One account that owns this program.  # noqa: E501

        :return: The account_id of this LoyaltyProgram.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this LoyaltyProgram.

        The ID of the Talon.One account that owns this program.  # noqa: E501

        :param account_id: The account_id of this LoyaltyProgram.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this LoyaltyProgram.  # noqa: E501

        The internal name for the Loyalty Program. This is an immutable value.  # noqa: E501

        :return: The name of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoyaltyProgram.

        The internal name for the Loyalty Program. This is an immutable value.  # noqa: E501

        :param name: The name of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def tiers(self):
        """Gets the tiers of this LoyaltyProgram.  # noqa: E501

        The tiers in this loyalty program.  # noqa: E501

        :return: The tiers of this LoyaltyProgram.  # noqa: E501
        :rtype: list[LoyaltyTier]
        """
        return self._tiers

    @tiers.setter
    def tiers(self, tiers):
        """Sets the tiers of this LoyaltyProgram.

        The tiers in this loyalty program.  # noqa: E501

        :param tiers: The tiers of this LoyaltyProgram.  # noqa: E501
        :type: list[LoyaltyTier]
        """

        self._tiers = tiers

    @property
    def timezone(self):
        """Gets the timezone of this LoyaltyProgram.  # noqa: E501

        A string containing an IANA timezone descriptor.  # noqa: E501

        :return: The timezone of this LoyaltyProgram.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this LoyaltyProgram.

        A string containing an IANA timezone descriptor.  # noqa: E501

        :param timezone: The timezone of this LoyaltyProgram.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and timezone is None:  # noqa: E501
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                timezone is not None and len(timezone) < 1):
            raise ValueError("Invalid value for `timezone`, length must be greater than or equal to `1`")  # noqa: E501

        self._timezone = timezone

    @property
    def card_based(self):
        """Gets the card_based of this LoyaltyProgram.  # noqa: E501

        Defines the type of loyalty program: - `true`: the program is a card-based. - `false`: the program is profile-based.   # noqa: E501

        :return: The card_based of this LoyaltyProgram.  # noqa: E501
        :rtype: bool
        """
        return self._card_based

    @card_based.setter
    def card_based(self, card_based):
        """Sets the card_based of this LoyaltyProgram.

        Defines the type of loyalty program: - `true`: the program is a card-based. - `false`: the program is profile-based.   # noqa: E501

        :param card_based: The card_based of this LoyaltyProgram.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and card_based is None:  # noqa: E501
            raise ValueError("Invalid value for `card_based`, must not be `None`")  # noqa: E501

        self._card_based = card_based

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
        if not isinstance(other, LoyaltyProgram):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoyaltyProgram):
            return True

        return self.to_dict() != other.to_dict()
