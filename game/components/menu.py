from game.utils.constants import IMG_DIR
from game.components.game_func import Games
import pygame
import sys
import os


# class games
games_op = Games()

class Menu:
    def __init__(self, width, height, options):
        self.width = width
        self.height = height
        self.options = options
        self.selected_option = 0

        # Inicializar Pygame
        pygame.init()

        # Configuración de la ventana
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Colores
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Fuente
        self.font = pygame.font.Font(None, 40)

    def run(self, result):
        image = pygame.image.load(os.path.join(IMG_DIR, 'Other/bg_02_h.png'))

        # Bucle principal del programa
        running = True
        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.selected_option == len(self.options) - 1:
                            running = False
                        else:
                            print("Seleccionaste:", self.options[self.selected_option])
                            result = self.options[self.selected_option]
                            if result == 'PLAY':
                                self.options = []
                                width = 1300
                                height = 600
                                screen = pygame.display.set_mode((width, height))
                                while True:
                                    try:
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_RETURN:  
                                                pass
                                    except:
                                       pass

                                    games_op.events()
                                    games_op.update()
                                    games_op.draw()
                                pygame.display.quit()
                                pygame.quit()


            # Limpiar la pantalla
            self.screen.blit(image, (0,0))

            # Dibujar las opciones
            for i in range(len(self.options)):
                text = self.font.render(self.options[i], True, self.WHITE)
                if i == self.selected_option:
                    pygame.draw.rect(self.screen, self.WHITE, (self.width // 2 - 100, 800 // 2 - 100 + i * 50, 200, 40), 2)
                self.screen.blit(text, (self.width // 2 - text.get_width() // 2, 800 // 2 - 100 + i * 50))

            # Actualizar la pantalla
            pygame.display.flip()

        # Salir del programa
        pygame.quit()
        sys.exit()

# Uso de la clase Menu
options = ["PLAY","EXIT"]
menu = Menu(1300, 600, options)


