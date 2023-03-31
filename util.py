from enum import Enum

class Direction(Enum):
  UP = (0, -1)
  DOWN = (0, 1)
  LEFT = (-1, 0)
  RIGHT = (1, 0)

class Color(Enum):
  RED = (255, 63, 63)
  BLUE = (63, 63, 255)
  GREEN = (63, 255, 63)
  YELLOW = (255, 255, 31)
  WHITE = (255, 255, 255)
  GRAY = (63, 63, 63)
