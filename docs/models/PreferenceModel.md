# xprizo_sdk_py.model.preference_model.PreferenceModel

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**hashId** | None, str,  | NoneClass, str,  |  | [optional] 
**isCookiesAllowed** | bool,  | BoolClass,  |  | [optional] 
**isUserNameVisible** | bool,  | BoolClass,  |  | [optional] 
**isEmailVisible** | bool,  | BoolClass,  |  | [optional] 
**isPhoneVisible** | bool,  | BoolClass,  |  | [optional] 
**isLocationVisible** | bool,  | BoolClass,  |  | [optional] 
**findOption** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**receiveSupportNotification** | bool,  | BoolClass,  |  | [optional] 
**latLng** | None, str,  | NoneClass, str,  |  | [optional] 
**profilePicture** | None, str,  | NoneClass, str,  |  | [optional] 
**notificationCount** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**notificationPushToken** | None, str,  | NoneClass, str,  |  | [optional] 
**agentDepositFee** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**agentWithdrawalFee** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit float
**transferFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**kycLevel** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**merchantLevel** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**merchantFee** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**depositLimit** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**withdrawalLimit** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**payFeesFromSavings** | bool,  | BoolClass,  |  | [optional] 
**lastLogin** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**registeredOn** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**recruitedOn** | None, str, datetime,  | NoneClass, str,  |  | [optional] value must conform to RFC-3339 date-time
**agentId** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**agentCommission** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**isSubAgent** | bool,  | BoolClass,  |  | [optional] 
**notifyViaEmail** | bool,  | BoolClass,  |  | [optional] 
**notifyOnNewApproval** | bool,  | BoolClass,  |  | [optional] 
**notifyOnNewTransaction** | bool,  | BoolClass,  |  | [optional] 
**notifyOnNewTicket** | bool,  | BoolClass,  |  | [optional] 
**approvalWebhook** | None, str,  | NoneClass, str,  |  | [optional] 
**paymentWebhook** | None, str,  | NoneClass, str,  |  | [optional] 
**requestPaymentWebhook** | None, str,  | NoneClass, str,  |  | [optional] 
**allowMarketingEmails** | bool,  | BoolClass,  |  | [optional] 
**defaultOTPType** | None, str,  | NoneClass, str,  |  | [optional] 
**language** | None, str,  | NoneClass, str,  |  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

