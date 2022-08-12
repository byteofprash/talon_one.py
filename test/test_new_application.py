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
from talon_one.models.new_application import NewApplication  # noqa: E501
from talon_one.rest import ApiException

class TestNewApplication(unittest.TestCase):
    """NewApplication unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test NewApplication
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.new_application.NewApplication()  # noqa: E501
        if include_optional :
            return NewApplication(
                name = 'My Application', 
                description = 'A test Application', 
                timezone = 'Europe/Berlin', 
                currency = 'EUR', 
                case_sensitivity = 'sensitive', 
                attributes = None, 
                limits = [
                    talon_one.models.limit_config.LimitConfig(
                        action = 'createCoupon', 
                        limit = 1000.0, 
                        period = 'yearly', 
                        entities = [Coupon], )
                    ], 
                campaign_priority = 'universal', 
                exclusive_campaigns_strategy = 'listOrder', 
                default_discount_scope = 'sessionTotal', 
                enable_cascading_discounts = True, 
                enable_flattened_cart_items = True, 
                attributes_settings = talon_one.models.attributes_settings.AttributesSettings(
                    mandatory = talon_one.models.attributes_mandatory.AttributesMandatory(
                        campaigns = [
                            '0'
                            ], 
                        coupons = [
                            '0'
                            ], ), ), 
                sandbox = True, 
                enable_partial_discounts = False, 
                default_discount_additional_cost_per_item_scope = 'price', 
                key = 'a'
            )
        else :
            return NewApplication(
                name = 'My Application',
                timezone = 'Europe/Berlin',
                currency = 'EUR',
        )

    def testNewApplication(self):
        """Test NewApplication"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
