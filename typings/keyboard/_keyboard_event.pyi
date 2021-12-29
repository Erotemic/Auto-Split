"""
This type stub file was generated by pyright.
"""

from typing import Literal, Optional, Union


KEY_DOWN = Literal['down']
KEY_UP = Literal['up']


class KeyboardEvent:
    event_type: Optional[Union[KEY_DOWN, KEY_UP]] = ...
    scan_code: Optional[int] = ...
    name: Optional[str] = ...
    time: Optional[Unknown] = ...
    device: Optional[Unknown] = ...
    modifiers: Optional[Unknown] = ...
    is_keypad: Optional[bool] = ...

    def __init__(self,
                 event_type: event_type,
                 scan_code,
                 name: name = ...,
                 time: time = ...,
                 device: device = ...,
                 modifiers: modifiers = ...,
                 is_keypad: is_keypad = ...
                 ) -> None:
        ...

    def to_json(self, ensure_ascii: bool = ...) -> str:
        ...

    def __repr__(self) -> str:
        ...

    def __eq__(self, other: KeyboardEvent) -> bool:
        ...
