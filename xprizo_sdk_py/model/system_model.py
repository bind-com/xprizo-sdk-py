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


class SystemModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
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
            major = schemas.Int32Schema
            minor = schemas.Int32Schema
            buildNo = schemas.Int32Schema
            
            
            class copyright(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'copyright':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class messagingServer(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'messagingServer':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "name": name,
                "major": major,
                "minor": minor,
                "buildNo": buildNo,
                "copyright": copyright,
                "messagingServer": messagingServer,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["major"]) -> MetaOapg.properties.major: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minor"]) -> MetaOapg.properties.minor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buildNo"]) -> MetaOapg.properties.buildNo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["copyright"]) -> MetaOapg.properties.copyright: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messagingServer"]) -> MetaOapg.properties.messagingServer: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["major"], typing_extensions.Literal["minor"], typing_extensions.Literal["buildNo"], typing_extensions.Literal["copyright"], typing_extensions.Literal["messagingServer"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["major"]) -> typing.Union[MetaOapg.properties.major, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minor"]) -> typing.Union[MetaOapg.properties.minor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buildNo"]) -> typing.Union[MetaOapg.properties.buildNo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["copyright"]) -> typing.Union[MetaOapg.properties.copyright, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messagingServer"]) -> typing.Union[MetaOapg.properties.messagingServer, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name"], typing_extensions.Literal["major"], typing_extensions.Literal["minor"], typing_extensions.Literal["buildNo"], typing_extensions.Literal["copyright"], typing_extensions.Literal["messagingServer"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, None, str, schemas.Unset] = schemas.unset,
        major: typing.Union[MetaOapg.properties.major, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        minor: typing.Union[MetaOapg.properties.minor, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        buildNo: typing.Union[MetaOapg.properties.buildNo, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        copyright: typing.Union[MetaOapg.properties.copyright, None, str, schemas.Unset] = schemas.unset,
        messagingServer: typing.Union[MetaOapg.properties.messagingServer, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SystemModel':
        return super().__new__(
            cls,
            *_args,
            name=name,
            major=major,
            minor=minor,
            buildNo=buildNo,
            copyright=copyright,
            messagingServer=messagingServer,
            _configuration=_configuration,
        )
