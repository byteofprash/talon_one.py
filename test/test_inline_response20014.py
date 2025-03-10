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
from talon_one.models.inline_response20014 import InlineResponse20014  # noqa: E501
from talon_one.rest import ApiException

class TestInlineResponse20014(unittest.TestCase):
    """InlineResponse20014 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineResponse20014
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = talon_one.models.inline_response20014.InlineResponse20014()  # noqa: E501
        if include_optional :
            return InlineResponse20014(
                total_result_size = 56, 
                data = [
                    talon_one.models.access_log_entry.AccessLogEntry(
                        uuid = '0', 
                        status = 56, 
                        method = '0', 
                        request_uri = '0', 
                        time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        request_payload = '0', 
                        response_payload = '0', )
                    ]
            )
        else :
            return InlineResponse20014(
                total_result_size = 56,
                data = [
                    talon_one.models.access_log_entry.AccessLogEntry(
                        uuid = '0', 
                        status = 56, 
                        method = '0', 
                        request_uri = '0', 
                        time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        request_payload = '0', 
                        response_payload = '0', )
                    ],
        )

    def testInlineResponse20014(self):
        """Test InlineResponse20014"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
