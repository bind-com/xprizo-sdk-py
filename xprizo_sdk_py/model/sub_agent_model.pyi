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


class SubAgentModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            profileId = schemas.Int64Schema
            id = schemas.Int64Schema
            
            
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
            commission = schemas.Float64Schema
            isSharedWallet = schemas.BoolSchema
            
            
            class taskId(
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
                ) -> 'taskId':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
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
                "profileId": profileId,
                "id": id,
                "name": name,
                "commission": commission,
                "isSharedWallet": isSharedWallet,
                "taskId": taskId,
                "status": status,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profileId"]) -> MetaOapg.properties.profileId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commission"]) -> MetaOapg.properties.commission: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isSharedWallet"]) -> MetaOapg.properties.isSharedWallet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["taskId"]) -> MetaOapg.properties.taskId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["profileId"], typing_extensions.Literal["id"], typing_extensions.Literal["name"], typing_extensions.Literal["commission"], typing_extensions.Literal["isSharedWallet"], typing_extensions.Literal["taskId"], typing_extensions.Literal["status"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profileId"]) -> typing.Union[MetaOapg.properties.profileId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commission"]) -> typing.Union[MetaOapg.properties.commission, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isSharedWallet"]) -> typing.Union[MetaOapg.properties.isSharedWallet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["taskId"]) -> typing.Union[MetaOapg.properties.taskId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["profileId"], typing_extensions.Literal["id"], typing_extensions.Literal["name"], typing_extensions.Literal["commission"], typing_extensions.Literal["isSharedWallet"], typing_extensions.Literal["taskId"], typing_extensions.Literal["status"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        profileId: typing.Union[MetaOapg.properties.profileId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        commission: typing.Union[MetaOapg.properties.commission, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        isSharedWallet: typing.Union[MetaOapg.properties.isSharedWallet, bool, schemas.Unset] = schemas.unset,
        taskId: typing.Union[MetaOapg.properties.taskId, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SubAgentModel':
        return super().__new__(
            cls,
            *_args,
            profileId=profileId,
            id=id,
            name=name,
            commission=commission,
            isSharedWallet=isSharedWallet,
            taskId=taskId,
            status=status,
            _configuration=_configuration,
        )
