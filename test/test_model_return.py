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
from talon_one.models.model_return import ModelReturn  # noqa: E501
from talon_one.rest import ApiException

class TestModelReturn(unittest.TestCase):
    """ModelReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ModelReturn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.model_return.ModelReturn()  # noqa: E501
        if include_optional :
            return ModelReturn(
                id = 6, 
                created = '2020-06-10T09:05:27.993483Z', 
                application_id = 322, 
                account_id = 3886, 
                returned_cart_items = [
                    talon_one.models.returned_cart_item.ReturnedCartItem(
                        position = 2, 
                        quantity = 1, )
                    ], 
                event_id = 123, 
                session_id = 123, 
                session_integration_id = '0c0e0207-eb30-4e06-a56c-2b7c8a64953c', 
                profile_id = 123, 
                profile_integration_id = '0c0e0207-eb30-4e06-a56c-2b7c8a64953c', 
                created_by = 123
            )
        else :
            return ModelReturn(
                id = 6,
                created = '2020-06-10T09:05:27.993483Z',
                application_id = 322,
                account_id = 3886,
                returned_cart_items = [
                    talon_one.models.returned_cart_item.ReturnedCartItem(
                        position = 2, 
                        quantity = 1, )
                    ],
                event_id = 123,
                session_id = 123,
                session_integration_id = '0c0e0207-eb30-4e06-a56c-2b7c8a64953c',
        )

    def testModelReturn(self):
        """Test ModelReturn"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
