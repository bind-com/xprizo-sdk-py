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


class UserRequestPaymentTransactionModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
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
            amount = schemas.Float64Schema
            fromAccountId = schemas.Int64Schema
            toAccountId = schemas.Int64Schema
            
            
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
            __annotations__ = {
                "description": description,
                "reference": reference,
                "amount": amount,
                "fromAccountId": fromAccountId,
                "toAccountId": toAccountId,
                "currencyCode": currencyCode,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromAccountId"]) -> MetaOapg.properties.fromAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toAccountId"]) -> MetaOapg.properties.toAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyCode"]) -> MetaOapg.properties.currencyCode: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description"], typing_extensions.Literal["reference"], typing_extensions.Literal["amount"], typing_extensions.Literal["fromAccountId"], typing_extensions.Literal["toAccountId"], typing_extensions.Literal["currencyCode"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> typing.Union[MetaOapg.properties.reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromAccountId"]) -> typing.Union[MetaOapg.properties.fromAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toAccountId"]) -> typing.Union[MetaOapg.properties.toAccountId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyCode"]) -> typing.Union[MetaOapg.properties.currencyCode, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description"], typing_extensions.Literal["reference"], typing_extensions.Literal["amount"], typing_extensions.Literal["fromAccountId"], typing_extensions.Literal["toAccountId"], typing_extensions.Literal["currencyCode"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        reference: typing.Union[MetaOapg.properties.reference, None, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        fromAccountId: typing.Union[MetaOapg.properties.fromAccountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        toAccountId: typing.Union[MetaOapg.properties.toAccountId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currencyCode: typing.Union[MetaOapg.properties.currencyCode, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'UserRequestPaymentTransactionModel':
        return super().__new__(
            cls,
            *_args,
            description=description,
            reference=reference,
            amount=amount,
            fromAccountId=fromAccountId,
            toAccountId=toAccountId,
            currencyCode=currencyCode,
            _configuration=_configuration,
        )
