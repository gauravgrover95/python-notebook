class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1

    def __init__(self, type, health, attack):
        self.type_of_enemy = type
        self.health_points = health
        self.attack_damage = attack

    def talk(self):
        print(f'I am {self.type_of_enemy} enemy. Be prepared for fight!')

    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer to you.')

    def attack(self):
        print(f'{self.type_of_enemy} attacks for {self.attack_damage} damage.')

