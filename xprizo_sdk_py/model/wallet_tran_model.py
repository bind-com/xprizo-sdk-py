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


class WalletTranModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
            tranHeadId = schemas.Int64Schema
            date = schemas.DateTimeSchema
            
            
            class reference(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'reference':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class tranTypeCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tranTypeCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class tranType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tranType':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class action(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'action':
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
            accountId = schemas.Int64Schema
            
            
            class refAccountId(
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
                ) -> 'refAccountId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            contactId = schemas.Int64Schema
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
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
            isTrust = schemas.BoolSchema
            realAmount = schemas.Float64Schema
            amount = schemas.Float64Schema
            feeAmount = schemas.Float64Schema
            feeReal = schemas.Float64Schema
        
            @staticmethod
            def approval() -> typing.Type['ApprovalModel']:
                return ApprovalModel
            
            
            class status(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'status':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "tranHeadId": tranHeadId,
                "date": date,
                "reference": reference,
                "tranTypeCode": tranTypeCode,
                "tranType": tranType,
                "action": action,
                "name": name,
                "accountId": accountId,
                "refAccountId": refAccountId,
                "contactId": contactId,
                "description": description,
                "currencyCode": currencyCode,
                "symbol": symbol,
                "isTrust": isTrust,
                "realAmount": realAmount,
                "amount": amount,
                "feeAmount": feeAmount,
                "feeReal": feeReal,
                "approval": approval,
                "status": status,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tranHeadId"]) -> MetaOapg.properties.tranHeadId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tranTypeCode"]) -> MetaOapg.properties.tranTypeCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tranType"]) -> MetaOapg.properties.tranType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountId"]) -> MetaOapg.properties.accountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refAccountId"]) -> MetaOapg.properties.refAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactId"]) -> MetaOapg.properties.contactId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyCode"]) -> MetaOapg.properties.currencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbol"]) -> MetaOapg.properties.symbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isTrust"]) -> MetaOapg.properties.isTrust: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["realAmount"]) -> MetaOapg.properties.realAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeAmount"]) -> MetaOapg.properties.feeAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feeReal"]) -> MetaOapg.properties.feeReal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approval"]) -> 'ApprovalModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["tranHeadId"], typing_extensions.Literal["date"], typing_extensions.Literal["reference"], typing_extensions.Literal["tranTypeCode"], typing_extensions.Literal["tranType"], typing_extensions.Literal["action"], typing_extensions.Literal["name"], typing_extensions.Literal["accountId"], typing_extensions.Literal["refAccountId"], typing_extensions.Literal["contactId"], typing_extensions.Literal["description"], typing_extensions.Literal["currencyCode"], typing_extensions.Literal["symbol"], typing_extensions.Literal["isTrust"], typing_extensions.Literal["realAmount"], typing_extensions.Literal["amount"], typing_extensions.Literal["feeAmount"], typing_extensions.Literal["feeReal"], typing_extensions.Literal["approval"], typing_extensions.Literal["status"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tranHeadId"]) -> typing.Union[MetaOapg.properties.tranHeadId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tranTypeCode"]) -> typing.Union[MetaOapg.properties.tranTypeCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tranType"]) -> typing.Union[MetaOapg.properties.tranType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountId"]) -> typing.Union[MetaOapg.properties.accountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refAccountId"]) -> typing.Union[MetaOapg.properties.refAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactId"]) -> typing.Union[MetaOapg.properties.contactId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyCode"]) -> typing.Union[MetaOapg.properties.currencyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbol"]) -> typing.Union[MetaOapg.properties.symbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isTrust"]) -> typing.Union[MetaOapg.properties.isTrust, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["realAmount"]) -> typing.Union[MetaOapg.properties.realAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeAmount"]) -> typing.Union[MetaOapg.properties.feeAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feeReal"]) -> typing.Union[MetaOapg.properties.feeReal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approval"]) -> typing.Union['ApprovalModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["tranHeadId"], typing_extensions.Literal["date"], typing_extensions.Literal["reference"], typing_extensions.Literal["tranTypeCode"], typing_extensions.Literal["tranType"], typing_extensions.Literal["action"], typing_extensions.Literal["name"], typing_extensions.Literal["accountId"], typing_extensions.Literal["refAccountId"], typing_extensions.Literal["contactId"], typing_extensions.Literal["description"], typing_extensions.Literal["currencyCode"], typing_extensions.Literal["symbol"], typing_extensions.Literal["isTrust"], typing_extensions.Literal["realAmount"], typing_extensions.Literal["amount"], typing_extensions.Literal["feeAmount"], typing_extensions.Literal["feeReal"], typing_extensions.Literal["approval"], typing_extensions.Literal["status"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        tranHeadId: typing.Union[MetaOapg.properties.tranHeadId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, datetime, schemas.Unset] = schemas.unset,
        reference: typing.Union[MetaOapg.properties.reference, None, str, schemas.Unset] = schemas.unset,
        tranTypeCode: typing.Union[MetaOapg.properties.tranTypeCode, None, str, schemas.Unset] = schemas.unset,
        tranType: typing.Union[MetaOapg.properties.tranType, None, str, schemas.Unset] = schemas.unset,
        action: typing.Union[MetaOapg.properties.action, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        accountId: typing.Union[MetaOapg.properties.accountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        refAccountId: typing.Union[MetaOapg.properties.refAccountId, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        contactId: typing.Union[MetaOapg.properties.contactId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        currencyCode: typing.Union[MetaOapg.properties.currencyCode, None, str, schemas.Unset] = schemas.unset,
        symbol: typing.Union[MetaOapg.properties.symbol, None, str, schemas.Unset] = schemas.unset,
        isTrust: typing.Union[MetaOapg.properties.isTrust, bool, schemas.Unset] = schemas.unset,
        realAmount: typing.Union[MetaOapg.properties.realAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        feeAmount: typing.Union[MetaOapg.properties.feeAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        feeReal: typing.Union[MetaOapg.properties.feeReal, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        approval: typing.Union['ApprovalModel', schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WalletTranModel':
        return super().__new__(
            cls,
            *_args,
            id=id,
            tranHeadId=tranHeadId,
            date=date,
            reference=reference,
            tranTypeCode=tranTypeCode,
            tranType=tranType,
            action=action,
            name=name,
            accountId=accountId,
            refAccountId=refAccountId,
            contactId=contactId,
            description=description,
            currencyCode=currencyCode,
            symbol=symbol,
            isTrust=isTrust,
            realAmount=realAmount,
            amount=amount,
            feeAmount=feeAmount,
            feeReal=feeReal,
            approval=approval,
            status=status,
            _configuration=_configuration,
        )

from xprizo_sdk_py.model.approval_model import ApprovalModel
