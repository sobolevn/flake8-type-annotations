# -*- coding: utf-8 -*-

"""Module with incorrect type annotations."""

from typing import Optional


def _untyped_function(first = 0):  # noqa: E251
    return first


def _typed_function(first: int, second:int = 0)-> int:  # noqa: E231,T801
    return first + second


def _typed_with_default(first=0, second: int=0) ->int:  # noqa: T800,T801
    return first + second


def _typed_with_multiple_options(
    first: str= '+',  # noqa: T800
    second:Optional[str]= None,  # noqa: E231,T800
) ->str:  # noqa: T801
    return first + second if second is not None else first


def _typed_multiline(
    first= 0,  # noqa: E251
    second: bool=True,  # noqa: T800
    third = 0,  # noqa: E251
)->int:  # noqa: T801
    return first if second else third


def _typed_multiline_multiple_annotations(
    first =0,  # noqa: E251
    second: bool=True,  # noqa: T800
    third: int=0,  # noqa: T800
)->int:  # noqa: T801
    return first if second else third


def _typed_with_strings(first: Optional['str']= None) ->Optional['str']:  # noqa: T800, T801
    return first


def _typed_with_optional(first: Optional['str'] =None)-> Optional['str']:  # noqa: T800, T801
    return first


def _typed_with_raw_strings(first: 'str'='a')->'str':  # noqa: T800,T801
    return first


class _TypedClass(object):
    def _typed_method(self, first:int, second: int= 0) ->int:  # noqa: E231,T800,T801
        return first + second

    def _typed_with_default(self, first=0, second: int =0)-> int:  # noqa: T800,T801
        return first + second

    def _typed_multiline(
        self,
        first=0,
        second: bool=True,  # noqa: T800
    )->int:  # noqa: T801
        return first if second else -first
