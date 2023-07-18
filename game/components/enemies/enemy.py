import random
import pygame
from pygame.sprite import Sprite

from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, ENEMY_4, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = [250,450,850,1250]
    Y_POS = [-10,-15,-20]
    SPEED_Y = [2, 3, 4]
    SPEED_X = [1, 1.2, 1.4]
    MOV_X = {0: 'left', 1: 'right'}
    ENEMIES = {1: ENEMY_1, 2: ENEMY_2, 3: ENEMY_3, 4: ENEMY_4}

    def __init__(self, image = 1, move_x_for = [30, 100]):
        self.image = self.ENEMIES[image]
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS[random.randint(0,3)]
        self.rect.y = self.Y_POS[random.randint(0,2)]
        self.speed_y = self.SPEED_Y[random.randint(0,2)]
        self.speed_x = self.SPEED_X[random.randint(0,2)]
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(move_x_for[0], move_x_for[1])
        self.type = 'enemy'
        self.index = 0
        self.shooting_time = random.randint(30, 50)


    def update(self, ships, game):
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        
        self.change_movement_x()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)


    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index +=1
        if ((self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.SHIP_WIDTH)):
            self.movement_x = 'left'
            self.index=0
        elif ((self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10)):
            self.movement_x = 'right'
            self.index=0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30, 50)