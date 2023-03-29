from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class Player:
    x = None
    y = None
    direction = None

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def respawn(self):
        self.x = 0
        self.y = 0
        self.direction = Direction.RIGHT

    def draw(self, game, window):
        game.draw.rect(window, (0, 255, 0), (self.x, self.y, 10, 10))
