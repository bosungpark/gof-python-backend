from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from functools import wraps


class LoggingStrategy(ABC):
    @abstractmethod
    def select_logger(self):
        pass

class BasicLoggingStrategy(LoggingStrategy):
    
    def basic_logger(self, logging_type:str):
        def inner_basic_logger(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                print("basic_logger", logging_type)
                result = func(*args, **kwargs)
                return result
            return wrapper
        return inner_basic_logger

    def select_logger(self):
        return self.basic_logger


# class BasicAsyncLoggingStrategy(LoggingStrategy):
#     def basic_async_logger(self ,func: Callable):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print("basic_async_logger")
#         return wrapper

#     def select_logger(self):
#         return self.basic_async_logger


# class DetailedLoggingStrategy(LoggingStrategy):
#     def detailed_logger(self, func: Callable):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print("detailed_logger")
#             result = func(*args, **kwargs)
#             return result
#         return wrapper

#     def select_logger(self):
#         return self.detailed_logger


# class DetailedAsyncLoggingStrategy(LoggingStrategy):
#     def detailed_async_logger(self, func: Callable):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print("detailed_async_logger")
#         return wrapper

#     def select_logger(self):
#         return self.detailed_async_logger


class LoggingFactory():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def generate_logger(self) -> None:
        logger = self._strategy.select_logger()
        return logger


if __name__ == "__main__":
    context = LoggingFactory(BasicLoggingStrategy())
    basic = context.generate_logger()

    # context.strategy = DetailedLoggingStrategy()
    # detail = context.generate_logger()

    @basic("here")
    def foo_api():
        print("api call")
        return

    foo_api()
    
