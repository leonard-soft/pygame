# libraries
from time import sleep
import pygame
from pygame.locals import *
import sys
import os

class Start:

    # class atributes
    IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
    SCREEN_WIDTH = 1300
    SCREEN_HEIGHT = 600

    def __init__(self):
        self.animation_img = pygame.image.load(os.path.join(self.IMAGES_DIR, 'Other/bg_02_h.png'))
        self.animation_logo = pygame.image.load(os.path.join(self.IMAGES_DIR, 'Other/logo.png'))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def draw_animation(self):

        # count
        ejc = 0

        logo_rect = self.animation_logo.get_rect()
        logo_rect.center = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2)

        running = True
        alpha = 0
        logo_alpha = 0
        clock = pygame.time.Clock()

        while running:
            
            # Background fade animation
            if alpha < 255:
                alpha += 5
                self.animation_img.set_alpha(alpha)

            # Logo Appearance Animation
            if alpha >= 255 and logo_alpha < 255:
                logo_alpha += 5
                self.animation_logo.set_alpha(logo_alpha)

            self.screen.blit(self.animation_img, (0, 0))
            self.screen.blit(self.animation_logo, logo_rect)

            pygame.display.flip()
            clock.tick(30)

            if ejc > 50:
                running = False
            ejc += 4

# constant
startClass = Start()