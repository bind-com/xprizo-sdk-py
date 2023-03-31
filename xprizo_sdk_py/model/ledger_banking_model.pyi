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


class LedgerBankingModel(
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
            
            
            class accountName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accountName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class accountNo(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accountNo':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class bic(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bic':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class branch(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'branch':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class branchCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'branchCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class iban(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'iban':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class institution(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'institution':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class countryCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'countryCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "hashId": hashId,
                "name": name,
                "currencyCode": currencyCode,
                "accountName": accountName,
                "accountNo": accountNo,
                "bic": bic,
                "branch": branch,
                "branchCode": branchCode,
                "iban": iban,
                "institution": institution,
                "countryCode": countryCode,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hashId"]) -> MetaOapg.properties.hashId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyCode"]) -> MetaOapg.properties.currencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountName"]) -> MetaOapg.properties.accountName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountNo"]) -> MetaOapg.properties.accountNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bic"]) -> MetaOapg.properties.bic: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branch"]) -> MetaOapg.properties.branch: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["branchCode"]) -> MetaOapg.properties.branchCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["iban"]) -> MetaOapg.properties.iban: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["institution"]) -> MetaOapg.properties.institution: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["countryCode"]) -> MetaOapg.properties.countryCode: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["hashId"], typing_extensions.Literal["name"], typing_extensions.Literal["currencyCode"], typing_extensions.Literal["accountName"], typing_extensions.Literal["accountNo"], typing_extensions.Literal["bic"], typing_extensions.Literal["branch"], typing_extensions.Literal["branchCode"], typing_extensions.Literal["iban"], typing_extensions.Literal["institution"], typing_extensions.Literal["countryCode"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hashId"]) -> typing.Union[MetaOapg.properties.hashId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyCode"]) -> typing.Union[MetaOapg.properties.currencyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountName"]) -> typing.Union[MetaOapg.properties.accountName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountNo"]) -> typing.Union[MetaOapg.properties.accountNo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bic"]) -> typing.Union[MetaOapg.properties.bic, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branch"]) -> typing.Union[MetaOapg.properties.branch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["branchCode"]) -> typing.Union[MetaOapg.properties.branchCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["iban"]) -> typing.Union[MetaOapg.properties.iban, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["institution"]) -> typing.Union[MetaOapg.properties.institution, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["countryCode"]) -> typing.Union[MetaOapg.properties.countryCode, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["hashId"], typing_extensions.Literal["name"], typing_extensions.Literal["currencyCode"], typing_extensions.Literal["accountName"], typing_extensions.Literal["accountNo"], typing_extensions.Literal["bic"], typing_extensions.Literal["branch"], typing_extensions.Literal["branchCode"], typing_extensions.Literal["iban"], typing_extensions.Literal["institution"], typing_extensions.Literal["countryCode"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        hashId: typing.Union[MetaOapg.properties.hashId, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        currencyCode: typing.Union[MetaOapg.properties.currencyCode, None, str, schemas.Unset] = schemas.unset,
        accountName: typing.Union[MetaOapg.properties.accountName, None, str, schemas.Unset] = schemas.unset,
        accountNo: typing.Union[MetaOapg.properties.accountNo, None, str, schemas.Unset] = schemas.unset,
        bic: typing.Union[MetaOapg.properties.bic, None, str, schemas.Unset] = schemas.unset,
        branch: typing.Union[MetaOapg.properties.branch, None, str, schemas.Unset] = schemas.unset,
        branchCode: typing.Union[MetaOapg.properties.branchCode, None, str, schemas.Unset] = schemas.unset,
        iban: typing.Union[MetaOapg.properties.iban, None, str, schemas.Unset] = schemas.unset,
        institution: typing.Union[MetaOapg.properties.institution, None, str, schemas.Unset] = schemas.unset,
        countryCode: typing.Union[MetaOapg.properties.countryCode, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LedgerBankingModel':
        return super().__new__(
            cls,
            *_args,
            hashId=hashId,
            name=name,
            currencyCode=currencyCode,
            accountName=accountName,
            accountNo=accountNo,
            bic=bic,
            branch=branch,
            branchCode=branchCode,
            iban=iban,
            institution=institution,
            countryCode=countryCode,
            _configuration=_configuration,
        )
