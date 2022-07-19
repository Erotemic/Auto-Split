""" # noqa Y021
This type stub file was generated by pyright.

NOTE:
Apparently Pillow support on Ubuntu 64-bit has several additional steps since it doesn't have JPEG/PNG support out of the box. Description here:

https://stackoverflow.com/questions/7648200/pip-install-pil-e-tickets-1-no-jpeg-png-support
http://ubuntuforums.org/showthread.php?t=1751455
"""

# import collections
# import datetime
# import errno
# import functools
# import os
# import subprocess
# import time
# from contextlib import contextmanager
import sys
from collections.abc import Callable, Generator
from typing import NamedTuple

import cv2
from PIL.Image import Image

__version__: str = ...
useOpenCV: bool
RUNNING_PYTHON_2 = sys.version_info[0] == 2
RUNNING_CV_2: bool = ...
LOAD_COLOR = cv2.IMREAD_COLOR
LOAD_GRAYSCALE = cv2.IMREAD_GRAYSCALE
if sys.version_info[0] != 2:
    unicode = str
_PYGETWINDOW_UNAVAILABLE: bool = ...
GRAYSCALE_DEFAULT: bool = ...
USE_IMAGE_NOT_FOUND_EXCEPTION: bool = ...
scrotExists: bool = ...
Box = NamedTuple('Box', 'left top width height')
Point = NamedTuple('Point', 'x y')
RGB = NamedTuple('RGB', 'red green blue')


class PyScreezeException(Exception):
    ...


class ImageNotFoundException(PyScreezeException):
    ...


def requiresPillow(wrappedFunction) -> Callable:
    ...


def locate(needleImage, haystackImage, **kwargs) -> Box | None:
    ...


def locateOnScreen(image, minSearchTime=..., **kwargs):
    ...


def locateAllOnScreen(image, **kwargs) -> Generator[Box, None, None]:
    ...


def locateCenterOnScreen(image, **kwargs) -> Point | None:
    ...


def locateOnWindow(image, title, **kwargs):
    ...


@requiresPillow
def showRegionOnScreen(region, outlineColor=..., filename=...) -> None:
    ...


def center(coords) -> Point:
    ...


def pixelMatchesColor(x, y, expectedRGBColor, tolerance=...):
    ...


def pixel(x, y) -> RGB:
    ...


def screenshot(imageFilename: Unknown | None = ..., region: Unknown | None = ...) -> Image:
    ...


grab = screenshot


def locateAll(
    needleImage: Unknown,
    haystackImage: Unknown,
    grayscale: Unknown | None = ...,
    limit: int = ...,
    region: Unknown | None = ...,
    step: int = ...,
    confidence: float = ...
) -> Generator[Box, None, None]:
    ...
