# xprizo_sdk_py.model.profile_full_model.ProfileFullModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**hashId** | None, str,  | NoneClass, str,  |  | [optional] 
**name** | None, str,  | NoneClass, str,  |  | [optional] 
**role** | None, str,  | NoneClass, str,  |  | [optional] 
**isInactive** | bool,  | BoolClass,  |  | [optional] 
**isSuspended** | bool,  | BoolClass,  |  | [optional] 
**isAgent** | bool,  | BoolClass,  |  | [optional] 
**isUnlocked** | bool,  | BoolClass,  |  | [optional] 
**usePaymentPin** | bool,  | BoolClass,  |  | [optional] 
**lastLogin** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**registeredOn** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**recruitedOn** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**contact** | [**ContactModel**](ContactModel.md) | [**ContactModel**](ContactModel.md) |  | [optional] 
**preference** | [**PreferenceModel**](PreferenceModel.md) | [**PreferenceModel**](PreferenceModel.md) |  | [optional] 
**[userWallets](#userWallets)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[savingWallets](#savingWallets)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[agentWallets](#agentWallets)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 
**[linkedWallets](#linkedWallets)** | list, tuple, None,  | tuple, NoneClass,  |  | [optional] 

# userWallets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WalletAccountModel**](WalletAccountModel.md) | [**WalletAccountModel**](WalletAccountModel.md) | [**WalletAccountModel**](WalletAccountModel.md) |  | 

# savingWallets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WalletAccountModel**](WalletAccountModel.md) | [**WalletAccountModel**](WalletAccountModel.md) | [**WalletAccountModel**](WalletAccountModel.md) |  | 

# agentWallets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WalletAccountModel**](WalletAccountModel.md) | [**WalletAccountModel**](WalletAccountModel.md) | [**WalletAccountModel**](WalletAccountModel.md) |  | 

# linkedWallets

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LinkedWalletModel**](LinkedWalletModel.md) | [**LinkedWalletModel**](LinkedWalletModel.md) | [**LinkedWalletModel**](LinkedWalletModel.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

