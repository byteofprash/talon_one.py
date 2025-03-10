# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerSession](https://docs.talon.one/integration-api/#operation/updateCustomerSessionV2) endpoint is `https://mycompany.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import talon_one
from talon_one.models.add_loyalty_points_effect_props import AddLoyaltyPointsEffectProps  # noqa: E501
from talon_one.rest import ApiException

class TestAddLoyaltyPointsEffectProps(unittest.TestCase):
    """AddLoyaltyPointsEffectProps unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AddLoyaltyPointsEffectProps
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.add_loyalty_points_effect_props.AddLoyaltyPointsEffectProps()  # noqa: E501
        if include_optional :
            return AddLoyaltyPointsEffectProps(
                name = '0', 
                program_id = 56, 
                sub_ledger_id = '0', 
                value = 1.337, 
                desired_value = 1.337, 
                recipient_integration_id = '0', 
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                transaction_uuid = '0', 
                cart_item_position = 1.337, 
                cart_item_sub_position = 1.337, 
                card_identifier = '0'
            )
        else :
            return AddLoyaltyPointsEffectProps(
                name = '0',
                program_id = 56,
                sub_ledger_id = '0',
                value = 1.337,
                recipient_integration_id = '0',
                transaction_uuid = '0',
        )

    def testAddLoyaltyPointsEffectProps(self):
        """Test AddLoyaltyPointsEffectProps"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
