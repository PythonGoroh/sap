from typing import Optional

from classes.item import Item


class InventorySlot:
    def __init__(self, item: Optional[Item] = None, quantity: int = 0) -> None:
        self.item = item
        self.quantity = quantity

    def is_empty(self):
        if self.item is None or self.quantity <= 0:
            return True
        return False

    def add(self, item: Item, quantity: int = 1):
        if self.is_empty():
            self.item = item
            self.quantity = min(quantity, item.max_stack)
            return quantity - self.quantity
        elif (
            self.item is not None
            and self.item.id == item.id
            and self.quantity < item.max_stack
        ):
            space_left = item.max_stack - self.quantity
            can_add = min(space_left, quantity)
            self.quantity += can_add
            return quantity - can_add
        return quantity

    def remove():
        pass

    def __str__(self) -> str:
        pass
