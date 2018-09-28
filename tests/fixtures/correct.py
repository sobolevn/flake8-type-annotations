# -*- coding: utf-8 -*-

"""Module with correct type annotations."""


def _typed_function(first: int, second: int = 0) -> int:
    return first + second


def _typed_with_default(first=0, second: int = 0) -> int:
    return first + second


def _typed_multiline(
    first=0,
    second: bool = True,
) -> int:
    return first if second else -first


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
