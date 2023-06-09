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


class ContactModel(
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
            
            
            class email(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'email':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class mobile(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'mobile':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class phone(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phone':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class title(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'title':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class firstName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'firstName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class middleName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'middleName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class lastName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lastName':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class suffix(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'suffix':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class gender(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'gender':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class physicalCountryCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'physicalCountryCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class physicalStreet(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'physicalStreet':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class physicalCity(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'physicalCity':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class physicalStateProvince(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'physicalStateProvince':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class physicalZipPostalCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'physicalZipPostalCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class postalCountryCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postalCountryCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class postalStreet(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postalStreet':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class postalCity(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postalCity':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class postalStateProvince(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postalStateProvince':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class postalZipPostalCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postalZipPostalCode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class kycValidUntil(
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
                ) -> 'kycValidUntil':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            isKYCCompliant = schemas.BoolSchema
            
            
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
            __annotations__ = {
                "id": id,
                "hashId": hashId,
                "name": name,
                "email": email,
                "mobile": mobile,
                "phone": phone,
                "title": title,
                "firstName": firstName,
                "middleName": middleName,
                "lastName": lastName,
                "suffix": suffix,
                "gender": gender,
                "physicalCountryCode": physicalCountryCode,
                "physicalStreet": physicalStreet,
                "physicalCity": physicalCity,
                "physicalStateProvince": physicalStateProvince,
                "physicalZipPostalCode": physicalZipPostalCode,
                "postalCountryCode": postalCountryCode,
                "postalStreet": postalStreet,
                "postalCity": postalCity,
                "postalStateProvince": postalStateProvince,
                "postalZipPostalCode": postalZipPostalCode,
                "kycValidUntil": kycValidUntil,
                "isKYCCompliant": isKYCCompliant,
                "tradingName": tradingName,
                "taxCountryCode": taxCountryCode,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hashId"]) -> MetaOapg.properties.hashId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mobile"]) -> MetaOapg.properties.mobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middleName"]) -> MetaOapg.properties.middleName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suffix"]) -> MetaOapg.properties.suffix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gender"]) -> MetaOapg.properties.gender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["physicalCountryCode"]) -> MetaOapg.properties.physicalCountryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["physicalStreet"]) -> MetaOapg.properties.physicalStreet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["physicalCity"]) -> MetaOapg.properties.physicalCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["physicalStateProvince"]) -> MetaOapg.properties.physicalStateProvince: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["physicalZipPostalCode"]) -> MetaOapg.properties.physicalZipPostalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalCountryCode"]) -> MetaOapg.properties.postalCountryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalStreet"]) -> MetaOapg.properties.postalStreet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalCity"]) -> MetaOapg.properties.postalCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalStateProvince"]) -> MetaOapg.properties.postalStateProvince: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalZipPostalCode"]) -> MetaOapg.properties.postalZipPostalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kycValidUntil"]) -> MetaOapg.properties.kycValidUntil: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isKYCCompliant"]) -> MetaOapg.properties.isKYCCompliant: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tradingName"]) -> MetaOapg.properties.tradingName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taxCountryCode"]) -> MetaOapg.properties.taxCountryCode: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["hashId"], typing_extensions.Literal["name"], typing_extensions.Literal["email"], typing_extensions.Literal["mobile"], typing_extensions.Literal["phone"], typing_extensions.Literal["title"], typing_extensions.Literal["firstName"], typing_extensions.Literal["middleName"], typing_extensions.Literal["lastName"], typing_extensions.Literal["suffix"], typing_extensions.Literal["gender"], typing_extensions.Literal["physicalCountryCode"], typing_extensions.Literal["physicalStreet"], typing_extensions.Literal["physicalCity"], typing_extensions.Literal["physicalStateProvince"], typing_extensions.Literal["physicalZipPostalCode"], typing_extensions.Literal["postalCountryCode"], typing_extensions.Literal["postalStreet"], typing_extensions.Literal["postalCity"], typing_extensions.Literal["postalStateProvince"], typing_extensions.Literal["postalZipPostalCode"], typing_extensions.Literal["kycValidUntil"], typing_extensions.Literal["isKYCCompliant"], typing_extensions.Literal["tradingName"], typing_extensions.Literal["taxCountryCode"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hashId"]) -> typing.Union[MetaOapg.properties.hashId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mobile"]) -> typing.Union[MetaOapg.properties.mobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> typing.Union[MetaOapg.properties.title, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middleName"]) -> typing.Union[MetaOapg.properties.middleName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suffix"]) -> typing.Union[MetaOapg.properties.suffix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gender"]) -> typing.Union[MetaOapg.properties.gender, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["physicalCountryCode"]) -> typing.Union[MetaOapg.properties.physicalCountryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["physicalStreet"]) -> typing.Union[MetaOapg.properties.physicalStreet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["physicalCity"]) -> typing.Union[MetaOapg.properties.physicalCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["physicalStateProvince"]) -> typing.Union[MetaOapg.properties.physicalStateProvince, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["physicalZipPostalCode"]) -> typing.Union[MetaOapg.properties.physicalZipPostalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalCountryCode"]) -> typing.Union[MetaOapg.properties.postalCountryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalStreet"]) -> typing.Union[MetaOapg.properties.postalStreet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalCity"]) -> typing.Union[MetaOapg.properties.postalCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalStateProvince"]) -> typing.Union[MetaOapg.properties.postalStateProvince, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalZipPostalCode"]) -> typing.Union[MetaOapg.properties.postalZipPostalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kycValidUntil"]) -> typing.Union[MetaOapg.properties.kycValidUntil, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isKYCCompliant"]) -> typing.Union[MetaOapg.properties.isKYCCompliant, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tradingName"]) -> typing.Union[MetaOapg.properties.tradingName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taxCountryCode"]) -> typing.Union[MetaOapg.properties.taxCountryCode, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["hashId"], typing_extensions.Literal["name"], typing_extensions.Literal["email"], typing_extensions.Literal["mobile"], typing_extensions.Literal["phone"], typing_extensions.Literal["title"], typing_extensions.Literal["firstName"], typing_extensions.Literal["middleName"], typing_extensions.Literal["lastName"], typing_extensions.Literal["suffix"], typing_extensions.Literal["gender"], typing_extensions.Literal["physicalCountryCode"], typing_extensions.Literal["physicalStreet"], typing_extensions.Literal["physicalCity"], typing_extensions.Literal["physicalStateProvince"], typing_extensions.Literal["physicalZipPostalCode"], typing_extensions.Literal["postalCountryCode"], typing_extensions.Literal["postalStreet"], typing_extensions.Literal["postalCity"], typing_extensions.Literal["postalStateProvince"], typing_extensions.Literal["postalZipPostalCode"], typing_extensions.Literal["kycValidUntil"], typing_extensions.Literal["isKYCCompliant"], typing_extensions.Literal["tradingName"], typing_extensions.Literal["taxCountryCode"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hashId: typing.Union[MetaOapg.properties.hashId, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, None, str, schemas.Unset] = schemas.unset,
        mobile: typing.Union[MetaOapg.properties.mobile, None, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, None, str, schemas.Unset] = schemas.unset,
        title: typing.Union[MetaOapg.properties.title, None, str, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, None, str, schemas.Unset] = schemas.unset,
        middleName: typing.Union[MetaOapg.properties.middleName, None, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, None, str, schemas.Unset] = schemas.unset,
        suffix: typing.Union[MetaOapg.properties.suffix, None, str, schemas.Unset] = schemas.unset,
        gender: typing.Union[MetaOapg.properties.gender, None, str, schemas.Unset] = schemas.unset,
        physicalCountryCode: typing.Union[MetaOapg.properties.physicalCountryCode, None, str, schemas.Unset] = schemas.unset,
        physicalStreet: typing.Union[MetaOapg.properties.physicalStreet, None, str, schemas.Unset] = schemas.unset,
        physicalCity: typing.Union[MetaOapg.properties.physicalCity, None, str, schemas.Unset] = schemas.unset,
        physicalStateProvince: typing.Union[MetaOapg.properties.physicalStateProvince, None, str, schemas.Unset] = schemas.unset,
        physicalZipPostalCode: typing.Union[MetaOapg.properties.physicalZipPostalCode, None, str, schemas.Unset] = schemas.unset,
        postalCountryCode: typing.Union[MetaOapg.properties.postalCountryCode, None, str, schemas.Unset] = schemas.unset,
        postalStreet: typing.Union[MetaOapg.properties.postalStreet, None, str, schemas.Unset] = schemas.unset,
        postalCity: typing.Union[MetaOapg.properties.postalCity, None, str, schemas.Unset] = schemas.unset,
        postalStateProvince: typing.Union[MetaOapg.properties.postalStateProvince, None, str, schemas.Unset] = schemas.unset,
        postalZipPostalCode: typing.Union[MetaOapg.properties.postalZipPostalCode, None, str, schemas.Unset] = schemas.unset,
        kycValidUntil: typing.Union[MetaOapg.properties.kycValidUntil, None, str, datetime, schemas.Unset] = schemas.unset,
        isKYCCompliant: typing.Union[MetaOapg.properties.isKYCCompliant, bool, schemas.Unset] = schemas.unset,
        tradingName: typing.Union[MetaOapg.properties.tradingName, None, str, schemas.Unset] = schemas.unset,
        taxCountryCode: typing.Union[MetaOapg.properties.taxCountryCode, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ContactModel':
        return super().__new__(
            cls,
            *_args,
            id=id,
            hashId=hashId,
            name=name,
            email=email,
            mobile=mobile,
            phone=phone,
            title=title,
            firstName=firstName,
            middleName=middleName,
            lastName=lastName,
            suffix=suffix,
            gender=gender,
            physicalCountryCode=physicalCountryCode,
            physicalStreet=physicalStreet,
            physicalCity=physicalCity,
            physicalStateProvince=physicalStateProvince,
            physicalZipPostalCode=physicalZipPostalCode,
            postalCountryCode=postalCountryCode,
            postalStreet=postalStreet,
            postalCity=postalCity,
            postalStateProvince=postalStateProvince,
            postalZipPostalCode=postalZipPostalCode,
            kycValidUntil=kycValidUntil,
            isKYCCompliant=isKYCCompliant,
            tradingName=tradingName,
            taxCountryCode=taxCountryCode,
            _configuration=_configuration,
        )
