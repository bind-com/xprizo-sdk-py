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


class ContactBusinessModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
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
            
            
            class tradingName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tradingName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class taxNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'taxNumber':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class taxCountryCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'taxCountryCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class regName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'regName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class regNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'regNumber':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class regDate(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'regDate':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class contactPerson(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'contactPerson':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class phoneBusiness(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phoneBusiness':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "hashId": hashId,
                "tradingName": tradingName,
                "taxNumber": taxNumber,
                "taxCountryCode": taxCountryCode,
                "regName": regName,
                "regNumber": regNumber,
                "regDate": regDate,
                "contactPerson": contactPerson,
                "phoneBusiness": phoneBusiness,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hashId"]) -> MetaOapg.properties.hashId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tradingName"]) -> MetaOapg.properties.tradingName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxNumber"]) -> MetaOapg.properties.taxNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCountryCode"]) -> MetaOapg.properties.taxCountryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regName"]) -> MetaOapg.properties.regName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regNumber"]) -> MetaOapg.properties.regNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regDate"]) -> MetaOapg.properties.regDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactPerson"]) -> MetaOapg.properties.contactPerson: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneBusiness"]) -> MetaOapg.properties.phoneBusiness: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hashId"], typing_extensions.Literal["tradingName"], typing_extensions.Literal["taxNumber"], typing_extensions.Literal["taxCountryCode"], typing_extensions.Literal["regName"], typing_extensions.Literal["regNumber"], typing_extensions.Literal["regDate"], typing_extensions.Literal["contactPerson"], typing_extensions.Literal["phoneBusiness"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hashId"]) -> typing.Union[MetaOapg.properties.hashId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tradingName"]) -> typing.Union[MetaOapg.properties.tradingName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxNumber"]) -> typing.Union[MetaOapg.properties.taxNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCountryCode"]) -> typing.Union[MetaOapg.properties.taxCountryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regName"]) -> typing.Union[MetaOapg.properties.regName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regNumber"]) -> typing.Union[MetaOapg.properties.regNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regDate"]) -> typing.Union[MetaOapg.properties.regDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactPerson"]) -> typing.Union[MetaOapg.properties.contactPerson, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneBusiness"]) -> typing.Union[MetaOapg.properties.phoneBusiness, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hashId"], typing_extensions.Literal["tradingName"], typing_extensions.Literal["taxNumber"], typing_extensions.Literal["taxCountryCode"], typing_extensions.Literal["regName"], typing_extensions.Literal["regNumber"], typing_extensions.Literal["regDate"], typing_extensions.Literal["contactPerson"], typing_extensions.Literal["phoneBusiness"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        hashId: typing.Union[MetaOapg.properties.hashId, None, str, schemas.Unset] = schemas.unset,
        tradingName: typing.Union[MetaOapg.properties.tradingName, None, str, schemas.Unset] = schemas.unset,
        taxNumber: typing.Union[MetaOapg.properties.taxNumber, None, str, schemas.Unset] = schemas.unset,
        taxCountryCode: typing.Union[MetaOapg.properties.taxCountryCode, None, str, schemas.Unset] = schemas.unset,
        regName: typing.Union[MetaOapg.properties.regName, None, str, schemas.Unset] = schemas.unset,
        regNumber: typing.Union[MetaOapg.properties.regNumber, None, str, schemas.Unset] = schemas.unset,
        regDate: typing.Union[MetaOapg.properties.regDate, None, str, schemas.Unset] = schemas.unset,
        contactPerson: typing.Union[MetaOapg.properties.contactPerson, None, str, schemas.Unset] = schemas.unset,
        phoneBusiness: typing.Union[MetaOapg.properties.phoneBusiness, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ContactBusinessModel':
        return super().__new__(
            cls,
            *_args,
            hashId=hashId,
            tradingName=tradingName,
            taxNumber=taxNumber,
            taxCountryCode=taxCountryCode,
            regName=regName,
            regNumber=regNumber,
            regDate=regDate,
            contactPerson=contactPerson,
            phoneBusiness=phoneBusiness,
            _configuration=_configuration,
        )
