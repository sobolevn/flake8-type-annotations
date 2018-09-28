# -*- coding: utf-8 -*-

import tokenize
from typing import Generator, Tuple, Sequence

import pkg_resources
from pycodestyle import STARTSWITH_DEF_REGEX

pkg_name = 'flake8-type-annotations'

#: We store the version number inside the `pyproject.toml`:
pkg_version: str = pkg_resources.get_distribution(pkg_name).version

STDIN = 'stdin'


def _validate_parameters(
    tokens: Sequence[tokenize.TokenInfo],
) -> Generator[int, None, None]:
    for index, token in enumerate(tokens):
        if token.exact_type == tokenize.EQUAL:
            _, previous_end = tokens[index - 1].end
            _, next_start = tokens[index + 1].start
            if next_start - previous_end < len(' = '):
               yield token.start


def _validate_return_type(
    tokens: Sequence[tokenize.TokenInfo],
) -> Generator[int, None, None]:
    for index, token in enumerate(tokens):
        if token.string == '->':
            _, previous_end = tokens[index - 1].end
            _, next_start = tokens[index + 1].start
            if next_start - previous_end < len(' -> '):
               yield token.start


class Checker(object):
    """Flake8 plugin to find incorrect type annotation styles."""

    name = pkg_name
    version = pkg_version

    T800 = (
        'T800: Missing spaces between parameter '
        'annotation and default value'
    )
    T801 = 'T801: Missing spaces in return type annotation'

    def __init__(
        self,
        logical_line: str,
        tokens: Sequence[tokenize.TokenInfo],
        filename: str = STDIN,
        simple: int = 12,
    ) -> None:
        """
        Creates new checker instance.

        We need both tree and tokenize sequence, since it is sometimes
        easier to get the information from ``ast`` and sometimes it is easier
        to get the information from ``tokenize`` sources.
        """
        self.logical_line = logical_line
        self.tokens = tokens
        self.filename = filename

    def __iter__(self) -> Generator[Tuple[int, str], None, None]:
        if STARTSWITH_DEF_REGEX.match(self.logical_line):
            for offset in _validate_parameters(self.tokens):
                yield offset, self.T800

            for offset in _validate_return_type(self.tokens):
                yield offset, self.T801
