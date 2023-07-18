from game.components.enemies.enemy import Enemy
import random

class EnemyManager:

    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    """
    def add_enemy(self):
        if len (self.enemies)<2:
            enemy = Enemy()
            enemy2 = Enemy()
            self.enemies.append(enemy)
            self.enemies.append(enemy2) """
        
    def add_enemy(self):
        enemy_type = random.randint(1,2)
        if enemy_type == 1:
            enemy = Enemy()
        else:
            move_x_for = [50, 120]
            enemy = Enemy(enemy_type, move_x_for)
        if len (self.enemies)<1:
            self.enemies.append(enemy)
    