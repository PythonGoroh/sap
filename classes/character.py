class Character:
    def __init__(
        self, name: str, health: int, damage: int, armor: int, default_health: int = 0
    ):
        self.health = health

        if default_health == 0:
            self.default_health = default_health
        else:
            self.default_health = health
        self.damage = damage
        self.armor = armor
        self.name = name

    def take_damage(self, value: int):
        self.health -= value - self.armor

    def heal(self):
        self.health = self.default_health

    # СЕТТЕРЫ
    def set_health(self, value: int):
        self.health = value

    def set_damage(self, value: int):
        self.damage = value

    def set_armor(self, value: int):
        self.armor = value

    def set_name(self, value: str):
        self.name = value

    # ГЕТТЕРЫ
    def get_health(self) -> int:
        return self.health

    def get_damage(self) -> int:
        return self.damage

    def get_armor(self) -> int:
        return self.armor

    def get_name(self) -> str:
        return self.name
