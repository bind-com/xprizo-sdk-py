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


class WalletAccountModel(
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
            
            
            class name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'name':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            referenceNo = schemas.Int32Schema
            
            
            class referenceAlternate(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'referenceAlternate':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            contactId = schemas.Int64Schema
            
            
            class contact(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'contact':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            isInactive = schemas.BoolSchema
            
            
            class merchantCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'merchantCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            business = schemas.Float64Schema
            trust = schemas.Float64Schema
            realTrust = schemas.Float64Schema
            realBusiness = schemas.Float64Schema
            
            
            class realTradeLimit(
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
                ) -> 'realTradeLimit':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            tradeLimit = schemas.Float64Schema
            
            
            class oneOffWithdrawalAmount(
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
                ) -> 'oneOffWithdrawalAmount':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class dailyWithdrawalLimit(
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
                ) -> 'dailyWithdrawalLimit':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class realReserve(
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
                ) -> 'realReserve':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class currencyCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'currencyCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class symbol(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'symbol':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            newTransactionCount = schemas.Int32Schema
            isDefault = schemas.BoolSchema
            
            
            class lastTranHeadId(
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
                ) -> 'lastTranHeadId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "hashId": hashId,
                "name": name,
                "referenceNo": referenceNo,
                "referenceAlternate": referenceAlternate,
                "contactId": contactId,
                "contact": contact,
                "isInactive": isInactive,
                "merchantCode": merchantCode,
                "business": business,
                "trust": trust,
                "realTrust": realTrust,
                "realBusiness": realBusiness,
                "realTradeLimit": realTradeLimit,
                "tradeLimit": tradeLimit,
                "oneOffWithdrawalAmount": oneOffWithdrawalAmount,
                "dailyWithdrawalLimit": dailyWithdrawalLimit,
                "realReserve": realReserve,
                "currencyCode": currencyCode,
                "symbol": symbol,
                "newTransactionCount": newTransactionCount,
                "isDefault": isDefault,
                "lastTranHeadId": lastTranHeadId,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hashId"]) -> MetaOapg.properties.hashId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceNo"]) -> MetaOapg.properties.referenceNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["referenceAlternate"]) -> MetaOapg.properties.referenceAlternate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactId"]) -> MetaOapg.properties.contactId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact"]) -> MetaOapg.properties.contact: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isInactive"]) -> MetaOapg.properties.isInactive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantCode"]) -> MetaOapg.properties.merchantCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["business"]) -> MetaOapg.properties.business: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["trust"]) -> MetaOapg.properties.trust: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realTrust"]) -> MetaOapg.properties.realTrust: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realBusiness"]) -> MetaOapg.properties.realBusiness: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realTradeLimit"]) -> MetaOapg.properties.realTradeLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tradeLimit"]) -> MetaOapg.properties.tradeLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["oneOffWithdrawalAmount"]) -> MetaOapg.properties.oneOffWithdrawalAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dailyWithdrawalLimit"]) -> MetaOapg.properties.dailyWithdrawalLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realReserve"]) -> MetaOapg.properties.realReserve: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyCode"]) -> MetaOapg.properties.currencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["newTransactionCount"]) -> MetaOapg.properties.newTransactionCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastTranHeadId"]) -> MetaOapg.properties.lastTranHeadId: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["hashId"], typing_extensions.Literal["name"], typing_extensions.Literal["referenceNo"], typing_extensions.Literal["referenceAlternate"], typing_extensions.Literal["contactId"], typing_extensions.Literal["contact"], typing_extensions.Literal["isInactive"], typing_extensions.Literal["merchantCode"], typing_extensions.Literal["business"], typing_extensions.Literal["trust"], typing_extensions.Literal["realTrust"], typing_extensions.Literal["realBusiness"], typing_extensions.Literal["realTradeLimit"], typing_extensions.Literal["tradeLimit"], typing_extensions.Literal["oneOffWithdrawalAmount"], typing_extensions.Literal["dailyWithdrawalLimit"], typing_extensions.Literal["realReserve"], typing_extensions.Literal["currencyCode"], typing_extensions.Literal["symbol"], typing_extensions.Literal["newTransactionCount"], typing_extensions.Literal["isDefault"], typing_extensions.Literal["lastTranHeadId"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hashId"]) -> typing.Union[MetaOapg.properties.hashId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceNo"]) -> typing.Union[MetaOapg.properties.referenceNo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["referenceAlternate"]) -> typing.Union[MetaOapg.properties.referenceAlternate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactId"]) -> typing.Union[MetaOapg.properties.contactId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact"]) -> typing.Union[MetaOapg.properties.contact, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isInactive"]) -> typing.Union[MetaOapg.properties.isInactive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantCode"]) -> typing.Union[MetaOapg.properties.merchantCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["business"]) -> typing.Union[MetaOapg.properties.business, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trust"]) -> typing.Union[MetaOapg.properties.trust, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realTrust"]) -> typing.Union[MetaOapg.properties.realTrust, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realBusiness"]) -> typing.Union[MetaOapg.properties.realBusiness, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realTradeLimit"]) -> typing.Union[MetaOapg.properties.realTradeLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tradeLimit"]) -> typing.Union[MetaOapg.properties.tradeLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["oneOffWithdrawalAmount"]) -> typing.Union[MetaOapg.properties.oneOffWithdrawalAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dailyWithdrawalLimit"]) -> typing.Union[MetaOapg.properties.dailyWithdrawalLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realReserve"]) -> typing.Union[MetaOapg.properties.realReserve, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyCode"]) -> typing.Union[MetaOapg.properties.currencyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> typing.Union[MetaOapg.properties.symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["newTransactionCount"]) -> typing.Union[MetaOapg.properties.newTransactionCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDefault"]) -> typing.Union[MetaOapg.properties.isDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastTranHeadId"]) -> typing.Union[MetaOapg.properties.lastTranHeadId, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["hashId"], typing_extensions.Literal["name"], typing_extensions.Literal["referenceNo"], typing_extensions.Literal["referenceAlternate"], typing_extensions.Literal["contactId"], typing_extensions.Literal["contact"], typing_extensions.Literal["isInactive"], typing_extensions.Literal["merchantCode"], typing_extensions.Literal["business"], typing_extensions.Literal["trust"], typing_extensions.Literal["realTrust"], typing_extensions.Literal["realBusiness"], typing_extensions.Literal["realTradeLimit"], typing_extensions.Literal["tradeLimit"], typing_extensions.Literal["oneOffWithdrawalAmount"], typing_extensions.Literal["dailyWithdrawalLimit"], typing_extensions.Literal["realReserve"], typing_extensions.Literal["currencyCode"], typing_extensions.Literal["symbol"], typing_extensions.Literal["newTransactionCount"], typing_extensions.Literal["isDefault"], typing_extensions.Literal["lastTranHeadId"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hashId: typing.Union[MetaOapg.properties.hashId, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        referenceNo: typing.Union[MetaOapg.properties.referenceNo, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        referenceAlternate: typing.Union[MetaOapg.properties.referenceAlternate, None, str, schemas.Unset] = schemas.unset,
        contactId: typing.Union[MetaOapg.properties.contactId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        contact: typing.Union[MetaOapg.properties.contact, None, str, schemas.Unset] = schemas.unset,
        isInactive: typing.Union[MetaOapg.properties.isInactive, bool, schemas.Unset] = schemas.unset,
        merchantCode: typing.Union[MetaOapg.properties.merchantCode, None, str, schemas.Unset] = schemas.unset,
        business: typing.Union[MetaOapg.properties.business, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        trust: typing.Union[MetaOapg.properties.trust, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        realTrust: typing.Union[MetaOapg.properties.realTrust, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        realBusiness: typing.Union[MetaOapg.properties.realBusiness, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        realTradeLimit: typing.Union[MetaOapg.properties.realTradeLimit, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tradeLimit: typing.Union[MetaOapg.properties.tradeLimit, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        oneOffWithdrawalAmount: typing.Union[MetaOapg.properties.oneOffWithdrawalAmount, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        dailyWithdrawalLimit: typing.Union[MetaOapg.properties.dailyWithdrawalLimit, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        realReserve: typing.Union[MetaOapg.properties.realReserve, None, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currencyCode: typing.Union[MetaOapg.properties.currencyCode, None, str, schemas.Unset] = schemas.unset,
        symbol: typing.Union[MetaOapg.properties.symbol, None, str, schemas.Unset] = schemas.unset,
        newTransactionCount: typing.Union[MetaOapg.properties.newTransactionCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isDefault: typing.Union[MetaOapg.properties.isDefault, bool, schemas.Unset] = schemas.unset,
        lastTranHeadId: typing.Union[MetaOapg.properties.lastTranHeadId, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WalletAccountModel':
        return super().__new__(
            cls,
            *_args,
            id=id,
            hashId=hashId,
            name=name,
            referenceNo=referenceNo,
            referenceAlternate=referenceAlternate,
            contactId=contactId,
            contact=contact,
            isInactive=isInactive,
            merchantCode=merchantCode,
            business=business,
            trust=trust,
            realTrust=realTrust,
            realBusiness=realBusiness,
            realTradeLimit=realTradeLimit,
            tradeLimit=tradeLimit,
            oneOffWithdrawalAmount=oneOffWithdrawalAmount,
            dailyWithdrawalLimit=dailyWithdrawalLimit,
            realReserve=realReserve,
            currencyCode=currencyCode,
            symbol=symbol,
            newTransactionCount=newTransactionCount,
            isDefault=isDefault,
            lastTranHeadId=lastTranHeadId,
            _configuration=_configuration,
        )
