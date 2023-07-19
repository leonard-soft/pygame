# constants and components
from game.utils.constants import IMG_DIR
from game.components.game_func import Games
from game.utils.constants import SELECT_SOUND, SELECTED_SOUND, PAUSE_EFFECT, SCREEN_WIDTH, SCREEN_HEIGHT

# import libreries
import pygame
import sys
import os


# class games
games_op = Games()

class Menu:
    
    # Inicializar Pygame
    pygame.init()
    pygame.mixer.init()

    # constant
    GAME_TITLE = pygame.image.load(os.path.join(IMG_DIR, 'menu/image.png'))

    def __init__(self, options):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.options = options
        self.selected_option = 0
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.font = pygame.font.Font(None, 40)


    def run(self, result):

        # background image
        image = pygame.image.load(os.path.join(IMG_DIR, 'Other/bg_02_h.png'))

        # while True
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
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
                            running = False

                        else:
                            sound = pygame.mixer.Sound(SELECTED_SOUND)
                            pygame.mixer.Sound.play(sound)
                            print("Seleccionaste:", self.options[self.selected_option])
                            result = self.options[self.selected_option]

                            if result == 'PLAY':
                                self.options = []
                                
                                games_op.playing = True
                                while games_op.playing:

                                    key = pygame.key.get_pressed()
                                    if key[pygame.K_RSHIFT]:
                                        sound = pygame.mixer.Sound(PAUSE_EFFECT)
                                        pygame.mixer.Sound.play(sound)
                                        
                                        self.options = ['CONTINUE']
                                        self.GAME_TITLE = pygame.image.load(os.path.join(IMG_DIR, 'menu/pause.png'))
                                        self.screen.blit(self.GAME_TITLE, (800, 100))
                                        self.run(result)

                                    games_op.events()
                                    games_op.update()
                                    games_op.draw()
                                
            # Clean window
            self.screen.blit(image, (0,0))
            self.screen.blit(self.GAME_TITLE, (410, 100))

            # Draw options
            for i in range(len(self.options)):
                text = self.font.render(self.options[i], True, self.WHITE)
                if i == self.selected_option:
                    pygame.draw.rect(self.screen, self.WHITE, (self.width // 2 - 100, 1000 // 2 - 100 + i * 50, 200, 40), 2)
                self.screen.blit(text, (self.width // 2 - text.get_width() // 2, 1000 // 2 - 100 + i * 50))

            # update window
            pygame.display.flip()


# Uso de la clase Menu
options = ["PLAY","EXIT"]
menu = Menu(options)


