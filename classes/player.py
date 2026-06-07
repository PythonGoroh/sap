class Player:
    def __init__(self, name: str = "Player"):
        self.default_armor: int = 10
        self.default_health: int = 10
        self.default_mana: int = 10
        self.default_damage: int = 5
        self.name = name
        
        self.health: int = self.default_health
        self.armor: int = self.default_armor
        self.mana: int = self.default_mana
        self.damage: int = self.default_damage
        
        self.level: int = 1
        self.exp: int = 0
        
    
    def take_damage(self, value: int):
        self.health -= value - self.armor
        self.armor -= value
        
    
    def check_level_up(self):
        if self.exp == self.level * 100:
            self.level += 1
            self.health += 1
            self.default_health += 1


    #ВОССТАНОВЛЕНИЕ СТАТОВ

    def heal(self):
        self.health = self.default_health
    
    def repair_armor(self):
        self.armor = self.default_armor
        
    def re_mana(self):
        self.mana = self.default_mana
        
    #ГЕТТЕРЫ
    
    def get_health(self) -> int:
        return self.health
    
    def get_level(self) -> int:
        return self.level
    
    def get_exp(self) -> int:
        return self.exp
        
    def get_armor(self) -> int:
        return self.armor
    
    def get_mana(self) -> int:
        return self.mana
    
    
    #СЕТТЕРЫ    
        
    def set_health(self, value: int):
        self.health = value
    
    def set_level(self, value: int):
        self.level = value
    
    def set_exp(self, value: int):
        self.exp = value
    
    def set_armor(self, value: int):
        self.armor = value
    