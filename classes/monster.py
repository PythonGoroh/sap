from classes.character import Character


class Monster(Character):
    def __init__(
        self, name: str, health: int, damage: int, armor: int, default_health: int = 0
    ):
        super().__init__(name, health, damage, armor, default_health)
