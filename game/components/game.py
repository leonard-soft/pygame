import pygame
import os
from time import sleep

from game.components.enemies.enemy_manager import EnemyManager
from game.components.spaceship import spaceShip
from game.components.start_animation import startClass
from game.components.menu import menu
from game.utils.constants import SPACESHIP
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, MENU_MUSIC

class Game():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = spaceShip()
        self.player_option_result = ""
        self.enemy_manager = EnemyManager()

    def run(self):
        # Game loop: events - update - draw
        pygame.mixer.music.load(MENU_MUSIC)
        pygame.mixer.music.play(4)

        startClass.draw_animation()
        sleep(3)

        menu.run(self.player_option_result)
        
       

