from abc import ABC, abstractmethod
from typing import Optional

import preferences


class Item(ABC):
    def __init__(
        self, id: int, name: str, weight: float, value: int, max_stack: int = 1
    ) -> None:
        self.id = id
        self.name = name
        self.weight = weight
        self.value = value
        self.quantity = 1
        self.max_stack = max_stack

    @abstractmethod
    def use(self, user, target=None):
        pass

    def get_info(self):
        if preferences.DEBUG:
            return (
                f"({self.id}){self.name} (вес: {self.weight}, ценность: {self.value})"
            )
