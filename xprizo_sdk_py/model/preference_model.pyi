# coding: utf-8

"""
    Xprizo API

    Xprizo api endpoints  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@xprizo.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from xprizo_sdk_py import schemas  # noqa: F401


class PreferenceModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            
            
            class hashId(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'hashId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            isCookiesAllowed = schemas.BoolSchema
            isUserNameVisible = schemas.BoolSchema
            isEmailVisible = schemas.BoolSchema
            isPhoneVisible = schemas.BoolSchema
            isLocationVisible = schemas.BoolSchema
            findOption = schemas.Int32Schema
            receiveSupportNotification = schemas.BoolSchema
            
            
            class latLng(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'latLng':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class profilePicture(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'profilePicture':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            notificationCount = schemas.Int32Schema
            
            
            class notificationPushToken(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'notificationPushToken':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class agentDepositFee(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'agentDepositFee':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class agentWithdrawalFee(
                schemas.Float64Base,
                schemas.NumberBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'double'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, float, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'agentWithdrawalFee':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            transferFee = schemas.Float64Schema
            kycLevel = schemas.Int32Schema
            merchantLevel = schemas.Int32Schema
            merchantFee = schemas.Float64Schema
            depositLimit = schemas.Float64Schema
            withdrawalLimit = schemas.Float64Schema
            payFeesFromSavings = schemas.BoolSchema
            
            
            class lastLogin(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lastLogin':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class registeredOn(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'registeredOn':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class recruitedOn(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'recruitedOn':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class agentId(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'agentId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            agentCommission = schemas.Float64Schema
            isSubAgent = schemas.BoolSchema
            notifyViaEmail = schemas.BoolSchema
            notifyOnNewApproval = schemas.BoolSchema
            notifyOnNewTransaction = schemas.BoolSchema
            notifyOnNewTicket = schemas.BoolSchema
            
            
            class approvalWebhook(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'approvalWebhook':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class paymentWebhook(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'paymentWebhook':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class requestPaymentWebhook(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'requestPaymentWebhook':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            allowMarketingEmails = schemas.BoolSchema
            
            
            class defaultOTPType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'defaultOTPType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class language(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'language':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "hashId": hashId,
                "isCookiesAllowed": isCookiesAllowed,
                "isUserNameVisible": isUserNameVisible,
                "isEmailVisible": isEmailVisible,
                "isPhoneVisible": isPhoneVisible,
                "isLocationVisible": isLocationVisible,
                "findOption": findOption,
                "receiveSupportNotification": receiveSupportNotification,
                "latLng": latLng,
                "profilePicture": profilePicture,
                "notificationCount": notificationCount,
                "notificationPushToken": notificationPushToken,
                "agentDepositFee": agentDepositFee,
                "agentWithdrawalFee": agentWithdrawalFee,
                "transferFee": transferFee,
                "kycLevel": kycLevel,
                "merchantLevel": merchantLevel,
                "merchantFee": merchantFee,
                "depositLimit": depositLimit,
                "withdrawalLimit": withdrawalLimit,
                "payFeesFromSavings": payFeesFromSavings,
                "lastLogin": lastLogin,
                "registeredOn": registeredOn,
                "recruitedOn": recruitedOn,
                "agentId": agentId,
                "agentCommission": agentCommission,
                "isSubAgent": isSubAgent,
                "notifyViaEmail": notifyViaEmail,
                "notifyOnNewApproval": notifyOnNewApproval,
                "notifyOnNewTransaction": notifyOnNewTransaction,
                "notifyOnNewTicket": notifyOnNewTicket,
                "approvalWebhook": approvalWebhook,
                "paymentWebhook": paymentWebhook,
                "requestPaymentWebhook": requestPaymentWebhook,
                "allowMarketingEmails": allowMarketingEmails,
                "defaultOTPType": defaultOTPType,
                "language": language,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hashId"]) -> MetaOapg.properties.hashId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isCookiesAllowed"]) -> MetaOapg.properties.isCookiesAllowed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isUserNameVisible"]) -> MetaOapg.properties.isUserNameVisible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEmailVisible"]) -> MetaOapg.properties.isEmailVisible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isPhoneVisible"]) -> MetaOapg.properties.isPhoneVisible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isLocationVisible"]) -> MetaOapg.properties.isLocationVisible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["findOption"]) -> MetaOapg.properties.findOption: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiveSupportNotification"]) -> MetaOapg.properties.receiveSupportNotification: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["latLng"]) -> MetaOapg.properties.latLng: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profilePicture"]) -> MetaOapg.properties.profilePicture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notificationCount"]) -> MetaOapg.properties.notificationCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notificationPushToken"]) -> MetaOapg.properties.notificationPushToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agentDepositFee"]) -> MetaOapg.properties.agentDepositFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agentWithdrawalFee"]) -> MetaOapg.properties.agentWithdrawalFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transferFee"]) -> MetaOapg.properties.transferFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kycLevel"]) -> MetaOapg.properties.kycLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantLevel"]) -> MetaOapg.properties.merchantLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantFee"]) -> MetaOapg.properties.merchantFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["depositLimit"]) -> MetaOapg.properties.depositLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withdrawalLimit"]) -> MetaOapg.properties.withdrawalLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payFeesFromSavings"]) -> MetaOapg.properties.payFeesFromSavings: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastLogin"]) -> MetaOapg.properties.lastLogin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registeredOn"]) -> MetaOapg.properties.registeredOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recruitedOn"]) -> MetaOapg.properties.recruitedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agentId"]) -> MetaOapg.properties.agentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agentCommission"]) -> MetaOapg.properties.agentCommission: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSubAgent"]) -> MetaOapg.properties.isSubAgent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifyViaEmail"]) -> MetaOapg.properties.notifyViaEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifyOnNewApproval"]) -> MetaOapg.properties.notifyOnNewApproval: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifyOnNewTransaction"]) -> MetaOapg.properties.notifyOnNewTransaction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifyOnNewTicket"]) -> MetaOapg.properties.notifyOnNewTicket: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approvalWebhook"]) -> MetaOapg.properties.approvalWebhook: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paymentWebhook"]) -> MetaOapg.properties.paymentWebhook: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestPaymentWebhook"]) -> MetaOapg.properties.requestPaymentWebhook: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowMarketingEmails"]) -> MetaOapg.properties.allowMarketingEmails: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultOTPType"]) -> MetaOapg.properties.defaultOTPType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> MetaOapg.properties.language: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["hashId"], typing_extensions.Literal["isCookiesAllowed"], typing_extensions.Literal["isUserNameVisible"], typing_extensions.Literal["isEmailVisible"], typing_extensions.Literal["isPhoneVisible"], typing_extensions.Literal["isLocationVisible"], typing_extensions.Literal["findOption"], typing_extensions.Literal["receiveSupportNotification"], typing_extensions.Literal["latLng"], typing_extensions.Literal["profilePicture"], typing_extensions.Literal["notificationCount"], typing_extensions.Literal["notificationPushToken"], typing_extensions.Literal["agentDepositFee"], typing_extensions.Literal["agentWithdrawalFee"], typing_extensions.Literal["transferFee"], typing_extensions.Literal["kycLevel"], typing_extensions.Literal["merchantLevel"], typing_extensions.Literal["merchantFee"], typing_extensions.Literal["depositLimit"], typing_extensions.Literal["withdrawalLimit"], typing_extensions.Literal["payFeesFromSavings"], typing_extensions.Literal["lastLogin"], typing_extensions.Literal["registeredOn"], typing_extensions.Literal["recruitedOn"], typing_extensions.Literal["agentId"], typing_extensions.Literal["agentCommission"], typing_extensions.Literal["isSubAgent"], typing_extensions.Literal["notifyViaEmail"], typing_extensions.Literal["notifyOnNewApproval"], typing_extensions.Literal["notifyOnNewTransaction"], typing_extensions.Literal["notifyOnNewTicket"], typing_extensions.Literal["approvalWebhook"], typing_extensions.Literal["paymentWebhook"], typing_extensions.Literal["requestPaymentWebhook"], typing_extensions.Literal["allowMarketingEmails"], typing_extensions.Literal["defaultOTPType"], typing_extensions.Literal["language"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hashId"]) -> typing.Union[MetaOapg.properties.hashId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isCookiesAllowed"]) -> typing.Union[MetaOapg.properties.isCookiesAllowed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isUserNameVisible"]) -> typing.Union[MetaOapg.properties.isUserNameVisible, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEmailVisible"]) -> typing.Union[MetaOapg.properties.isEmailVisible, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isPhoneVisible"]) -> typing.Union[MetaOapg.properties.isPhoneVisible, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isLocationVisible"]) -> typing.Union[MetaOapg.properties.isLocationVisible, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["findOption"]) -> typing.Union[MetaOapg.properties.findOption, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiveSupportNotification"]) -> typing.Union[MetaOapg.properties.receiveSupportNotification, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["latLng"]) -> typing.Union[MetaOapg.properties.latLng, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profilePicture"]) -> typing.Union[MetaOapg.properties.profilePicture, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notificationCount"]) -> typing.Union[MetaOapg.properties.notificationCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notificationPushToken"]) -> typing.Union[MetaOapg.properties.notificationPushToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agentDepositFee"]) -> typing.Union[MetaOapg.properties.agentDepositFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agentWithdrawalFee"]) -> typing.Union[MetaOapg.properties.agentWithdrawalFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transferFee"]) -> typing.Union[MetaOapg.properties.transferFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kycLevel"]) -> typing.Union[MetaOapg.properties.kycLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantLevel"]) -> typing.Union[MetaOapg.properties.merchantLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantFee"]) -> typing.Union[MetaOapg.properties.merchantFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["depositLimit"]) -> typing.Union[MetaOapg.properties.depositLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withdrawalLimit"]) -> typing.Union[MetaOapg.properties.withdrawalLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payFeesFromSavings"]) -> typing.Union[MetaOapg.properties.payFeesFromSavings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastLogin"]) -> typing.Union[MetaOapg.properties.lastLogin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registeredOn"]) -> typing.Union[MetaOapg.properties.registeredOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recruitedOn"]) -> typing.Union[MetaOapg.properties.recruitedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agentId"]) -> typing.Union[MetaOapg.properties.agentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agentCommission"]) -> typing.Union[MetaOapg.properties.agentCommission, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSubAgent"]) -> typing.Union[MetaOapg.properties.isSubAgent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifyViaEmail"]) -> typing.Union[MetaOapg.properties.notifyViaEmail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifyOnNewApproval"]) -> typing.Union[MetaOapg.properties.notifyOnNewApproval, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifyOnNewTransaction"]) -> typing.Union[MetaOapg.properties.notifyOnNewTransaction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifyOnNewTicket"]) -> typing.Union[MetaOapg.properties.notifyOnNewTicket, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approvalWebhook"]) -> typing.Union[MetaOapg.properties.approvalWebhook, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paymentWebhook"]) -> typing.Union[MetaOapg.properties.paymentWebhook, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestPaymentWebhook"]) -> typing.Union[MetaOapg.properties.requestPaymentWebhook, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowMarketingEmails"]) -> typing.Union[MetaOapg.properties.allowMarketingEmails, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultOTPType"]) -> typing.Union[MetaOapg.properties.defaultOTPType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union[MetaOapg.properties.language, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["hashId"], typing_extensions.Literal["isCookiesAllowed"], typing_extensions.Literal["isUserNameVisible"], typing_extensions.Literal["isEmailVisible"], typing_extensions.Literal["isPhoneVisible"], typing_extensions.Literal["isLocationVisible"], typing_extensions.Literal["findOption"], typing_extensions.Literal["receiveSupportNotification"], typing_extensions.Literal["latLng"], typing_extensions.Literal["profilePicture"], typing_extensions.Literal["notificationCount"], typing_extensions.Literal["notificationPushToken"], typing_extensions.Literal["agentDepositFee"], typing_extensions.Literal["agentWithdrawalFee"], typing_extensions.Literal["transferFee"], typing_extensions.Literal["kycLevel"], typing_extensions.Literal["merchantLevel"], typing_extensions.Literal["merchantFee"], typing_extensions.Literal["depositLimit"], typing_extensions.Literal["withdrawalLimit"], typing_extensions.Literal["payFeesFromSavings"], typing_extensions.Literal["lastLogin"], typing_extensions.Literal["registeredOn"], typing_extensions.Literal["recruitedOn"], typing_extensions.Literal["agentId"], typing_extensions.Literal["agentCommission"], typing_extensions.Literal["isSubAgent"], typing_extensions.Literal["notifyViaEmail"], typing_extensions.Literal["notifyOnNewApproval"], typing_extensions.Literal["notifyOnNewTransaction"], typing_extensions.Literal["notifyOnNewTicket"], typing_extensions.Literal["approvalWebhook"], typing_extensions.Literal["paymentWebhook"], typing_extensions.Literal["requestPaymentWebhook"], typing_extensions.Literal["allowMarketingEmails"], typing_extensions.Literal["defaultOTPType"], typing_extensions.Literal["language"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hashId: typing.Union[MetaOapg.properties.hashId, None, str, schemas.Unset] = schemas.unset,
        isCookiesAllowed: typing.Union[MetaOapg.properties.isCookiesAllowed, bool, schemas.Unset] = schemas.unset,
        isUserNameVisible: typing.Union[MetaOapg.properties.isUserNameVisible, bool, schemas.Unset] = schemas.unset,
        isEmailVisible: typing.Union[MetaOapg.properties.isEmailVisible, bool, schemas.Unset] = schemas.unset,
        isPhoneVisible: typing.Union[MetaOapg.properties.isPhoneVisible, bool, schemas.Unset] = schemas.unset,
        isLocationVisible: typing.Union[MetaOapg.properties.isLocationVisible, bool, schemas.Unset] = schemas.unset,
        findOption: typing.Union[MetaOapg.properties.findOption, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        receiveSupportNotification: typing.Union[MetaOapg.properties.receiveSupportNotification, bool, schemas.Unset] = schemas.unset,
        latLng: typing.Union[MetaOapg.properties.latLng, None, str, schemas.Unset] = schemas.unset,
        profilePicture: typing.Union[MetaOapg.properties.profilePicture, None, str, schemas.Unset] = schemas.unset,
        notificationCount: typing.Union[MetaOapg.properties.notificationCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        notificationPushToken: typing.Union[MetaOapg.properties.notificationPushToken, None, str, schemas.Unset] = schemas.unset,
        agentDepositFee: typing.Union[MetaOapg.properties.agentDepositFee, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        agentWithdrawalFee: typing.Union[MetaOapg.properties.agentWithdrawalFee, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        transferFee: typing.Union[MetaOapg.properties.transferFee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        kycLevel: typing.Union[MetaOapg.properties.kycLevel, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        merchantLevel: typing.Union[MetaOapg.properties.merchantLevel, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        merchantFee: typing.Union[MetaOapg.properties.merchantFee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        depositLimit: typing.Union[MetaOapg.properties.depositLimit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        withdrawalLimit: typing.Union[MetaOapg.properties.withdrawalLimit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        payFeesFromSavings: typing.Union[MetaOapg.properties.payFeesFromSavings, bool, schemas.Unset] = schemas.unset,
        lastLogin: typing.Union[MetaOapg.properties.lastLogin, None, str, datetime, schemas.Unset] = schemas.unset,
        registeredOn: typing.Union[MetaOapg.properties.registeredOn, None, str, datetime, schemas.Unset] = schemas.unset,
        recruitedOn: typing.Union[MetaOapg.properties.recruitedOn, None, str, datetime, schemas.Unset] = schemas.unset,
        agentId: typing.Union[MetaOapg.properties.agentId, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        agentCommission: typing.Union[MetaOapg.properties.agentCommission, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        isSubAgent: typing.Union[MetaOapg.properties.isSubAgent, bool, schemas.Unset] = schemas.unset,
        notifyViaEmail: typing.Union[MetaOapg.properties.notifyViaEmail, bool, schemas.Unset] = schemas.unset,
        notifyOnNewApproval: typing.Union[MetaOapg.properties.notifyOnNewApproval, bool, schemas.Unset] = schemas.unset,
        notifyOnNewTransaction: typing.Union[MetaOapg.properties.notifyOnNewTransaction, bool, schemas.Unset] = schemas.unset,
        notifyOnNewTicket: typing.Union[MetaOapg.properties.notifyOnNewTicket, bool, schemas.Unset] = schemas.unset,
        approvalWebhook: typing.Union[MetaOapg.properties.approvalWebhook, None, str, schemas.Unset] = schemas.unset,
        paymentWebhook: typing.Union[MetaOapg.properties.paymentWebhook, None, str, schemas.Unset] = schemas.unset,
        requestPaymentWebhook: typing.Union[MetaOapg.properties.requestPaymentWebhook, None, str, schemas.Unset] = schemas.unset,
        allowMarketingEmails: typing.Union[MetaOapg.properties.allowMarketingEmails, bool, schemas.Unset] = schemas.unset,
        defaultOTPType: typing.Union[MetaOapg.properties.defaultOTPType, None, str, schemas.Unset] = schemas.unset,
        language: typing.Union[MetaOapg.properties.language, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PreferenceModel':
        return super().__new__(
            cls,
            *_args,
            id=id,
            hashId=hashId,
            isCookiesAllowed=isCookiesAllowed,
            isUserNameVisible=isUserNameVisible,
            isEmailVisible=isEmailVisible,
            isPhoneVisible=isPhoneVisible,
            isLocationVisible=isLocationVisible,
            findOption=findOption,
            receiveSupportNotification=receiveSupportNotification,
            latLng=latLng,
            profilePicture=profilePicture,
            notificationCount=notificationCount,
            notificationPushToken=notificationPushToken,
            agentDepositFee=agentDepositFee,
            agentWithdrawalFee=agentWithdrawalFee,
            transferFee=transferFee,
            kycLevel=kycLevel,
            merchantLevel=merchantLevel,
            merchantFee=merchantFee,
            depositLimit=depositLimit,
            withdrawalLimit=withdrawalLimit,
            payFeesFromSavings=payFeesFromSavings,
            lastLogin=lastLogin,
            registeredOn=registeredOn,
            recruitedOn=recruitedOn,
            agentId=agentId,
            agentCommission=agentCommission,
            isSubAgent=isSubAgent,
            notifyViaEmail=notifyViaEmail,
            notifyOnNewApproval=notifyOnNewApproval,
            notifyOnNewTransaction=notifyOnNewTransaction,
            notifyOnNewTicket=notifyOnNewTicket,
            approvalWebhook=approvalWebhook,
            paymentWebhook=paymentWebhook,
            requestPaymentWebhook=requestPaymentWebhook,
            allowMarketingEmails=allowMarketingEmails,
            defaultOTPType=defaultOTPType,
            language=language,
            _configuration=_configuration,
        )
