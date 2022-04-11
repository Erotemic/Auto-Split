"""# noqa: Y021
This type stub file was generated by pyright.
https://github.com/asweigart/pyautogui/issues/645
"""
from __future__ import absolute_import, division, print_function

import collections
import sys
from collections.abc import Callable, Sequence
from contextlib import contextmanager
from datetime import datetime
from typing import Literal, Union

__version__: str


class PyAutoGUIException(Exception):
    ...


class FailSafeException(PyAutoGUIException):
    ...


class ImageNotFoundException(PyAutoGUIException):
    ...


if sys.version_info[0] == 2 or sys.version_info[0: 2] in ((3, 1), (3, 2)):  # noqa: Y003
    collectionsSequence = collections.Sequence
else:
    collectionsSequence = Sequence


def raisePyAutoGUIImageNotFoundException(wrappedFunction) -> Callable:
    ...


def useImageNotFoundException(value=...) -> None:
    ...


KEY_NAMES = ...
KEYBOARD_KEYS = ...
LEFT = ...
MIDDLE = ...
RIGHT = ...
PRIMARY = ...
SECONDARY = ...
QWERTY = ...
QWERTZ = ...


def isShiftCharacter(character) -> bool:
    ...


MINIMUM_DURATION = ...
MINIMUM_SLEEP = ...
PAUSE = ...
DARWIN_CATCH_UP_TIME = ...
FAILSAFE: bool
FAILSAFE_POINTS = ...
LOG_SCREENSHOTS = ...
LOG_SCREENSHOTS_LIMIT = ...
G_LOG_SCREENSHOTS_FILENAMES = ...
Point = ...
Size = ...


def getPointOnLine(x1: int, y1: int, x2: int, y2: int, n: float) -> tuple[int, int]:
    ...


def linear(n):
    ...


def position(x=..., y=...) -> Point:
    ...


def size() -> Size:
    ...


def onScreen(x, y=...) -> bool:
    ...


def mouseDown(x=..., y=..., button=..., duration=..., tween=..., logScreenshot=..., _pause=...) -> None:
    ...


def mouseUp(x=..., y=..., button=..., duration=..., tween=..., logScreenshot=..., _pause=...) -> None:
    ...


def click(
        x=...,
        y=...,
        clicks=...,
        interval=...,
        button=...,
        duration=...,
        tween=...,
        logScreenshot=...,
        _pause=...) -> None:
    ...


def leftClick(x=..., y=..., interval=..., duration=..., tween=..., logScreenshot=..., _pause=...) -> None:
    ...


def rightClick(x=..., y=..., interval=..., duration=..., tween=..., logScreenshot=..., _pause=...) -> None:
    ...


def middleClick(x=..., y=..., interval=..., duration=..., tween=..., logScreenshot=..., _pause=...) -> None:
    ...


def doubleClick(x=..., y=..., interval=..., button=..., duration=..., tween=..., logScreenshot=..., _pause=...) -> None:
    ...


def tripleClick(x=..., y=..., interval=..., button=..., duration=..., tween=..., logScreenshot=..., _pause=...) -> None:
    ...


def scroll(clicks, x=..., y=..., logScreenshot=..., _pause=...) -> None:
    ...


def hscroll(clicks, x=..., y=..., logScreenshot=..., _pause=...) -> None:
    ...


def vscroll(clicks, x=..., y=..., logScreenshot=..., _pause=...) -> None:
    ...


def moveTo(x=..., y=..., duration=..., tween=..., logScreenshot=..., _pause=...) -> None:
    ...


def moveRel(xOffset=..., yOffset=..., duration=..., tween=..., logScreenshot=..., _pause=...) -> None:
    ...


move = ...


def dragTo(x=..., y=..., duration=..., tween=..., button=..., logScreenshot=..., _pause=..., mouseDownUp=...) -> None:
    ...


def dragRel(
        xOffset=...,
        yOffset=...,
        duration=...,
        tween=...,
        button=...,
        logScreenshot=...,
        _pause=...,
        mouseDownUp=...):
    ...


drag = ...


def isValidKey(key) -> bool:
    ...


def keyDown(key, logScreenshot=..., _pause=...) -> None:
    ...


def keyUp(key, logScreenshot=..., _pause=...) -> None:
    ...


def press(keys, presses=..., interval=..., logScreenshot=..., _pause=...):
    ...


@contextmanager
def hold(keys, logScreenshot=..., _pause=...):
    ...


def typewrite(message, interval=..., logScreenshot=..., _pause=...) -> None:
    ...


write = ...


def hotkey(*args: str, **kwargs: Union[int, bool, None]) -> None:
    ...


def failSafeCheck() -> None:
    ...


def displayMousePosition(xOffset=..., yOffset=...):
    ...


def sleep(seconds) -> None:
    ...


def countdown(seconds) -> None:
    ...


def run(commandStr, _ssCount=...) -> None:
    ...


def printInfo(dontPrint=...) -> str:
    ...


def getInfo() -> tuple[str, str, Literal['0.9.53'], str, Size, datetime]:
    ...
