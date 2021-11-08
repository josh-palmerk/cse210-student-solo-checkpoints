from random import randint
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here...
class Food(Actor):
    def __init__(self):
        super().__init__()
        self._points = randint(1, 10)
        self.set_width = constants.DEFAULT_SQUARE_LENGTH
        self.set_height = constants.DEFAULT_SQUARE_LENGTH
        self.set_position(Point(randint(0, constants.MAX_X), randint(0, constants.MAX_Y)))
        self.set_text(f"{self._points}")
        # self.set_velocity(0, 0)

    def get_points(self):
        return self._points

    def reset(self):
        self._points = randint(1, 10)
        self.set_position(Point(randint(0, constants.MAX_X), randint(0, constants.MAX_Y)))
        self.set_text(f"{self._points}")
