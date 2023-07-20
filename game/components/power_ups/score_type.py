from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SCORE, SCORE_TYPE


class Score(PowerUp):
    def __init__(self):
        super().__init__(SCORE, SCORE_TYPE)