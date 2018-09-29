# flake8-type-annotations

[![wemake.services](https://img.shields.io/badge/-wemake.services-green.svg?label=%20&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAABGdBTUEAALGPC%2FxhBQAAAAFzUkdCAK7OHOkAAAAbUExURQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP%2F%2F%2F5TvxDIAAAAIdFJOUwAjRA8xXANAL%2Bv0SAAAADNJREFUGNNjYCAIOJjRBdBFWMkVQeGzcHAwksJnAPPZGOGAASzPzAEHEGVsLExQwE7YswCb7AFZSF3bbAAAAABJRU5ErkJggg%3D%3D)](https://wemake.services) [![Build Status](https://travis-ci.org/sobolevn/flake8-type-annotations.svg?branch=master)](https://travis-ci.org/sobolevn/flake8-type-annotations) [![Coverage](https://coveralls.io/repos/github/sobolevn/flake8-type-annotations/badge.svg?branch=master)](https://coveralls.io/github/sobolevn/flake8-type-annotations?branch=master) [![Python Version](https://img.shields.io/pypi/pyversions/flake8-type-annotations.svg)](https://pypi.org/project/flake8-type-annotations/) [![PyPI version](https://badge.fury.io/py/flake8-type-annotations.svg)](https://pypi.org/project/flake8-type-annotations/)

This tool is used to validate type annotations syntax
as it was [originally proposed](https://github.com/PyCQA/pycodestyle/issues/357)
by [Guido van Rossum](https://github.com/gvanrossum).

## Installation

```bash
pip install flake8-type-annotations
```

## Code example

```python
# Consistency with this plugin:
def function(param=0, other: int = 0) -> int:
    return param + other


# Possible errors without this plugin:
def function(param=0, other: int=0)->int:
    return param + other
```

## Error codes

| Error code |                          Description                          |
|:----------:|:-------------------------------------------------------------:|
|    T800    | Missing spaces between parameter annotation and default value |
|    T801    | Missing spaces in return type annotation                      |

## License

MIT.
