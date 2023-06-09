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


class ReportModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class type(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'type':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
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
        
            @staticmethod
            def heading() -> typing.Type['ReportHeadingModel']:
                return ReportHeadingModel
            
            
            class columns(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ReportColumnModel']:
                        return ReportColumnModel
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'columns':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            isLandscape = schemas.BoolSchema
            isFitToPage = schemas.BoolSchema
            isDefault = schemas.BoolSchema
            __annotations__ = {
                "type": type,
                "description": description,
                "heading": heading,
                "columns": columns,
                "isLandscape": isLandscape,
                "isFitToPage": isFitToPage,
                "isDefault": isDefault,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heading"]) -> 'ReportHeadingModel': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isLandscape"]) -> MetaOapg.properties.isLandscape: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isFitToPage"]) -> MetaOapg.properties.isFitToPage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isDefault"]) -> MetaOapg.properties.isDefault: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["description"], typing_extensions.Literal["heading"], typing_extensions.Literal["columns"], typing_extensions.Literal["isLandscape"], typing_extensions.Literal["isFitToPage"], typing_extensions.Literal["isDefault"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heading"]) -> typing.Union['ReportHeadingModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columns"]) -> typing.Union[MetaOapg.properties.columns, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isLandscape"]) -> typing.Union[MetaOapg.properties.isLandscape, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isFitToPage"]) -> typing.Union[MetaOapg.properties.isFitToPage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isDefault"]) -> typing.Union[MetaOapg.properties.isDefault, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type"], typing_extensions.Literal["description"], typing_extensions.Literal["heading"], typing_extensions.Literal["columns"], typing_extensions.Literal["isLandscape"], typing_extensions.Literal["isFitToPage"], typing_extensions.Literal["isDefault"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, None, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        heading: typing.Union['ReportHeadingModel', schemas.Unset] = schemas.unset,
        columns: typing.Union[MetaOapg.properties.columns, list, tuple, None, schemas.Unset] = schemas.unset,
        isLandscape: typing.Union[MetaOapg.properties.isLandscape, bool, schemas.Unset] = schemas.unset,
        isFitToPage: typing.Union[MetaOapg.properties.isFitToPage, bool, schemas.Unset] = schemas.unset,
        isDefault: typing.Union[MetaOapg.properties.isDefault, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ReportModel':
        return super().__new__(
            cls,
            *_args,
            type=type,
            description=description,
            heading=heading,
            columns=columns,
            isLandscape=isLandscape,
            isFitToPage=isFitToPage,
            isDefault=isDefault,
            _configuration=_configuration,
        )

from xprizo_sdk_py.model.report_column_model import ReportColumnModel
from xprizo_sdk_py.model.report_heading_model import ReportHeadingModel
