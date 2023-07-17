from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
import os


class Menu:

    # class atributes
    IMAGES_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
    SCREEN_WIDTH = 1300
    SCREEN_HEIGHT = 600

    def __init__(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.image = pygame.image.load(os.path.join(self.IMAGES_DIR, 'Other/bg_02_h.png'))
        self.title_img = pygame.image.load(os.path.join(self.IMAGES_DIR, 'menu/image.png'))

    def draw_background(self):

        # rect
        logo_rect = self.title_img.get_rect()
        logo_rect.center = (self.SCREEN_WIDTH // 2, 250 // 2)

        running = True
        clock = pygame.time.Clock()
        # count
        ejc = 0

        while running:

            self.screen.blit(self.image, (0,0))        
            self.screen.blit(self.title_img, logo_rect)
        
            pygame.display.flip()
            clock.tick(30)
        
            if ejc > 30:
                running = False
            ejc += 4


main_menu = Menu()
