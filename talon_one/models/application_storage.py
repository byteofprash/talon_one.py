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


class ApplicationStorage(object):
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
        'id': 'int',
        'created': 'datetime',
        'modified': 'datetime',
        'application_id': 'int',
        'name': 'str',
        'datatype': 'object',
        'description': 'str',
        'used_at': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'created': 'created',
        'modified': 'modified',
        'application_id': 'applicationId',
        'name': 'name',
        'datatype': 'datatype',
        'description': 'description',
        'used_at': 'usedAt'
    }

    def __init__(self, id=None, created=None, modified=None, application_id=None, name=None, datatype=None, description=None, used_at=None):  # noqa: E501
        """ApplicationStorage - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._created = None
        self._modified = None
        self._application_id = None
        self._name = None
        self._datatype = None
        self._description = None
        self._used_at = None
        self.discriminator = None

        self.id = id
        self.created = created
        self.modified = modified
        self.application_id = application_id
        self.name = name
        self.datatype = datatype
        if description is not None:
            self.description = description
        self.used_at = used_at

    @property
    def id(self):
        """Gets the id of this ApplicationStorage.  # noqa: E501

        Unique ID for this entity.  # noqa: E501

        :return: The id of this ApplicationStorage.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplicationStorage.

        Unique ID for this entity.  # noqa: E501

        :param id: The id of this ApplicationStorage.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created(self):
        """Gets the created of this ApplicationStorage.  # noqa: E501

        The exact moment this entity was created.  # noqa: E501

        :return: The created of this ApplicationStorage.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ApplicationStorage.

        The exact moment this entity was created.  # noqa: E501

        :param created: The created of this ApplicationStorage.  # noqa: E501
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def modified(self):
        """Gets the modified of this ApplicationStorage.  # noqa: E501

        The exact moment this entity was last modified.  # noqa: E501

        :return: The modified of this ApplicationStorage.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this ApplicationStorage.

        The exact moment this entity was last modified.  # noqa: E501

        :param modified: The modified of this ApplicationStorage.  # noqa: E501
        :type: datetime
        """
        if modified is None:
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def application_id(self):
        """Gets the application_id of this ApplicationStorage.  # noqa: E501

        The ID of the application that owns this entity.  # noqa: E501

        :return: The application_id of this ApplicationStorage.  # noqa: E501
        :rtype: int
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ApplicationStorage.

        The ID of the application that owns this entity.  # noqa: E501

        :param application_id: The application_id of this ApplicationStorage.  # noqa: E501
        :type: int
        """
        if application_id is None:
            raise ValueError("Invalid value for `application_id`, must not be `None`")  # noqa: E501

        self._application_id = application_id

    @property
    def name(self):
        """Gets the name of this ApplicationStorage.  # noqa: E501

        Identifier for the information to be saved, e.g. \"Loyalty points for SKU\".  # noqa: E501

        :return: The name of this ApplicationStorage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationStorage.

        Identifier for the information to be saved, e.g. \"Loyalty points for SKU\".  # noqa: E501

        :param name: The name of this ApplicationStorage.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def datatype(self):
        """Gets the datatype of this ApplicationStorage.  # noqa: E501

        A JSON Schema describing the information to be saved in the storage  # noqa: E501

        :return: The datatype of this ApplicationStorage.  # noqa: E501
        :rtype: object
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this ApplicationStorage.

        A JSON Schema describing the information to be saved in the storage  # noqa: E501

        :param datatype: The datatype of this ApplicationStorage.  # noqa: E501
        :type: object
        """
        if datatype is None:
            raise ValueError("Invalid value for `datatype`, must not be `None`")  # noqa: E501

        self._datatype = datatype

    @property
    def description(self):
        """Gets the description of this ApplicationStorage.  # noqa: E501

        Description of the application store  # noqa: E501

        :return: The description of this ApplicationStorage.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApplicationStorage.

        Description of the application store  # noqa: E501

        :param description: The description of this ApplicationStorage.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def used_at(self):
        """Gets the used_at of this ApplicationStorage.  # noqa: E501

        array of rulesets where the application storage is used  # noqa: E501

        :return: The used_at of this ApplicationStorage.  # noqa: E501
        :rtype: list[str]
        """
        return self._used_at

    @used_at.setter
    def used_at(self, used_at):
        """Sets the used_at of this ApplicationStorage.

        array of rulesets where the application storage is used  # noqa: E501

        :param used_at: The used_at of this ApplicationStorage.  # noqa: E501
        :type: list[str]
        """
        if used_at is None:
            raise ValueError("Invalid value for `used_at`, must not be `None`")  # noqa: E501

        self._used_at = used_at

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
        if issubclass(ApplicationStorage, dict):
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
        if not isinstance(other, ApplicationStorage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
