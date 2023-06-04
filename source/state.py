from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    ...


class State(ABC):
    context: Context

    @abstractmethod
    def turn_on(self):
        ...


class Redio(Context):
    _state: State | None = None

    def __init__(self, state: State):
        self.change_state(state)

    def change_state(self, state: State):
        print(f"Context switch to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def turn_on(self):
        self._state.turn_on()


class AM(State):
    def turn_on(self):
        print("turn on the redio AM")


class FM(State):
    def turn_on(self):
        print("turn on the redio FM")


context = Redio(state= AM())
context.turn_on()
context.change_state(state= FM())
context.turn_on()

# Context switch to AM
# turn on the redio AM
# Context switch to FM
# turn on the redio FM
