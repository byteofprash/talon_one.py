# coding: utf-8

"""
    Talon.One API

    The Talon.One API is used to manage applications and campaigns, as well as to integrate with your application. The operations in the _Integration API_ section are used to integrate with our platform, while the other operations are used to manage applications and campaigns.  ### Where is the API?  The API is available at the same hostname as these docs. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerProfile][] operation is `https://mycompany.talon.one/v1/customer_profiles/id`  [updateCustomerProfile]: #operation--v1-customer_profiles--integrationId--put   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LoyaltyLedgerEntry(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'created': 'datetime',
        'program_id': 'int',
        'customer_profile_id': 'str',
        'customer_session_id': 'str',
        'event_id': 'int',
        'type': 'str',
        'amount': 'float',
        'expiry_date': 'datetime',
        'name': 'str',
        'sub_ledger_id': 'str'
    }

    attribute_map = {
        'created': 'created',
        'program_id': 'programID',
        'customer_profile_id': 'customerProfileID',
        'customer_session_id': 'customerSessionID',
        'event_id': 'eventID',
        'type': 'type',
        'amount': 'amount',
        'expiry_date': 'expiryDate',
        'name': 'name',
        'sub_ledger_id': 'subLedgerID'
    }

    def __init__(self, created=None, program_id=None, customer_profile_id=None, customer_session_id=None, event_id=None, type=None, amount=None, expiry_date=None, name=None, sub_ledger_id=None):  # noqa: E501
        """LoyaltyLedgerEntry - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._program_id = None
        self._customer_profile_id = None
        self._customer_session_id = None
        self._event_id = None
        self._type = None
        self._amount = None
        self._expiry_date = None
        self._name = None
        self._sub_ledger_id = None
        self.discriminator = None

        self.created = created
        self.program_id = program_id
        self.customer_profile_id = customer_profile_id
        if customer_session_id is not None:
            self.customer_session_id = customer_session_id
        if event_id is not None:
            self.event_id = event_id
        self.type = type
        self.amount = amount
        if expiry_date is not None:
            self.expiry_date = expiry_date
        self.name = name
        self.sub_ledger_id = sub_ledger_id

    @property
    def created(self):
        """Gets the created of this LoyaltyLedgerEntry.  # noqa: E501


        :return: The created of this LoyaltyLedgerEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this LoyaltyLedgerEntry.


        :param created: The created of this LoyaltyLedgerEntry.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def program_id(self):
        """Gets the program_id of this LoyaltyLedgerEntry.  # noqa: E501


        :return: The program_id of this LoyaltyLedgerEntry.  # noqa: E501
        :rtype: int
        """
        return self._program_id

    @program_id.setter
    def program_id(self, program_id):
        """Sets the program_id of this LoyaltyLedgerEntry.


        :param program_id: The program_id of this LoyaltyLedgerEntry.  # noqa: E501
        :type: int
        """
        if program_id is None:
            raise ValueError("Invalid value for `program_id`, must not be `None`")  # noqa: E501

        self._program_id = program_id

    @property
    def customer_profile_id(self):
        """Gets the customer_profile_id of this LoyaltyLedgerEntry.  # noqa: E501


        :return: The customer_profile_id of this LoyaltyLedgerEntry.  # noqa: E501
        :rtype: str
        """
        return self._customer_profile_id

    @customer_profile_id.setter
    def customer_profile_id(self, customer_profile_id):
        """Sets the customer_profile_id of this LoyaltyLedgerEntry.


        :param customer_profile_id: The customer_profile_id of this LoyaltyLedgerEntry.  # noqa: E501
        :type: str
        """
        if customer_profile_id is None:
            raise ValueError("Invalid value for `customer_profile_id`, must not be `None`")  # noqa: E501

        self._customer_profile_id = customer_profile_id

    @property
    def customer_session_id(self):
        """Gets the customer_session_id of this LoyaltyLedgerEntry.  # noqa: E501


        :return: The customer_session_id of this LoyaltyLedgerEntry.  # noqa: E501
        :rtype: str
        """
        return self._customer_session_id

    @customer_session_id.setter
    def customer_session_id(self, customer_session_id):
        """Sets the customer_session_id of this LoyaltyLedgerEntry.


        :param customer_session_id: The customer_session_id of this LoyaltyLedgerEntry.  # noqa: E501
        :type: str
        """

        self._customer_session_id = customer_session_id

    @property
    def event_id(self):
        """Gets the event_id of this LoyaltyLedgerEntry.  # noqa: E501


        :return: The event_id of this LoyaltyLedgerEntry.  # noqa: E501
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this LoyaltyLedgerEntry.


        :param event_id: The event_id of this LoyaltyLedgerEntry.  # noqa: E501
        :type: int
        """

        self._event_id = event_id

    @property
    def type(self):
        """Gets the type of this LoyaltyLedgerEntry.  # noqa: E501


        :return: The type of this LoyaltyLedgerEntry.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LoyaltyLedgerEntry.


        :param type: The type of this LoyaltyLedgerEntry.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["addition", "subtraction"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def amount(self):
        """Gets the amount of this LoyaltyLedgerEntry.  # noqa: E501


        :return: The amount of this LoyaltyLedgerEntry.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this LoyaltyLedgerEntry.


        :param amount: The amount of this LoyaltyLedgerEntry.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def expiry_date(self):
        """Gets the expiry_date of this LoyaltyLedgerEntry.  # noqa: E501


        :return: The expiry_date of this LoyaltyLedgerEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this LoyaltyLedgerEntry.


        :param expiry_date: The expiry_date of this LoyaltyLedgerEntry.  # noqa: E501
        :type: datetime
        """

        self._expiry_date = expiry_date

    @property
    def name(self):
        """Gets the name of this LoyaltyLedgerEntry.  # noqa: E501

        A name referencing the condition or effect that added this entry, or the specific name provided in an API call.  # noqa: E501

        :return: The name of this LoyaltyLedgerEntry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LoyaltyLedgerEntry.

        A name referencing the condition or effect that added this entry, or the specific name provided in an API call.  # noqa: E501

        :param name: The name of this LoyaltyLedgerEntry.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def sub_ledger_id(self):
        """Gets the sub_ledger_id of this LoyaltyLedgerEntry.  # noqa: E501

        This specifies if we are adding loyalty points to the main ledger or a subledger  # noqa: E501

        :return: The sub_ledger_id of this LoyaltyLedgerEntry.  # noqa: E501
        :rtype: str
        """
        return self._sub_ledger_id

    @sub_ledger_id.setter
    def sub_ledger_id(self, sub_ledger_id):
        """Sets the sub_ledger_id of this LoyaltyLedgerEntry.

        This specifies if we are adding loyalty points to the main ledger or a subledger  # noqa: E501

        :param sub_ledger_id: The sub_ledger_id of this LoyaltyLedgerEntry.  # noqa: E501
        :type: str
        """
        if sub_ledger_id is None:
            raise ValueError("Invalid value for `sub_ledger_id`, must not be `None`")  # noqa: E501

        self._sub_ledger_id = sub_ledger_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(LoyaltyLedgerEntry, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LoyaltyLedgerEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
