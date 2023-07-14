import pygame
from pygame.locals import *
import sys

class Darken:

    WIDTH = 1300
    HEIGHT = 600
    FPS = 60

    # colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self):
       self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
       self.clock = pygame.time.Clock()

    def draw_animation(self):
        running = True
        alpha = 0

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # Animación de oscurecimiento
            if alpha < 255:
                alpha += 5

            self.screen.fill(self.BLACK)
            overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
            overlay.set_alpha(alpha)
            self.screen.blit(overlay, (0, 0))

            pygame.display.flip()
            self.clock.tick(60)

darken = Darken()
