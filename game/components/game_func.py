import pygame
import sys

from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy_manager import EnemyManager
from game.components.power_ups.power_up_manager import PowerUpManager
from game.components.spaceship import spaceShip
from game.components.start_animation import startClass
from game.utils.constants import SPACESHIP
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, MENU_MUSIC, FONT_STYLE

class Games:

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
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.score = 0
        self.death_count = 0
        self.font = pygame.font.Font(FONT_STYLE, 15)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
                sys.exit()

    def update(self):
        user_input = pygame.key.get_pressed()
        user_key = pygame.key.get_focused()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update_player_b(self)
        self.bullet_manager.update_enemy_b(self)
        self.update_score()
        self.update_death_count()
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        # 2 enemies
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw_enemy_bullet(self.screen)
        self.bullet_manager.draw_player_bullet(self.screen)
        self.draw_score()
        self.draw_death_count()
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()

        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def update_score(self):
        message_text = f'SCORE : {self.score}'
        text = self.font.render(message_text, True, (255, 255, 255))
        return text
    
    def draw_score(self):
        text = self.update_score()
        self.screen.blit(text, (20,20))

    def update_death_count(self):
        message_text = f'DEATH COUNT : {self.death_count}'
        text = self.font.render(message_text, True, (255, 255, 255))
        return text
    
    def draw_death_count(self):
        text = self.update_death_count()
        self.screen.blit(text, (1130,20))

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round(((self.player.power_time_up - pygame.time.get_ticks() / 1) // 1000), 0)

            if time_to_show >= 0:
                font = pygame.font.Font(FONT_STYLE, 20)
                text = font.render(f'{self.player.power_up_type.capitalize()} is enable for {time_to_show} seconds', True, (255,255,255))
                text_rect = text.get_rect()
                self.screen.blit(text,(500,20))
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
