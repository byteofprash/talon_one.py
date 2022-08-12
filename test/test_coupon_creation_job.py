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
from talon_one.models.coupon_creation_job import CouponCreationJob  # noqa: E501
from talon_one.rest import ApiException

class TestCouponCreationJob(unittest.TestCase):
    """CouponCreationJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CouponCreationJob
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.coupon_creation_job.CouponCreationJob()  # noqa: E501
        if include_optional :
            return CouponCreationJob(
                id = 6, 
                created = '2020-06-10T09:05:27.993483Z', 
                campaign_id = 211, 
                application_id = 322, 
                account_id = 3886, 
                usage_limit = 100, 
                discount_limit = 30.0, 
                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                number_of_coupons = 200000, 
                coupon_settings = talon_one.models.code_generator_settings.CodeGeneratorSettings(
                    valid_characters = [A, B, C, D, E, 2, 0], 
                    coupon_pattern = 'SUMMER-####-####', ), 
                attributes = None, 
                batch_id = 'tqyrgahe', 
                status = 'pending', 
                created_amount = 1000000, 
                fail_count = 10, 
                errors = [Connection to database was reset, failed to generate enough unique codes, attribute 'PizzaLover' not found on entity 'Coupons'], 
                created_by = 1, 
                communicated = False, 
                chunk_execution_count = 0, 
                chunk_size = 20000
            )
        else :
            return CouponCreationJob(
                id = 6,
                created = '2020-06-10T09:05:27.993483Z',
                campaign_id = 211,
                application_id = 322,
                account_id = 3886,
                usage_limit = 100,
                number_of_coupons = 200000,
                attributes = None,
                batch_id = 'tqyrgahe',
                status = 'pending',
                created_amount = 1000000,
                fail_count = 10,
                errors = [Connection to database was reset, failed to generate enough unique codes, attribute 'PizzaLover' not found on entity 'Coupons'],
                created_by = 1,
                communicated = False,
                chunk_execution_count = 0,
        )

    def testCouponCreationJob(self):
        """Test CouponCreationJob"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
