from game.utils.constants import GAME_OVER_TITLE, EXPLOSION_EFFECT, SHOT_EFFECT, SPACE_GUN, SHIELD_TYPE
from game.utils.constants import SCORE_TYPE, CLOCK_TYPE
from game.components.GameOver import menu

import pygame
import os
import sys


class BulletManager:

    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.res = ''

    # update enemy
    def update_enemy_b(self, game_func):
        for bullet in self.enemy_bullets:
            bullet.update_enemy_bullets(self.enemy_bullets)

            if bullet.rect.colliderect(game_func.player.rect) and bullet.owner == 'enemy':

                if game_func.player.power_up_type != SHIELD_TYPE:
                    sound = pygame.mixer.Sound(EXPLOSION_EFFECT)
                    pygame.mixer.Sound.play(sound)
                    game_func.death_count += 1

                    for enemy in game_func.enemy_manager.enemies:
                        game_func.enemy_manager.enemies.remove(enemy)
                
                    menu.run(game_func)
                    
                self.enemy_bullets.remove(bullet)
                 

    # update enemy
    def update_player_b(self, game_func):
        for bullet in self.bullets:
            bullet.update_player_bullets(self.bullets)

            # enemy logic destroy
            for enemy in game_func.enemy_manager.enemies: 
                if bullet.rect.colliderect(enemy) and bullet.owner == 'player':
                    
                    # sound
                    sound = pygame.mixer.Sound(EXPLOSION_EFFECT)
                    pygame.mixer.Sound.play(sound)    
                    self.bullets.remove(bullet)
                    game_func.enemy_manager.enemies.remove(enemy)

                    # score logic
                    if game_func.player.power_up_type == SCORE_TYPE:
                        game_func.score += 500 
                    else:
                        game_func.score += 100     
    
    # draw methods
    def draw_enemy_bullet(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def draw_player_bullet(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    # add bullet method
    def add_bullet(self, bullet, game_func):

        if game_func.player.power_up_type == CLOCK_TYPE:
                pass
        else:
            # enemy
            if bullet.owner == 'enemy' and len (self.enemy_bullets)<1:

                #sound 
                shot_sound = pygame.mixer.Sound(SHOT_EFFECT)
                pygame.mixer.Sound.play(shot_sound)
                self.enemy_bullets.append(bullet)

        # player
        if bullet.owner == 'player':

            # sound
            shot_sound = pygame.mixer.Sound(SPACE_GUN)
            pygame.mixer.Sound.play(shot_sound)
            self.bullets.append(bullet)

    def draw_game_over(self, screen):
        screen.fill((145, 162, 254))
        screen.blit(GAME_OVER_TITLE, (480,200))
        pygame.display.flip()
        
    

    