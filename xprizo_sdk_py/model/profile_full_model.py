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


class ProfileFullModel(
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
            
            
            class role(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'role':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            isInactive = schemas.BoolSchema
            isSuspended = schemas.BoolSchema
            isAgent = schemas.BoolSchema
            isUnlocked = schemas.BoolSchema
            usePaymentPin = schemas.BoolSchema
            
            
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
        
            @staticmethod
            def contact() -> typing.Type['ContactModel']:
                return ContactModel
        
            @staticmethod
            def preference() -> typing.Type['PreferenceModel']:
                return PreferenceModel
            
            
            class userWallets(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WalletAccountModel']:
                        return WalletAccountModel
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'userWallets':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class savingWallets(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WalletAccountModel']:
                        return WalletAccountModel
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'savingWallets':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class agentWallets(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['WalletAccountModel']:
                        return WalletAccountModel
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'agentWallets':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class linkedWallets(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['LinkedWalletModel']:
                        return LinkedWalletModel
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'linkedWallets':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "hashId": hashId,
                "name": name,
                "role": role,
                "isInactive": isInactive,
                "isSuspended": isSuspended,
                "isAgent": isAgent,
                "isUnlocked": isUnlocked,
                "usePaymentPin": usePaymentPin,
                "lastLogin": lastLogin,
                "registeredOn": registeredOn,
                "recruitedOn": recruitedOn,
                "contact": contact,
                "preference": preference,
                "userWallets": userWallets,
                "savingWallets": savingWallets,
                "agentWallets": agentWallets,
                "linkedWallets": linkedWallets,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hashId"]) -> MetaOapg.properties.hashId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isInactive"]) -> MetaOapg.properties.isInactive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSuspended"]) -> MetaOapg.properties.isSuspended: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isAgent"]) -> MetaOapg.properties.isAgent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isUnlocked"]) -> MetaOapg.properties.isUnlocked: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["usePaymentPin"]) -> MetaOapg.properties.usePaymentPin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastLogin"]) -> MetaOapg.properties.lastLogin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["registeredOn"]) -> MetaOapg.properties.registeredOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recruitedOn"]) -> MetaOapg.properties.recruitedOn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact"]) -> 'ContactModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["preference"]) -> 'PreferenceModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userWallets"]) -> MetaOapg.properties.userWallets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["savingWallets"]) -> MetaOapg.properties.savingWallets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["agentWallets"]) -> MetaOapg.properties.agentWallets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linkedWallets"]) -> MetaOapg.properties.linkedWallets: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["hashId"], typing_extensions.Literal["name"], typing_extensions.Literal["role"], typing_extensions.Literal["isInactive"], typing_extensions.Literal["isSuspended"], typing_extensions.Literal["isAgent"], typing_extensions.Literal["isUnlocked"], typing_extensions.Literal["usePaymentPin"], typing_extensions.Literal["lastLogin"], typing_extensions.Literal["registeredOn"], typing_extensions.Literal["recruitedOn"], typing_extensions.Literal["contact"], typing_extensions.Literal["preference"], typing_extensions.Literal["userWallets"], typing_extensions.Literal["savingWallets"], typing_extensions.Literal["agentWallets"], typing_extensions.Literal["linkedWallets"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hashId"]) -> typing.Union[MetaOapg.properties.hashId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> typing.Union[MetaOapg.properties.role, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isInactive"]) -> typing.Union[MetaOapg.properties.isInactive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSuspended"]) -> typing.Union[MetaOapg.properties.isSuspended, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isAgent"]) -> typing.Union[MetaOapg.properties.isAgent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isUnlocked"]) -> typing.Union[MetaOapg.properties.isUnlocked, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["usePaymentPin"]) -> typing.Union[MetaOapg.properties.usePaymentPin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastLogin"]) -> typing.Union[MetaOapg.properties.lastLogin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["registeredOn"]) -> typing.Union[MetaOapg.properties.registeredOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recruitedOn"]) -> typing.Union[MetaOapg.properties.recruitedOn, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact"]) -> typing.Union['ContactModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["preference"]) -> typing.Union['PreferenceModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userWallets"]) -> typing.Union[MetaOapg.properties.userWallets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["savingWallets"]) -> typing.Union[MetaOapg.properties.savingWallets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["agentWallets"]) -> typing.Union[MetaOapg.properties.agentWallets, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linkedWallets"]) -> typing.Union[MetaOapg.properties.linkedWallets, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id"], typing_extensions.Literal["hashId"], typing_extensions.Literal["name"], typing_extensions.Literal["role"], typing_extensions.Literal["isInactive"], typing_extensions.Literal["isSuspended"], typing_extensions.Literal["isAgent"], typing_extensions.Literal["isUnlocked"], typing_extensions.Literal["usePaymentPin"], typing_extensions.Literal["lastLogin"], typing_extensions.Literal["registeredOn"], typing_extensions.Literal["recruitedOn"], typing_extensions.Literal["contact"], typing_extensions.Literal["preference"], typing_extensions.Literal["userWallets"], typing_extensions.Literal["savingWallets"], typing_extensions.Literal["agentWallets"], typing_extensions.Literal["linkedWallets"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hashId: typing.Union[MetaOapg.properties.hashId, None, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        role: typing.Union[MetaOapg.properties.role, None, str, schemas.Unset] = schemas.unset,
        isInactive: typing.Union[MetaOapg.properties.isInactive, bool, schemas.Unset] = schemas.unset,
        isSuspended: typing.Union[MetaOapg.properties.isSuspended, bool, schemas.Unset] = schemas.unset,
        isAgent: typing.Union[MetaOapg.properties.isAgent, bool, schemas.Unset] = schemas.unset,
        isUnlocked: typing.Union[MetaOapg.properties.isUnlocked, bool, schemas.Unset] = schemas.unset,
        usePaymentPin: typing.Union[MetaOapg.properties.usePaymentPin, bool, schemas.Unset] = schemas.unset,
        lastLogin: typing.Union[MetaOapg.properties.lastLogin, None, str, datetime, schemas.Unset] = schemas.unset,
        registeredOn: typing.Union[MetaOapg.properties.registeredOn, None, str, datetime, schemas.Unset] = schemas.unset,
        recruitedOn: typing.Union[MetaOapg.properties.recruitedOn, None, str, datetime, schemas.Unset] = schemas.unset,
        contact: typing.Union['ContactModel', schemas.Unset] = schemas.unset,
        preference: typing.Union['PreferenceModel', schemas.Unset] = schemas.unset,
        userWallets: typing.Union[MetaOapg.properties.userWallets, list, tuple, None, schemas.Unset] = schemas.unset,
        savingWallets: typing.Union[MetaOapg.properties.savingWallets, list, tuple, None, schemas.Unset] = schemas.unset,
        agentWallets: typing.Union[MetaOapg.properties.agentWallets, list, tuple, None, schemas.Unset] = schemas.unset,
        linkedWallets: typing.Union[MetaOapg.properties.linkedWallets, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ProfileFullModel':
        return super().__new__(
            cls,
            *_args,
            id=id,
            hashId=hashId,
            name=name,
            role=role,
            isInactive=isInactive,
            isSuspended=isSuspended,
            isAgent=isAgent,
            isUnlocked=isUnlocked,
            usePaymentPin=usePaymentPin,
            lastLogin=lastLogin,
            registeredOn=registeredOn,
            recruitedOn=recruitedOn,
            contact=contact,
            preference=preference,
            userWallets=userWallets,
            savingWallets=savingWallets,
            agentWallets=agentWallets,
            linkedWallets=linkedWallets,
            _configuration=_configuration,
        )

from xprizo_sdk_py.model.contact_model import ContactModel
from xprizo_sdk_py.model.linked_wallet_model import LinkedWalletModel
from xprizo_sdk_py.model.preference_model import PreferenceModel
from xprizo_sdk_py.model.wallet_account_model import WalletAccountModel
