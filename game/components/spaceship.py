from pygame.sprite import Sprite
import pygame

from game.utils.constants import SCREEN_WIDTH, SPACESHIP

class spaceShip(Sprite):

    # constants
    SHIP_WIDTH = 60
    SHIP_HEIGHT = 60
    X_POS = 650
    Y_POS = 500
    SHIP_SPEED = 12

    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect =  self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):

        if (user_input[pygame.K_LEFT] and user_input[pygame.K_UP]):
            self.valid_y_pos_up(self.move_left_and_up)
        elif (user_input[pygame.K_LEFT] and user_input[pygame.K_DOWN]):
            self.valid_y_pos_down(self.move_left_and_down)
        elif (user_input[pygame.K_RIGHT] and user_input[pygame.K_UP]):
            self.valid_y_pos_up(self.move_right_and_up)
        elif (user_input[pygame.K_RIGHT] and user_input[pygame.K_DOWN]):
            self.valid_y_pos_down(self.move_right_and_down)
        elif user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.valid_y_pos_up(self.move_up)
        elif user_input[pygame.K_DOWN]:
            self.valid_y_pos_down(self.move_down)

    def valid_y_pos_up(self, func):
        if self.rect.y > 10:
            func()

    def valid_y_pos_down(self, func):
        if self.rect.y < 540:
            func()

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def move_left(self):
        self.rect.x -= self.SHIP_SPEED

    def move_right(self):
        self.rect.x += self.SHIP_SPEED

    def move_up(self):
        self.rect.y -= self.SHIP_SPEED

    def move_down(self):
        self.rect.y += self.SHIP_SPEED

    def move_left_and_up(self):
        self.rect.x -= self.SHIP_SPEED
        self.rect.y -= self.SHIP_SPEED

    def move_left_and_down(self):
        self.rect.x -= self.SHIP_SPEED
        self.rect.y += self.SHIP_SPEED
    
    def move_right_and_up(self):
        self.rect.x += self.SHIP_SPEED
        self.rect.y -= self.SHIP_SPEED

    def move_right_and_down(self):
        self.rect.x += self.SHIP_SPEED
        self.rect.y += self.SHIP_SPEED