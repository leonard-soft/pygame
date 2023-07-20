from game.components.power_ups.power_up import PowerUp
from game.utils.constants import CLOCK, CLOCK_TYPE


class Clock(PowerUp):
    def __init__(self):
        super().__init__(CLOCK, CLOCK_TYPE)