from enemy import *

enemy = Enemy()
enemy.type_of_enemy = 'Zombie'
enemy.talk()
print('enemy health points', enemy.health_points)
print()

print(f'{enemy.type_of_enemy} enemy has {enemy.health_points} health points and '
      f'can do an {enemy.attack_damage} damage')
print()

enemy.walk_forward()
enemy.attack()
print()

enemy2 = Enemy()
enemy2.health_points = 100
print('enemy 2 health points', enemy2.health_points)