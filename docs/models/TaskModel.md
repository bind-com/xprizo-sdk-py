# xprizo_sdk_py.model.task_model.TaskModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**timestamp** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**accountId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**contactId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**contact** | None, str,  | NoneClass, str,  |  | [optional] 
**typeCode** | None, str,  | NoneClass, str,  |  | [optional] 
**createById** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**createdByName** | None, str,  | NoneClass, str,  |  | [optional] 
**description** | None, str,  | NoneClass, str,  |  | [optional] 
**assignedToId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**assigneeName** | None, str,  | NoneClass, str,  |  | [optional] 
**isHidden** | bool,  | BoolClass,  |  | [optional] 
**status** | None, str,  | NoneClass, str,  |  | [optional] 
**label** | None, str,  | NoneClass, str,  |  | [optional] 
**memo** | None, str,  | NoneClass, str,  |  | [optional] 
**amount** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**[comments](#comments)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**attachmentCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer

# comments

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

