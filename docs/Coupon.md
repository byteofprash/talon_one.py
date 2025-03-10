# Coupon


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**campaign_id** | **int** | The ID of the campaign that owns this entity. | 
**value** | **str** | The coupon code. | 
**usage_limit** | **int** | The number of times the coupon code can be redeemed. &#x60;0&#x60; means unlimited redemptions but any campaign usage limits will still apply.  | 
**discount_limit** | **float** | The amount of discounts that can be given with this coupon code.  | [optional] 
**start_date** | **datetime** | Timestamp at which point the coupon becomes valid. | [optional] 
**expiry_date** | **datetime** | Expiry date of the coupon. Coupon never expires if this is omitted, zero, or negative. | [optional] 
**limits** | [**list[LimitConfig]**](LimitConfig.md) | Limits configuration for a coupon. These limits will override the limits set from the campaign.  **Note:** Only usable when creating a single coupon which is not tied to a specific recipient. Only per-profile limits are allowed to be configured.  | [optional] 
**usage_counter** | **int** | The number of times this coupon has been successfully used. | 
**discount_counter** | **float** | The amount of discounts given on rules redeeming this coupon. Only usable if a coupon discount budget was set for this coupon. | [optional] 
**discount_remainder** | **float** | The remaining discount this coupon can give. | [optional] 
**attributes** | [**object**](.md) | Custom attributes associated with this coupon. | [optional] 
**referral_id** | **int** | The integration ID of the referring customer (if any) for whom this coupon was created as an effect. | [optional] 
**recipient_integration_id** | **str** | The Integration ID of the customer that is allowed to redeem this coupon. | [optional] 
**import_id** | **int** | The ID of the Import which created this coupon. | [optional] 
**reservation** | **bool** | Defines the type of reservation: - &#x60;true&#x60;: The reservation is a soft reservation. Any customer can use the coupon. This is done via the [Create coupon reservation endpoint](/integration-api/#operation/createCouponReservation). - &#x60;false&#x60;: The reservation is a hard reservation. Only the associated customer (&#x60;recipientIntegrationId&#x60;) can use the coupon. This is done via the Campaign Manager when you create a coupon for a given &#x60;recipientIntegrationId&#x60;, the [Create coupons endpoint](/management-api/#operation/createCoupons) or [Create coupons for multiple recipients endpoint](/management-api/#operation/createCouponsForMultipleRecipients).  | [optional] [default to True]
**batch_id** | **str** | The id of the batch the coupon belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


