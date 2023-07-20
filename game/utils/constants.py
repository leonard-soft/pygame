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
SCORE_IMG = pygame.image.load(os.path.join(IMG_DIR, 'Other/plus.png'))
CLOCK_IMG = pygame.image.load(os.path.join(IMG_DIR, 'Other/clock.png'))

# power up img
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
SCORE = pygame.transform.scale(SCORE_IMG, (50,50))
CLOCK = pygame.transform.scale(CLOCK_IMG, (50,50))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/back.jpeg'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

# power ups
DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
SCORE_TYPE = 'score'
CLOCK_TYPE = 'clock'

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

# options menu
OPTIONS_IMAGE = pygame.image.load(os.path.join(IMG_DIR, "Other/bg_02_h.png"))
SKY = pygame.image.load(os.path.join(IMG_DIR, "Other/sky2.jpg"))
UP_IMAGE = pygame.image.load(os.path.join(IMG_DIR, "controls/flechita.png"))
DOWN_IMAGE = pygame.image.load(os.path.join(IMG_DIR, "controls/flechita2.png"))
LEFT_IMAGE = pygame.image.load(os.path.join(IMG_DIR, "controls/flechita3.png"))
RIGHT_IMAGE = pygame.image.load(os.path.join(IMG_DIR, "controls/flechita4.png"))

# music
MENU_MUSIC = os.path.join(SOUNDS_DIR, "menu.mp3")
SELECT_SOUND = os.path.join(SOUNDS_DIR, "select.mp3")
SELECTED_SOUND = os.path.join(SOUNDS_DIR, "selected.mp3")
PAUSE_EFFECT = os.path.join(SOUNDS_DIR, "pause.mp3")
EXPLOSION_EFFECT = os.path.join(SOUNDS_DIR, "explosion.mp3")
SHOT_EFFECT = os.path.join(SOUNDS_DIR, "shot.mp3")
SPACE_GUN = os.path.join(SOUNDS_DIR, "space_gun.mp3")
POWER = os.path.join(SOUNDS_DIR, "power.mp3")
