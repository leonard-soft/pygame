from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, OPTIONS_IMAGE, SKY, UP_IMAGE
from game.utils.constants import DOWN_IMAGE, LEFT_IMAGE, RIGHT_IMAGE, BULLET
import pygame , sys

class Controls:
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background = OPTIONS_IMAGE
        self.font = pygame.font.Font(None, 40)
        self.font2 = pygame.font.Font(None, 30)
        self.title = self.font.render('Galactic War', True, (0,0,0))
        self.text1 = self.font2.render('press the up key to advance', True, (0,0,0))
        self.text2 = self.font2.render('press the down key to go back', True, (0,0,0))
        self.text3 = self.font2.render('press left key to move left', True, (0,0,0))
        self.text4 = self.font2.render('press right key to move right', True, (0,0,0))
        self.text5 = self.font2.render('press the P key to shoot', True, (0,0,0))
        self.text_s = self.font2.render('press the SPACE key to return', True, (0,0,0))
        self.up = pygame.transform.scale(UP_IMAGE, (40, 40))
        self.down = pygame.transform.scale(DOWN_IMAGE, (40, 40))
        self.left = pygame.transform.scale(LEFT_IMAGE, (40, 40))
        self.right = pygame.transform.scale(RIGHT_IMAGE, (40, 40))
        self.bullet = pygame.transform.scale(BULLET, (30, 30))

    def run(self ,game):

        running = True
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False
                        game.playing = False

            self.screen.blit(self.background, (0,0))
            self.screen.blit(SKY, (230,40))
            self.screen.blit(self.title, (563, 60))
            self.screen.blit(self.text1, (300, 150))
            self.screen.blit(self.up, (600, 140))
            self.screen.blit(self.text2, (680, 150))
            self.screen.blit(self.down, (1000, 140))
            self.screen.blit(self.text3, (300, 250))
            self.screen.blit(self.left, (600, 240))
            self.screen.blit(self.text4, (680, 250))
            self.screen.blit(self.right, (1000, 240))
            self.screen.blit(self.text5, (550, 350))
            self.screen.blit(self.bullet, (650, 390))
            self.screen.blit(self.text_s, (510, 500))

            pygame.display.flip()



controls = Controls()
