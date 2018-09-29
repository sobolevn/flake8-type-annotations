# -*- coding: utf-8 -*-

import tokenize
from typing import Generator, Sequence, Tuple

import pkg_resources
from pycodestyle import STARTSWITH_DEF_REGEX

pkg_name = 'flake8-type-annotations'

#: We store the version number inside the `pyproject.toml`:
pkg_version: str = pkg_resources.get_distribution(pkg_name).version


CORRECT_PATTERN = ' {0} '
EQUAL = '='
ARROW = '->'


def _get_boundaries(
    tokens: Sequence[tokenize.TokenInfo],
    index: int,
) -> Tuple[int, int]:
    _, previous_end = tokens[index - 1].end
    _, next_start = tokens[index + 1].start
    return previous_end, next_start


def _count_parens(token: tokenize.TokenInfo) -> int:
    if token.exact_type in (tokenize.LPAR, tokenize.LSQB):
        return 1
    if token.exact_type in (tokenize.RPAR, tokenize.RSQB):
        return -1
    return 0


def _validate_parameters(
    tokens: Sequence[tokenize.TokenInfo],
) -> Generator[Tuple[int, int], None, None]:
    parens = 0
    annotated_func_arg = False

    for index, token in enumerate(tokens):
        parens += _count_parens(token)

        if token.exact_type == tokenize.COLON and parens == 1:
            annotated_func_arg = True
        elif token.exact_type == tokenize.COMMA and parens == 1:
            annotated_func_arg = False

        if annotated_func_arg and token.exact_type == tokenize.EQUAL:
            previous_end, next_start = _get_boundaries(tokens, index)
            if next_start - previous_end < len(CORRECT_PATTERN.format(EQUAL)):
                yield token.start


def _validate_return_type(
    tokens: Sequence[tokenize.TokenInfo],
) -> Generator[Tuple[int, int], None, None]:
    for index, token in enumerate(tokens):
        if token.string == ARROW:  # there's no operator for `->` in tokenize
            previous_end, next_start = _get_boundaries(tokens, index)
            if next_start - previous_end < len(CORRECT_PATTERN.format(ARROW)):
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
    ) -> None:
        """
        Creates new checker instance.

        We need both tree and tokenize sequence, since it is sometimes
        easier to get the information from ``ast`` and sometimes it is easier
        to get the information from ``tokenize`` sources.
        """
        self.logical_line = logical_line
        self.tokens = tokens

    def __iter__(self) -> Generator[Tuple[Tuple[int, int], str], None, None]:
        """Called by ``flake8`` on each logical line in a file."""
        if STARTSWITH_DEF_REGEX.match(self.logical_line):
            for offset in _validate_parameters(self.tokens):
                yield offset, self.T800

            for offset in _validate_return_type(self.tokens):
                yield offset, self.T801
