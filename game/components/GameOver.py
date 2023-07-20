from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, IMG_DIR, SELECT_SOUND, SELECTED_SOUND

import pygame
import os, sys

class Menu:

    # pygame init
    pygame.init()

     # constant
    GAME_TITLE = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

    def __init__(self,options):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.options = options
        self.selected_option = 0
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.font = pygame.font.Font(None, 40)


    def run(self, game):
        res = ''
        # while True
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                        sound = pygame.mixer.Sound(SELECT_SOUND)
                        pygame.mixer.Sound.play(sound)

                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                        sound = pygame.mixer.Sound(SELECT_SOUND)
                        pygame.mixer.Sound.play(sound)

                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == len(self.options) - 1:
                            sound = pygame.mixer.Sound(SELECTED_SOUND)
                            pygame.mixer.Sound.play(sound)
                            res = self.options[self.selected_option]
                            running = False

                        else:
                            sound = pygame.mixer.Sound(SELECTED_SOUND)
                            pygame.mixer.Sound.play(sound)
                            res = self.options[self.selected_option]
                            running = False

            # Clean Window
            self.screen.fill((145, 162, 254))
            self.screen.blit(self.GAME_TITLE, (470, 100))

            # Draw options
            for i in range(len(self.options)):
                text = self.font.render(self.options[i], True, self.WHITE)
                if i == self.selected_option:
                    pygame.draw.rect(self.screen, self.WHITE, (self.width // 2 - 100, 900 // 2 - 100 + i * 50, 200, 40), 2)
                self.screen.blit(text, (self.width // 2 - text.get_width() // 2, 900 // 2 - 100 + i * 50))

            # Update window
            pygame.display.flip()

        if res == 'MAIN MENU':
            game.score = 0
            game.death_count = 0
            game.playing = False
            

# Uso de la clase Menu
options = ["PLAY AGAIN", "MAIN MENU"]
menu = Menu(options)

