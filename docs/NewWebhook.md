# NewWebhook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_ids** | **list[int]** | The IDs of the applications that are related to this entity. | 
**title** | **str** | Friendly title for this webhook. | 
**verb** | **str** | API method for this webhook. | 
**url** | **str** | API url (supports templating using parameters) for this webhook. | 
**headers** | **list[str]** | List of API HTTP headers for this webhook. | 
**payload** | **str** | API payload (supports templating using parameters) for this webhook. | [optional] 
**params** | [**list[TemplateArgDef]**](TemplateArgDef.md) | Array of template argument definitions. | 
**enabled** | **bool** | Enables or disables webhook from showing in rule builder. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


