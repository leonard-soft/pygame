from game.utils.constants import GAME_OVER_TITLE, EXPLOSION_EFFECT, SHOT_EFFECT, SPACE_GUN
import pygame
import sys


class BulletManager:

    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []

    def update_enemy_b(self, game_func):
        for bullet in self.enemy_bullets:
            bullet.update_enemy_bullets(self.enemy_bullets)
            if bullet.rect.colliderect(game_func.player.rect) and bullet.owner == 'enemy':
                # sound
                sound = pygame.mixer.Sound(EXPLOSION_EFFECT)
                pygame.mixer.Sound.play(sound)

                self.enemy_bullets.remove(bullet)
                game_func.playing = False
                self.draw_game_over(game_func.screen)
                pygame.time.delay(2000)
                running = False
                pygame.quit()
                sys.exit()

    def update_player_b(self, game_func):
        for bullet in self.bullets:
            bullet.update_player_bullets(self.bullets)
       
    def draw_enemy_bullet(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def draw_player_bullet(self, screen):
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len (self.enemy_bullets)<1:
            #sound 
            shot_sound = pygame.mixer.Sound(SHOT_EFFECT)
            pygame.mixer.Sound.play(shot_sound)
            self.enemy_bullets.append(bullet)

        if bullet.owner == 'player':
            shot_sound = pygame.mixer.Sound(SPACE_GUN)
            pygame.mixer.Sound.play(shot_sound)
            self.bullets.append(bullet)

    def draw_game_over(self, screen):
        screen.fill((145, 162, 254))
        screen.blit(GAME_OVER_TITLE, (480,200))
        pygame.display.flip()
        