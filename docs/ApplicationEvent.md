# ApplicationEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for this entity. Not to be confused with the Integration ID, which is set by your integration layer and used in most endpoints. | 
**created** | **datetime** | The exact moment this entity was created. | 
**application_id** | **int** | The ID of the application that owns this entity. | 
**profile_id** | **int** | The globally unique Talon.One ID of the customer that created this entity. | [optional] 
**session_id** | **int** | The globally unique Talon.One ID of the session that contains this event. | [optional] 
**type** | **str** | A string representing the event. Must not be a reserved event name. | 
**attributes** | [**object**](.md) | Additional JSON serialized data associated with the event. | 
**effects** | **list[object]** | An array containing the effects that were applied as a result of this event. | 
**rule_failure_reasons** | [**list[RuleFailureReason]**](RuleFailureReason.md) | An array containing the rule failure reasons which happened during this event. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


