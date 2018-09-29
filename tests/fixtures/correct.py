# -*- coding: utf-8 -*-

"""Module with correct type annotations."""

from typing import Optional


def _untyped_function(first=0):
    return first


def _typed_function(first: int, second: int = 0) -> int:
    return first + second


def _typed_only_first_param(first: int, second=None) -> int:
    return first if second is None else 9


def _typed_with_default(first=0, second: int = 0) -> int:
    return first + second


def _typed_with_mutable(
    first={'key': 'value'},
    second: dict = {'other': 12},
    third: dict = {'some': 1, 'other': 2},
) -> None:
    """Do not use mutable defaults. This is done only for testing."""
    return None


def _typed_with_multiple_options(
    first: str = '+',
    second: Optional[str] = None,
) -> str:
    return first + second if second is not None else first


def _typed_multiline(
    first=0,
    second: bool = True,
) -> int:
    return first if second else -first


def _typed_with_strings(first: Optional['str'] = None) -> Optional['str']:
    return first


def _typed_with_raw_strings(first: 'str' = 'a') -> 'str':
    return first


class _TypedClass(object):
    def _typed_method(self, first: int, second: int = 0) -> int:
        return first + second

    def _typed_with_default(self, first=0, second: int = 0) -> int:
        return first + second

    def _typed_multiline(
        self,
        first=0,
        second: bool = True,
    ) -> int:
        return first if second else -first
