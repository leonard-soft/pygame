import random
import pygame

from game.components.power_ups.shield import Shield
from game.components.power_ups.score_type import Score
from game.components.power_ups.clock import Clock
from game.utils.constants import SPACESHIP_SHIELD , POWER

class PowerUpManager:
    def __init__(self):
        self.power_ups_types = ['shield', 'score', 'clock']
        self.power_up_name = ''
        self.power_ups = []
        self.duration = random.randint(9, 11)
        self.when_appears = random.randint(5000, 10000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len (self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()
        
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up):

                sound = pygame.mixer.Sound(POWER)
                pygame.mixer.Sound.play(sound)

                if power_up.type == 'shield':
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)

                if power_up.type == 'score':
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    self.power_ups.remove(power_up)

                if power_up.type == 'clock':
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    self.power_ups.remove(power_up)

    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):

        name = random.choice(self.power_ups_types)

        if name == 'shield':
            power_up = Shield()
            self.when_appears += random.randint(5000, 10000)
            self.power_ups.append(power_up)

        if name == 'score':
            power_up = Score()
            self.when_appears += random.randint(5000, 10000)
            self.power_ups.append(power_up)

        if name == 'clock':
            power_up = Clock()
            self.when_appears += random.randint(5000, 10000)
            self.power_ups.append(power_up)
