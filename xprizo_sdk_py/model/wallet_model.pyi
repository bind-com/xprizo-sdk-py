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


class WalletModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int64Schema
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
            isDefault = schemas.BoolSchema
            isMerchant = schemas.BoolSchema
            __annotations__ = {
                "id": id,
                "contactId": contactId,
                "contact": contact,
                "currencyCode": currencyCode,
                "name": name,
                "profilePicture": profilePicture,
                "isDefault": isDefault,
                "isMerchant": isMerchant,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contactId"]) -> MetaOapg.properties.contactId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact"]) -> MetaOapg.properties.contact: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currencyCode"]) -> MetaOapg.properties.currencyCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profilePicture"]) -> MetaOapg.properties.profilePicture: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isMerchant"]) -> MetaOapg.properties.isMerchant: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["contactId"], typing_extensions.Literal["contact"], typing_extensions.Literal["currencyCode"], typing_extensions.Literal["name"], typing_extensions.Literal["profilePicture"], typing_extensions.Literal["isDefault"], typing_extensions.Literal["isMerchant"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contactId"]) -> typing.Union[MetaOapg.properties.contactId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact"]) -> typing.Union[MetaOapg.properties.contact, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currencyCode"]) -> typing.Union[MetaOapg.properties.currencyCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profilePicture"]) -> typing.Union[MetaOapg.properties.profilePicture, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDefault"]) -> typing.Union[MetaOapg.properties.isDefault, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isMerchant"]) -> typing.Union[MetaOapg.properties.isMerchant, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["contactId"], typing_extensions.Literal["contact"], typing_extensions.Literal["currencyCode"], typing_extensions.Literal["name"], typing_extensions.Literal["profilePicture"], typing_extensions.Literal["isDefault"], typing_extensions.Literal["isMerchant"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        contactId: typing.Union[MetaOapg.properties.contactId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        contact: typing.Union[MetaOapg.properties.contact, None, str, schemas.Unset] = schemas.unset,
        currencyCode: typing.Union[MetaOapg.properties.currencyCode, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        profilePicture: typing.Union[MetaOapg.properties.profilePicture, None, str, schemas.Unset] = schemas.unset,
        isDefault: typing.Union[MetaOapg.properties.isDefault, bool, schemas.Unset] = schemas.unset,
        isMerchant: typing.Union[MetaOapg.properties.isMerchant, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'WalletModel':
        return super().__new__(
            cls,
            *_args,
            id=id,
            contactId=contactId,
            contact=contact,
            currencyCode=currencyCode,
            name=name,
            profilePicture=profilePicture,
            isDefault=isDefault,
            isMerchant=isMerchant,
            _configuration=_configuration,
        )
