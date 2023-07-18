import pygame
import os

from game.components.start_animation import startClass
from game.components.menu import menu
from game.utils.constants import MENU_MUSIC

class Game():

    def __init__(self):
        pygame.init()
        self.player_option_result = ''

    def run(self):
        # Game loop: events - update - draw
        pygame.mixer.music.load(MENU_MUSIC)
        pygame.mixer.music.play(4)

        startClass.draw_animation()
        pygame.time.delay(3000)

        menu.run(self.player_option_result)
        
       

