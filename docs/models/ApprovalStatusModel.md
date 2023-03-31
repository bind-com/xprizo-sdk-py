# xprizo_sdk_py.model.approval_status_model.ApprovalStatusModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**statusType** | [**PendingTransactionStatus**](PendingTransactionStatus.md) | [**PendingTransactionStatus**](PendingTransactionStatus.md) |  | [optional] 
**status** | None, str,  | NoneClass, str,  |  | [optional] 
**actionedById** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**[affectedContactIds](#affectedContactIds)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**transaction** | [**TranHeadDataModel**](TranHeadDataModel.md) | [**TranHeadDataModel**](TranHeadDataModel.md) |  | [optional] 

# affectedContactIds

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

