import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, SCREEN_HEIGHT

class Bullet(Sprite):
    BULLET_SIZE = pygame.transform.scale(BULLET, (10, 20))
    BULLET_ENEMY_SIZE = pygame.transform.scale(BULLET_ENEMY, (10, 20))
    BULLETS = {'player':BULLET_SIZE, 'enemy': BULLET_ENEMY_SIZE}
    SPEED = 10
    
    def __init__(self, spaceshift):
        self.image = self.BULLETS[spaceshift.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceshift.rect.center
        self.owner = spaceshift.type

    def update_enemy_bullets(self, bullets):
        self.rect.y += self.SPEED
        if self.rect.y >= SCREEN_HEIGHT:
            bullets.remove(self)

    def update_player_bullets(self, bullets):
        self.rect.y -= self.SPEED
        

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))