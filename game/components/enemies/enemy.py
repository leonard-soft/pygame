import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_1, ENEMY_2, ENEMY_3, ENEMY_4, SCREEN_HEIGHT, SCREEN_WIDTH

class Enemy(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 60
    X_POS = [250,450,650,850,1050,1250]
    Y_POS = [-10,-15,-20]
    SPEED_Y = [1.5, 2.2, 3.2]
    SPEED_X = [1, 1.2, 1.4]
    MOV_X = {0: 'left', 1: 'right'}
    ENEMIES = [ENEMY_1, ENEMY_2, ENEMY_3, ENEMY_4]

    def __init__(self):
        self.image = random.choice(self.ENEMIES)
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS[random.randint(0,5)]
        self.rect.y = self.Y_POS[random.randint(0,2)]
        self.speed_y = random.choice(self.SPEED_Y)
        self.speed_x = random.choice(self.SPEED_X)
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(30,100)
        self.index = 0

    def update(self, ships):
        self.rect.y += self.speed_y

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
