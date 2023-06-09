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


class ApprovalModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class key(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'key':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            approveById = schemas.Int64Schema
            ttl = schemas.Int64Schema
            expiryDate = schemas.DateTimeSchema
            
            
            class error(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'error':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "key": key,
                "approveById": approveById,
                "ttl": ttl,
                "expiryDate": expiryDate,
                "error": error,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["key"]) -> MetaOapg.properties.key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approveById"]) -> MetaOapg.properties.approveById: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ttl"]) -> MetaOapg.properties.ttl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryDate"]) -> MetaOapg.properties.expiryDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["key"], typing_extensions.Literal["approveById"], typing_extensions.Literal["ttl"], typing_extensions.Literal["expiryDate"], typing_extensions.Literal["error"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["key"]) -> typing.Union[MetaOapg.properties.key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approveById"]) -> typing.Union[MetaOapg.properties.approveById, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ttl"]) -> typing.Union[MetaOapg.properties.ttl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryDate"]) -> typing.Union[MetaOapg.properties.expiryDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["key"], typing_extensions.Literal["approveById"], typing_extensions.Literal["ttl"], typing_extensions.Literal["expiryDate"], typing_extensions.Literal["error"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        key: typing.Union[MetaOapg.properties.key, None, str, schemas.Unset] = schemas.unset,
        approveById: typing.Union[MetaOapg.properties.approveById, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ttl: typing.Union[MetaOapg.properties.ttl, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        expiryDate: typing.Union[MetaOapg.properties.expiryDate, str, datetime, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ApprovalModel':
        return super().__new__(
            cls,
            *_args,
            key=key,
            approveById=approveById,
            ttl=ttl,
            expiryDate=expiryDate,
            error=error,
            _configuration=_configuration,
        )
