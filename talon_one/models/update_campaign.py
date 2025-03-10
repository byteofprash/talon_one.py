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


class UpdateCampaign(object):
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
        'description': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'attributes': 'object',
        'state': 'str',
        'active_ruleset_id': 'int',
        'tags': 'list[str]',
        'features': 'list[str]',
        'coupon_settings': 'CodeGeneratorSettings',
        'referral_settings': 'CodeGeneratorSettings',
        'limits': 'list[LimitConfig]',
        'campaign_groups': 'list[int]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'attributes': 'attributes',
        'state': 'state',
        'active_ruleset_id': 'activeRulesetId',
        'tags': 'tags',
        'features': 'features',
        'coupon_settings': 'couponSettings',
        'referral_settings': 'referralSettings',
        'limits': 'limits',
        'campaign_groups': 'campaignGroups'
    }

    def __init__(self, name=None, description=None, start_time=None, end_time=None, attributes=None, state='enabled', active_ruleset_id=None, tags=None, features=None, coupon_settings=None, referral_settings=None, limits=None, campaign_groups=None, local_vars_configuration=None):  # noqa: E501
        """UpdateCampaign - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._start_time = None
        self._end_time = None
        self._attributes = None
        self._state = None
        self._active_ruleset_id = None
        self._tags = None
        self._features = None
        self._coupon_settings = None
        self._referral_settings = None
        self._limits = None
        self._campaign_groups = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if attributes is not None:
            self.attributes = attributes
        if state is not None:
            self.state = state
        if active_ruleset_id is not None:
            self.active_ruleset_id = active_ruleset_id
        self.tags = tags
        self.features = features
        if coupon_settings is not None:
            self.coupon_settings = coupon_settings
        if referral_settings is not None:
            self.referral_settings = referral_settings
        self.limits = limits
        if campaign_groups is not None:
            self.campaign_groups = campaign_groups

    @property
    def name(self):
        """Gets the name of this UpdateCampaign.  # noqa: E501

        A user-facing name for this campaign.  # noqa: E501

        :return: The name of this UpdateCampaign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateCampaign.

        A user-facing name for this campaign.  # noqa: E501

        :param name: The name of this UpdateCampaign.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateCampaign.  # noqa: E501

        A detailed description of the campaign.  # noqa: E501

        :return: The description of this UpdateCampaign.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateCampaign.

        A detailed description of the campaign.  # noqa: E501

        :param description: The description of this UpdateCampaign.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def start_time(self):
        """Gets the start_time of this UpdateCampaign.  # noqa: E501

        Timestamp when the campaign will become active.  # noqa: E501

        :return: The start_time of this UpdateCampaign.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this UpdateCampaign.

        Timestamp when the campaign will become active.  # noqa: E501

        :param start_time: The start_time of this UpdateCampaign.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this UpdateCampaign.  # noqa: E501

        Timestamp when the campaign will become inactive.  # noqa: E501

        :return: The end_time of this UpdateCampaign.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this UpdateCampaign.

        Timestamp when the campaign will become inactive.  # noqa: E501

        :param end_time: The end_time of this UpdateCampaign.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def attributes(self):
        """Gets the attributes of this UpdateCampaign.  # noqa: E501

        Arbitrary properties associated with this campaign.  # noqa: E501

        :return: The attributes of this UpdateCampaign.  # noqa: E501
        :rtype: object
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this UpdateCampaign.

        Arbitrary properties associated with this campaign.  # noqa: E501

        :param attributes: The attributes of this UpdateCampaign.  # noqa: E501
        :type: object
        """

        self._attributes = attributes

    @property
    def state(self):
        """Gets the state of this UpdateCampaign.  # noqa: E501

        A disabled or archived campaign is not evaluated for rules or coupons.   # noqa: E501

        :return: The state of this UpdateCampaign.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this UpdateCampaign.

        A disabled or archived campaign is not evaluated for rules or coupons.   # noqa: E501

        :param state: The state of this UpdateCampaign.  # noqa: E501
        :type: str
        """
        allowed_values = ["enabled", "disabled", "archived"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def active_ruleset_id(self):
        """Gets the active_ruleset_id of this UpdateCampaign.  # noqa: E501

        ID of Ruleset this campaign applies on customer session evaluation.  # noqa: E501

        :return: The active_ruleset_id of this UpdateCampaign.  # noqa: E501
        :rtype: int
        """
        return self._active_ruleset_id

    @active_ruleset_id.setter
    def active_ruleset_id(self, active_ruleset_id):
        """Sets the active_ruleset_id of this UpdateCampaign.

        ID of Ruleset this campaign applies on customer session evaluation.  # noqa: E501

        :param active_ruleset_id: The active_ruleset_id of this UpdateCampaign.  # noqa: E501
        :type: int
        """

        self._active_ruleset_id = active_ruleset_id

    @property
    def tags(self):
        """Gets the tags of this UpdateCampaign.  # noqa: E501

        A list of tags for the campaign.  # noqa: E501

        :return: The tags of this UpdateCampaign.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateCampaign.

        A list of tags for the campaign.  # noqa: E501

        :param tags: The tags of this UpdateCampaign.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and tags is None:  # noqa: E501
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

    @property
    def features(self):
        """Gets the features of this UpdateCampaign.  # noqa: E501

        A list of features for the campaign.  # noqa: E501

        :return: The features of this UpdateCampaign.  # noqa: E501
        :rtype: list[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this UpdateCampaign.

        A list of features for the campaign.  # noqa: E501

        :param features: The features of this UpdateCampaign.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and features is None:  # noqa: E501
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501
        allowed_values = ["coupons", "referrals", "loyalty", "giveaways"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(features).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `features` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(features) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._features = features

    @property
    def coupon_settings(self):
        """Gets the coupon_settings of this UpdateCampaign.  # noqa: E501


        :return: The coupon_settings of this UpdateCampaign.  # noqa: E501
        :rtype: CodeGeneratorSettings
        """
        return self._coupon_settings

    @coupon_settings.setter
    def coupon_settings(self, coupon_settings):
        """Sets the coupon_settings of this UpdateCampaign.


        :param coupon_settings: The coupon_settings of this UpdateCampaign.  # noqa: E501
        :type: CodeGeneratorSettings
        """

        self._coupon_settings = coupon_settings

    @property
    def referral_settings(self):
        """Gets the referral_settings of this UpdateCampaign.  # noqa: E501


        :return: The referral_settings of this UpdateCampaign.  # noqa: E501
        :rtype: CodeGeneratorSettings
        """
        return self._referral_settings

    @referral_settings.setter
    def referral_settings(self, referral_settings):
        """Sets the referral_settings of this UpdateCampaign.


        :param referral_settings: The referral_settings of this UpdateCampaign.  # noqa: E501
        :type: CodeGeneratorSettings
        """

        self._referral_settings = referral_settings

    @property
    def limits(self):
        """Gets the limits of this UpdateCampaign.  # noqa: E501

        The set of limits that will operate for this campaign.  # noqa: E501

        :return: The limits of this UpdateCampaign.  # noqa: E501
        :rtype: list[LimitConfig]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """Sets the limits of this UpdateCampaign.

        The set of limits that will operate for this campaign.  # noqa: E501

        :param limits: The limits of this UpdateCampaign.  # noqa: E501
        :type: list[LimitConfig]
        """
        if self.local_vars_configuration.client_side_validation and limits is None:  # noqa: E501
            raise ValueError("Invalid value for `limits`, must not be `None`")  # noqa: E501

        self._limits = limits

    @property
    def campaign_groups(self):
        """Gets the campaign_groups of this UpdateCampaign.  # noqa: E501

        The IDs of the campaign groups that own this entity.  # noqa: E501

        :return: The campaign_groups of this UpdateCampaign.  # noqa: E501
        :rtype: list[int]
        """
        return self._campaign_groups

    @campaign_groups.setter
    def campaign_groups(self, campaign_groups):
        """Sets the campaign_groups of this UpdateCampaign.

        The IDs of the campaign groups that own this entity.  # noqa: E501

        :param campaign_groups: The campaign_groups of this UpdateCampaign.  # noqa: E501
        :type: list[int]
        """

        self._campaign_groups = campaign_groups

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
        if not isinstance(other, UpdateCampaign):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateCampaign):
            return True

        return self.to_dict() != other.to_dict()
