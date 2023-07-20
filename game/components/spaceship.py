from pygame.sprite import Sprite
import pygame

from game.components.bullets.bullet import Bullet
from game.utils.constants import SCREEN_WIDTH, SPACESHIP, DEFAULT_TYPE

class spaceShip(Sprite):

    # constants
    SHIP_WIDTH = 60
    SHIP_HEIGHT = 60
    X_POS = 650
    Y_POS = 500
    SHIP_SPEED = 8

    
    def __init__(self):
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH, self.SHIP_HEIGHT))
        self.rect =  self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'
        self.has_power_up = False
        self.power_up_type = DEFAULT_TYPE
        self.power_time_up = 0

    def update(self, user_input, game):

        # left and up
        if (user_input[pygame.K_LEFT] and user_input[pygame.K_UP]):
            self.valid_y_pos_up(self.move_left_and_up)

        # left and down
        if (user_input[pygame.K_LEFT] and user_input[pygame.K_DOWN]):
            self.valid_y_pos_down(self.move_left_and_down)

        # right and up
        if (user_input[pygame.K_RIGHT] and user_input[pygame.K_UP]):
            self.valid_y_pos_up(self.move_right_and_up)

        # right and down
        if (user_input[pygame.K_RIGHT] and user_input[pygame.K_DOWN]):
            self.valid_y_pos_down(self.move_right_and_down)

        # left
        if user_input[pygame.K_LEFT]:
            self.valid_x_pos(self.move_left)

        # right
        if user_input[pygame.K_RIGHT]:
            self.valid_x_pos_right(self.move_right)

        # up
        if user_input[pygame.K_UP]:
            self.valid_y_pos_up(self.move_up)

        # down
        if user_input[pygame.K_DOWN]:
            self.valid_y_pos_down(self.move_down)

        # shot
        if user_input[pygame.K_p]:
            self.shoot(game.bullet_manager)

    # methods that validate the position of the ship
    def valid_y_pos_up(self, func):
        if self.rect.y > 10:
            func()

    def valid_y_pos_down(self, func):
        if self.rect.y < 540:
            func()

    def valid_x_pos(self, func):
        if self.rect.x < -40:
            self.rect.x = 1340
        func()

    def valid_x_pos_right(self, func):
        if self.rect.x > 1340:
            self.rect.x = -40
        func()

    # draw method
    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    # move methods
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

    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)

    def set_image(self, size = (SHIP_WIDTH, SHIP_HEIGHT), image = SPACESHIP):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)