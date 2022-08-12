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
from talon_one.models.loyalty_ledger_entry import LoyaltyLedgerEntry  # noqa: E501
from talon_one.rest import ApiException

class TestLoyaltyLedgerEntry(unittest.TestCase):
    """LoyaltyLedgerEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoyaltyLedgerEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.loyalty_ledger_entry.LoyaltyLedgerEntry()  # noqa: E501
        if include_optional :
            return LoyaltyLedgerEntry(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                program_id = 56, 
                customer_profile_id = '0', 
                card_id = 56, 
                customer_session_id = '0', 
                event_id = 56, 
                type = '0', 
                amount = 1.337, 
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '0', 
                sub_ledger_id = '0', 
                user_id = 56
            )
        else :
            return LoyaltyLedgerEntry(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                program_id = 56,
                type = '0',
                amount = 1.337,
                name = '0',
                sub_ledger_id = '0',
        )

    def testLoyaltyLedgerEntry(self):
        """Test LoyaltyLedgerEntry"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
