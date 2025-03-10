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
from talon_one.models.loyalty import Loyalty  # noqa: E501
from talon_one.rest import ApiException

class TestLoyalty(unittest.TestCase):
    """Loyalty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Loyalty
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.loyalty.Loyalty()  # noqa: E501
        if include_optional :
            return Loyalty(
                cards = [
                    talon_one.models.loyalty_card.LoyaltyCard(
                        id = 6, 
                        created = '2020-06-10T09:05:27.993483Z', 
                        program_id = 125, 
                        status = '0', 
                        identifier = '0', 
                        users_per_card_limit = 111, 
                        profiles = [
                            talon_one.models.loyalty_card_profile_registration.LoyaltyCardProfileRegistration(
                                integration_id = '0', 
                                timestamp = '2021-09-12T10:12:42Z', )
                            ], 
                        ledger = talon_one.models.ledger_info.LedgerInfo(
                            current_balance = 46.0, 
                            pending_balance = 10.0, 
                            expired_balance = 30.0, 
                            spent_balance = 84.0, 
                            tentative_current_balance = 56.0, 
                            current_tier = talon_one.models.tier.Tier(
                                id = 11, 
                                name = 'bronze', ), 
                            points_to_next_tier = 20.0, 
                            projection = talon_one.models.loyalty_projection.LoyaltyProjection(
                                projections = [
                                    talon_one.models.loyalty_projection_data.LoyaltyProjectionData(
                                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        expiring_points = 14.0, 
                                        activating_points = 25.0, 
                                        projected_balance = 57.0, )
                                    ], 
                                total_expiring_points = 10.0, 
                                total_activating_points = 40.0, ), ), 
                        subledgers = {
                            'key' : talon_one.models.ledger_info.LedgerInfo(
                                current_balance = 46.0, 
                                pending_balance = 10.0, 
                                expired_balance = 30.0, 
                                spent_balance = 84.0, 
                                tentative_current_balance = 56.0, 
                                points_to_next_tier = 20.0, )
                            }, 
                        modified = '2021-09-12T10:12:42Z', )
                    ], 
                programs = {
                    'key' : talon_one.models.loyalty_program_ledgers.LoyaltyProgramLedgers(
                        id = 5, 
                        title = 'My loyalty program', 
                        name = 'program1', 
                        ledger = talon_one.models.ledger_info.LedgerInfo(
                            current_balance = 46.0, 
                            pending_balance = 10.0, 
                            expired_balance = 30.0, 
                            spent_balance = 84.0, 
                            tentative_current_balance = 56.0, 
                            current_tier = talon_one.models.tier.Tier(
                                id = 11, 
                                name = 'bronze', ), 
                            points_to_next_tier = 20.0, 
                            projection = talon_one.models.loyalty_projection.LoyaltyProjection(
                                projections = [
                                    talon_one.models.loyalty_projection_data.LoyaltyProjectionData(
                                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        expiring_points = 14.0, 
                                        activating_points = 25.0, 
                                        projected_balance = 57.0, )
                                    ], 
                                total_expiring_points = 10.0, 
                                total_activating_points = 40.0, ), ), 
                        sub_ledgers = {
                            'key' : talon_one.models.ledger_info.LedgerInfo(
                                current_balance = 46.0, 
                                pending_balance = 10.0, 
                                expired_balance = 30.0, 
                                spent_balance = 84.0, 
                                tentative_current_balance = 56.0, 
                                points_to_next_tier = 20.0, )
                            }, )
                    }
            )
        else :
            return Loyalty(
                programs = {
                    'key' : talon_one.models.loyalty_program_ledgers.LoyaltyProgramLedgers(
                        id = 5, 
                        title = 'My loyalty program', 
                        name = 'program1', 
                        ledger = talon_one.models.ledger_info.LedgerInfo(
                            current_balance = 46.0, 
                            pending_balance = 10.0, 
                            expired_balance = 30.0, 
                            spent_balance = 84.0, 
                            tentative_current_balance = 56.0, 
                            current_tier = talon_one.models.tier.Tier(
                                id = 11, 
                                name = 'bronze', ), 
                            points_to_next_tier = 20.0, 
                            projection = talon_one.models.loyalty_projection.LoyaltyProjection(
                                projections = [
                                    talon_one.models.loyalty_projection_data.LoyaltyProjectionData(
                                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        expiring_points = 14.0, 
                                        activating_points = 25.0, 
                                        projected_balance = 57.0, )
                                    ], 
                                total_expiring_points = 10.0, 
                                total_activating_points = 40.0, ), ), 
                        sub_ledgers = {
                            'key' : talon_one.models.ledger_info.LedgerInfo(
                                current_balance = 46.0, 
                                pending_balance = 10.0, 
                                expired_balance = 30.0, 
                                spent_balance = 84.0, 
                                tentative_current_balance = 56.0, 
                                points_to_next_tier = 20.0, )
                            }, )
                    },
        )

    def testLoyalty(self):
        """Test Loyalty"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
