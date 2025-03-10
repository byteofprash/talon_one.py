# IntegrationEventV2Request


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | ID of the customer profile set by your integration layer.  **Note:** If the customer does not yet have a known &#x60;profileId&#x60;, we recommend you use a guest &#x60;profileId&#x60;.  | [optional] 
**type** | **str** | A string representing the event. Must not be a reserved event name. | 
**attributes** | [**object**](.md) | Arbitrary additional JSON data associated with the event. | [optional] 
**response_content** | **list[str]** | Optional list of requested information to be present on the response related to the tracking custom event.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


