from __future__ import annotations

from typing import Any, Callable


class Delegator:
    def __init__(self, delegate: Delegate) -> None:
        self.delegate = delegate

    def __getattr__(self, name: str) -> Any | Callable:
        attr = getattr(self.delegate, name)

        if not callable(attr):
            return attr

        def wrapper(*args, **kwargs):
            return attr(*args, **kwargs)

        return wrapper


class Delegate:
    def __init__(self) -> None:
        self.name = 'bosung_park'

    def say_name(self) -> str:
        return f'my name is {self.name}'

delegator = Delegator(delegate=Delegate())

assert delegator.name == 'bosung_park'
assert delegator.say_name() == 'my name is bosung_park'
