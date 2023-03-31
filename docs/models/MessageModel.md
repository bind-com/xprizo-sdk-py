# xprizo_sdk_py.model.message_model.MessageModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**timestamp** | str, datetime,  | str,  |  | [optional] value must conform to RFC-3339 date-time
**contactId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**recipientId** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**parentId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**typeCode** | None, str,  | NoneClass, str,  |  | [optional] 
**message** | None, str,  | NoneClass, str,  |  | [optional] 
**isRead** | bool,  | BoolClass,  |  | [optional] 
**isImportant** | bool,  | BoolClass,  |  | [optional] 
**isDeleted** | bool,  | BoolClass,  |  | [optional] 
**label** | None, str,  | NoneClass, str,  |  | [optional] 
**data** | None, str,  | NoneClass, str,  |  | [optional] 
**recipientName** | None, str,  | NoneClass, str,  |  | [optional] 
**transaction** | [**WalletTranModel**](WalletTranModel.md) | [**WalletTranModel**](WalletTranModel.md) |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

