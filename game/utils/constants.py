import pygame
import os

# Global Constants
TITLE = "Galactic War"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1300
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
SOUNDS_DIR = os.path.join(os.path.dirname(__file__), "..", "sounds")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship2.gif"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/back.jpeg'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship2.gif"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/spaceship.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))

FONT_STYLE = 'freesansbold.ttf'

# game over
GAME_OVER_BACKGROUND = pygame.image.load(os.path.join(IMG_DIR, "Other/Track.jpg"))
GAME_OVER_TITLE = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

# music
MENU_MUSIC = os.path.join(SOUNDS_DIR, "menu.mp3")
SELECT_SOUND = os.path.join(SOUNDS_DIR, "select.mp3")
SELECTED_SOUND = os.path.join(SOUNDS_DIR, "selected.mp3")
PAUSE_EFFECT = os.path.join(SOUNDS_DIR, "pause.mp3")
EXPLOSION_EFFECT = os.path.join(SOUNDS_DIR, "explosion.mp3")
SHOT_EFFECT = os.path.join(SOUNDS_DIR, "shot.mp3")
