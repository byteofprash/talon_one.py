# coding: utf-8

"""
    Talon.One API

    Use the Talon.One API to integrate with your application and to manage applications and campaigns:  - Use the operations in the [Integration API section](#integration-api) are used to integrate with our platform - Use the operation in the [Management API section](#management-api) to manage applications and campaigns.  ## Determining the base URL of the endpoints  The API is available at the same hostname as your Campaign Manager deployment. For example, if you are reading this page at `https://mycompany.talon.one/docs/api/`, the URL for the [updateCustomerSession](https://docs.talon.one/integration-api/#operation/updateCustomerSessionV2) endpoint is `https://mycompany.talon.one/v2/customer_sessions/{Id}`   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import talon_one
from talon_one.api.management_api import ManagementApi  # noqa: E501
from talon_one.rest import ApiException


class TestManagementApi(unittest.TestCase):
    """ManagementApi unit test stubs"""

    def setUp(self):
        self.api = talon_one.api.management_api.ManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_loyalty_points(self):
        """Test case for add_loyalty_points

        Add points in loyalty program for given customer  # noqa: E501
        """
        pass

    def test_copy_campaign_to_applications(self):
        """Test case for copy_campaign_to_applications

        Copy the campaign into the specified application  # noqa: E501
        """
        pass

    def test_create_account_collection(self):
        """Test case for create_account_collection

        Create account-level collection  # noqa: E501
        """
        pass

    def test_create_additional_cost(self):
        """Test case for create_additional_cost

        Create additional cost  # noqa: E501
        """
        pass

    def test_create_attribute(self):
        """Test case for create_attribute

        Create custom attribute  # noqa: E501
        """
        pass

    def test_create_campaign_from_template(self):
        """Test case for create_campaign_from_template

        Create campaign from campaign template  # noqa: E501
        """
        pass

    def test_create_collection(self):
        """Test case for create_collection

        Create collection  # noqa: E501
        """
        pass

    def test_create_coupons(self):
        """Test case for create_coupons

        Create coupons  # noqa: E501
        """
        pass

    def test_create_coupons_async(self):
        """Test case for create_coupons_async

        Create coupons asynchronously  # noqa: E501
        """
        pass

    def test_create_coupons_for_multiple_recipients(self):
        """Test case for create_coupons_for_multiple_recipients

        Create coupons for multiple recipients  # noqa: E501
        """
        pass

    def test_create_notification_webhook(self):
        """Test case for create_notification_webhook

        Create notification webhook  # noqa: E501
        """
        pass

    def test_create_password_recovery_email(self):
        """Test case for create_password_recovery_email

        Request a password reset  # noqa: E501
        """
        pass

    def test_create_session(self):
        """Test case for create_session

        Create session  # noqa: E501
        """
        pass

    def test_delete_account_collection(self):
        """Test case for delete_account_collection

        Delete account-level collection  # noqa: E501
        """
        pass

    def test_delete_campaign(self):
        """Test case for delete_campaign

        Delete campaign  # noqa: E501
        """
        pass

    def test_delete_collection(self):
        """Test case for delete_collection

        Delete collection  # noqa: E501
        """
        pass

    def test_delete_coupon(self):
        """Test case for delete_coupon

        Delete coupon  # noqa: E501
        """
        pass

    def test_delete_coupons(self):
        """Test case for delete_coupons

        Delete coupons  # noqa: E501
        """
        pass

    def test_delete_notification_webhook(self):
        """Test case for delete_notification_webhook

        Delete notification webhook  # noqa: E501
        """
        pass

    def test_delete_referral(self):
        """Test case for delete_referral

        Delete referral  # noqa: E501
        """
        pass

    def test_destroy_session(self):
        """Test case for destroy_session

        Destroy session  # noqa: E501
        """
        pass

    def test_export_account_collection_items(self):
        """Test case for export_account_collection_items

        Export account-level collection's items  # noqa: E501
        """
        pass

    def test_export_collection_items(self):
        """Test case for export_collection_items

        Export a collection's items  # noqa: E501
        """
        pass

    def test_export_coupons(self):
        """Test case for export_coupons

        Export coupons  # noqa: E501
        """
        pass

    def test_export_customer_sessions(self):
        """Test case for export_customer_sessions

        Export customer sessions  # noqa: E501
        """
        pass

    def test_export_effects(self):
        """Test case for export_effects

        Export triggered effects  # noqa: E501
        """
        pass

    def test_export_loyalty_balance(self):
        """Test case for export_loyalty_balance

        Export customer loyalty balance to a CSV file  # noqa: E501
        """
        pass

    def test_export_loyalty_ledger(self):
        """Test case for export_loyalty_ledger

        Export a customer's loyalty ledger log  # noqa: E501
        """
        pass

    def test_export_referrals(self):
        """Test case for export_referrals

        Export referrals  # noqa: E501
        """
        pass

    def test_get_access_logs_without_total_count(self):
        """Test case for get_access_logs_without_total_count

        Get access logs for Application  # noqa: E501
        """
        pass

    def test_get_account(self):
        """Test case for get_account

        Get account details  # noqa: E501
        """
        pass

    def test_get_account_analytics(self):
        """Test case for get_account_analytics

        Get account analytics  # noqa: E501
        """
        pass

    def test_get_account_collection(self):
        """Test case for get_account_collection

        Get account-level collection  # noqa: E501
        """
        pass

    def test_get_additional_cost(self):
        """Test case for get_additional_cost

        Get additional cost  # noqa: E501
        """
        pass

    def test_get_additional_costs(self):
        """Test case for get_additional_costs

        List additional costs  # noqa: E501
        """
        pass

    def test_get_all_access_logs(self):
        """Test case for get_all_access_logs

        List access logs  # noqa: E501
        """
        pass

    def test_get_all_roles(self):
        """Test case for get_all_roles

        List roles  # noqa: E501
        """
        pass

    def test_get_application(self):
        """Test case for get_application

        Get application  # noqa: E501
        """
        pass

    def test_get_application_api_health(self):
        """Test case for get_application_api_health

        Get report of health of application API  # noqa: E501
        """
        pass

    def test_get_application_customer(self):
        """Test case for get_application_customer

        Get application's customer  # noqa: E501
        """
        pass

    def test_get_application_customer_friends(self):
        """Test case for get_application_customer_friends

        List friends referred by customer profile  # noqa: E501
        """
        pass

    def test_get_application_customers(self):
        """Test case for get_application_customers

        List application's customers  # noqa: E501
        """
        pass

    def test_get_application_customers_by_attributes(self):
        """Test case for get_application_customers_by_attributes

        List application customers matching the given attributes  # noqa: E501
        """
        pass

    def test_get_application_event_types(self):
        """Test case for get_application_event_types

        List Applications event types  # noqa: E501
        """
        pass

    def test_get_application_events_without_total_count(self):
        """Test case for get_application_events_without_total_count

        List Applications events  # noqa: E501
        """
        pass

    def test_get_application_session(self):
        """Test case for get_application_session

        Get Application session  # noqa: E501
        """
        pass

    def test_get_application_sessions(self):
        """Test case for get_application_sessions

        List Application sessions  # noqa: E501
        """
        pass

    def test_get_applications(self):
        """Test case for get_applications

        List applications  # noqa: E501
        """
        pass

    def test_get_attribute(self):
        """Test case for get_attribute

        Get custom attribute  # noqa: E501
        """
        pass

    def test_get_attributes(self):
        """Test case for get_attributes

        List custom attributes  # noqa: E501
        """
        pass

    def test_get_audiences(self):
        """Test case for get_audiences

        List audiences  # noqa: E501
        """
        pass

    def test_get_campaign(self):
        """Test case for get_campaign

        Get campaign  # noqa: E501
        """
        pass

    def test_get_campaign_analytics(self):
        """Test case for get_campaign_analytics

        Get analytics of campaigns  # noqa: E501
        """
        pass

    def test_get_campaign_by_attributes(self):
        """Test case for get_campaign_by_attributes

        List campaigns that match the given attributes  # noqa: E501
        """
        pass

    def test_get_campaigns(self):
        """Test case for get_campaigns

        List campaigns  # noqa: E501
        """
        pass

    def test_get_changes(self):
        """Test case for get_changes

        Get audit logs for an account  # noqa: E501
        """
        pass

    def test_get_collection(self):
        """Test case for get_collection

        Get collection  # noqa: E501
        """
        pass

    def test_get_collection_items(self):
        """Test case for get_collection_items

        Get collection items  # noqa: E501
        """
        pass

    def test_get_coupons_without_total_count(self):
        """Test case for get_coupons_without_total_count

        List coupons  # noqa: E501
        """
        pass

    def test_get_customer_activity_report(self):
        """Test case for get_customer_activity_report

        Get customer's activity report  # noqa: E501
        """
        pass

    def test_get_customer_activity_reports_without_total_count(self):
        """Test case for get_customer_activity_reports_without_total_count

        Get Activity Reports for Application Customers  # noqa: E501
        """
        pass

    def test_get_customer_analytics(self):
        """Test case for get_customer_analytics

        Get customer's analytics report  # noqa: E501
        """
        pass

    def test_get_customer_profile(self):
        """Test case for get_customer_profile

        Get customer profile  # noqa: E501
        """
        pass

    def test_get_customer_profiles(self):
        """Test case for get_customer_profiles

        List customer profiles  # noqa: E501
        """
        pass

    def test_get_customers_by_attributes(self):
        """Test case for get_customers_by_attributes

        List customer profiles matching the given attributes  # noqa: E501
        """
        pass

    def test_get_event_types(self):
        """Test case for get_event_types

        List event types  # noqa: E501
        """
        pass

    def test_get_exports(self):
        """Test case for get_exports

        Get exports  # noqa: E501
        """
        pass

    def test_get_loyalty_points(self):
        """Test case for get_loyalty_points

        Get the Loyalty Ledger for this integrationID  # noqa: E501
        """
        pass

    def test_get_loyalty_program(self):
        """Test case for get_loyalty_program

        Get loyalty program  # noqa: E501
        """
        pass

    def test_get_loyalty_programs(self):
        """Test case for get_loyalty_programs

        List loyalty programs  # noqa: E501
        """
        pass

    def test_get_loyalty_statistics(self):
        """Test case for get_loyalty_statistics

        Get loyalty program statistics by loyalty program ID  # noqa: E501
        """
        pass

    def test_get_notification_webhook(self):
        """Test case for get_notification_webhook

        Get notification webhook  # noqa: E501
        """
        pass

    def test_get_notification_webhooks(self):
        """Test case for get_notification_webhooks

        List notification webhooks  # noqa: E501
        """
        pass

    def test_get_referrals_without_total_count(self):
        """Test case for get_referrals_without_total_count

        List referrals  # noqa: E501
        """
        pass

    def test_get_role(self):
        """Test case for get_role

        Get role  # noqa: E501
        """
        pass

    def test_get_ruleset(self):
        """Test case for get_ruleset

        Get ruleset  # noqa: E501
        """
        pass

    def test_get_rulesets(self):
        """Test case for get_rulesets

        List campaign rulesets  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get user  # noqa: E501
        """
        pass

    def test_get_users(self):
        """Test case for get_users

        List users in account  # noqa: E501
        """
        pass

    def test_get_webhook(self):
        """Test case for get_webhook

        Get webhook  # noqa: E501
        """
        pass

    def test_get_webhook_activation_logs(self):
        """Test case for get_webhook_activation_logs

        List webhook activation log entries  # noqa: E501
        """
        pass

    def test_get_webhook_logs(self):
        """Test case for get_webhook_logs

        List webhook log entries  # noqa: E501
        """
        pass

    def test_get_webhooks(self):
        """Test case for get_webhooks

        List webhooks  # noqa: E501
        """
        pass

    def test_import_account_collection(self):
        """Test case for import_account_collection

        Import data in existing account-level collection  # noqa: E501
        """
        pass

    def test_import_allowed_list(self):
        """Test case for import_allowed_list

        Import allowed values for attribute  # noqa: E501
        """
        pass

    def test_import_collection(self):
        """Test case for import_collection

        Import data in existing collection  # noqa: E501
        """
        pass

    def test_import_coupons(self):
        """Test case for import_coupons

        Import coupons  # noqa: E501
        """
        pass

    def test_import_loyalty_points(self):
        """Test case for import_loyalty_points

        Import loyalty points  # noqa: E501
        """
        pass

    def test_import_pool_giveaways(self):
        """Test case for import_pool_giveaways

        Import giveaway codes into a giveaway pool  # noqa: E501
        """
        pass

    def test_import_referrals(self):
        """Test case for import_referrals

        Import referrals  # noqa: E501
        """
        pass

    def test_list_account_collections(self):
        """Test case for list_account_collections

        List collections in account  # noqa: E501
        """
        pass

    def test_list_collections(self):
        """Test case for list_collections

        List collections  # noqa: E501
        """
        pass

    def test_list_collections_in_application(self):
        """Test case for list_collections_in_application

        List collections in application  # noqa: E501
        """
        pass

    def test_remove_loyalty_points(self):
        """Test case for remove_loyalty_points

        Deduct points in loyalty program for given customer  # noqa: E501
        """
        pass

    def test_reset_password(self):
        """Test case for reset_password

        Reset password  # noqa: E501
        """
        pass

    def test_search_coupons_advanced_application_wide_without_total_count(self):
        """Test case for search_coupons_advanced_application_wide_without_total_count

        List coupons that match the given attributes (without total count)  # noqa: E501
        """
        pass

    def test_search_coupons_advanced_without_total_count(self):
        """Test case for search_coupons_advanced_without_total_count

        List coupons that match the given attributes in campaign (without total count)  # noqa: E501
        """
        pass

    def test_update_account_collection(self):
        """Test case for update_account_collection

        Update account-level collection  # noqa: E501
        """
        pass

    def test_update_additional_cost(self):
        """Test case for update_additional_cost

        Update additional cost  # noqa: E501
        """
        pass

    def test_update_attribute(self):
        """Test case for update_attribute

        Update custom attribute  # noqa: E501
        """
        pass

    def test_update_campaign(self):
        """Test case for update_campaign

        Update campaign  # noqa: E501
        """
        pass

    def test_update_collection(self):
        """Test case for update_collection

        Update collection description  # noqa: E501
        """
        pass

    def test_update_coupon(self):
        """Test case for update_coupon

        Update coupon  # noqa: E501
        """
        pass

    def test_update_coupon_batch(self):
        """Test case for update_coupon_batch

        Update coupons  # noqa: E501
        """
        pass

    def test_update_notification_webhook(self):
        """Test case for update_notification_webhook

        Update notification webhook  # noqa: E501
        """
        pass

    def test_update_referral(self):
        """Test case for update_referral

        Update referral  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
