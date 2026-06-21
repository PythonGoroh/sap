from abc import ABC

import preferences

from classes.character import Character


class Item(ABC):
    def __init__(
        self, id: int, name: str, weight: float, value: int, max_stack: int
    ) -> None:
        self.id = id
        self.name = name
        self.weight = weight
        self.value = value
        self.quantity = 1
        self.max_stack = max_stack

    def get_info(self):
        if preferences.DEBUG:
            return (
                f"[{self.id}]{self.name} (вес: {self.weight}, ценность: {self.value})"
            )
        return f"{self.name} (вес: {self.weight}, ценность: {self.value})"


class SwordItem(Item):
    def __init__(
        self,
        id: int,
        name: str,
        weight: float,
        value: int,
        max_stack: int,
        damage: int,
        durability: int,
        current_durability: int,
    ) -> None:
        super().__init__(id, name, weight, value, max_stack)
        self.damage = damage
        self.durability = durability
        self.current_durability = current_durability

    def use(self, target: Character):
        if self.current_durability <= 0:
            return f"{self.name} сломан!"
        target.take_damage(self.damage)
        item_damage = target.armor // 2
        self.durability -= item_damage
        target.set_armor(target.armor - self.damage // 2)
