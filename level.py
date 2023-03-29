from enum import Enum
from math import pi
from util import Color, Direction


class Tile(Enum):
  AIR = " "
  WALL = "0"
  EXIT = "E"       #  _________
  SLOPE_DR = "p"   # |p       q|    corners facing in
  SLOPE_DL = "q"   # |         |
  SLOPE_UR = "b"   # |         |
  SLOPE_UL = "d"   # |b_______d|
  PAINTABLE_RED = "r"
  PAINTABLE_BLUE = "c"  # cerulean (that means blue by the way)
  PAINTABLE_GREEN = "g"
  PAINTABLE_YELLOW = "y"
  PAINTED_RED = "R"
  PAINTED_BLUE = "C"
  PAINTED_GREEN = "G"
  PAINTED_YELLOW = "Y"
  BUCKET_RED = "1"
  BUCKET_BLUE = "2"
  BUCKET_GREEN = "3"
  BUCKET_YELLOW = "4"

  # hmm
  def is_paintable(self):
    return self == Tile.PAINTABLE_RED or self == Tile.PAINTABLE_BLUE or self == Tile.PAINTABLE_GREEN or self == Tile.PAINTABLE_YELLOW

  def is_painted(self):
    return self == Tile.PAINTED_RED or self == Tile.PAINTED_BLUE or self == Tile.PAINTED_GREEN or self == Tile.PAINTED_YELLOW

  def is_bucket(self):
    return self == Tile.BUCKET_RED or self == Tile.BUCKET_BLUE or self == Tile.BUCKET_GREEN or self == Tile.BUCKET_YELLOW

  def is_slope(self):
    return self == Tile.SLOPE_DR or self == Tile.SLOPE_DL or self == Tile.SLOPE_UR or self == Tile.SLOPE_UL


  def color(self):
    if self == Tile.PAINTABLE_RED or self == Tile.PAINTED_RED or self == Tile.BUCKET_RED:
      return Color.RED
    elif self == Tile.PAINTABLE_BLUE or self == Tile.PAINTED_BLUE or self == Tile.BUCKET_BLUE:
      return Color.BLUE
    elif self == Tile.PAINTABLE_GREEN or self == Tile.PAINTED_GREEN or self == Tile.BUCKET_GREEN:
      return Color.GREEN
    elif self == Tile.PAINTABLE_YELLOW or self == Tile.PAINTED_YELLOW or self == Tile.BUCKET_YELLOW:
      return Color.YELLOW

    return Color.WHITE


  def paint(self):
    if self == Tile.PAINTABLE_RED:
      return Tile.PAINTED_RED
    elif self == Tile.PAINTABLE_BLUE:
      return Tile.PAINTED_BLUE
    elif self == Tile.PAINTABLE_GREEN:
      return Tile.PAINTED_GREEN
    elif self == Tile.PAINTABLE_YELLOW:
      return Tile.PAINTED_YELLOW

    return self


  def solid(self, direction):   # direction is the side of the tile, the names of the slope are where the angle faces outwards
    if self == Tile.WALL:       # hence the direction comparisons matching the name of the slope
      return True
    elif self == Tile.SLOPE_DR and (direction == Direction.DOWN or direction == Direction.RIGHT):
      return True
    elif self == Tile.SLOPE_DL and (direction == Direction.DOWN or direction == Direction.LEFT):
      return True
    elif self == Tile.SLOPE_UR and (direction == Direction.UP or direction == Direction.RIGHT):
      return True
    elif self == Tile.SLOPE_UL and (direction == Direction.UP or direction == Direction.LEFT):
      return True
    return False


  # bounce a direction off of this slope
  def reflect(self, direction):
    if direction == Direction.UP:
      if self == Tile.SLOPE_DR:
        return Direction.RIGHT
      elif self == Tile.SLOPE_DL:
        return Direction.LEFT

    if direction == Direction.DOWN:
      if self == Tile.SLOPE_UR:
        return Direction.RIGHT
      elif self == Tile.SLOPE_UL:
        return Direction.LEFT

    if direction == Direction.LEFT:
      if self == Tile.SLOPE_DR:
        return Direction.DOWN
      elif self == Tile.SLOPE_UR:
        return Direction.UP

    if direction == Direction.RIGHT:
      if self == Tile.SLOPE_DL:
        return Direction.DOWN
      elif self == Tile.SLOPE_UL:
        return Direction.UP

    return direction



class Level():
  width = None
  height = None
  tiles = None

  def __init__(self, level_data):

    # data = level_data.readlines()

    tiles = []
    rows = 0
    columns = 0

    for line in level_data:
      rows += 1
      tiles.append([])  # make new array for this row (zero indexed)

      column_counter = 0
      for char in line:
        column_counter += 1
        tiles[rows-1].append(Tile(char))

      # check to make sure level is a rectangle
      if rows == 1:
        columns = column_counter
      elif column_counter != columns:
        raise Exception(f"Non-rectangular level region! Expected {columns} columns for row {rows}, but got {column_counter}!")

    self.height = rows
    self.width = columns
    self.tiles = tiles


  def draw(self, pygame, screen, scale):
    for x in range(self.width):
      for y in range(self.height):
        tile = self.tiles[y][x]
        color = (255, 255, 255)   # shouldn't appear
        if tile == Tile.AIR:
          continue
        elif tile == Tile.WALL:
          color = (31, 31, 31)
        else:
          color = tile.color().value

        tl = (x*scale, y*scale)
        tr = ((x+1)*scale-1, y*scale)
        bl = (x*scale, (y+1)*scale-1)
        br = ((x+1)*scale-1, (y+1)*scale-1)

        if(tile.is_paintable()):
          pygame.draw.line(screen, color, tl, br)
          pygame.draw.line(screen, color, tr, bl)

        elif(tile.is_painted()):
          pygame.draw.circle(screen, color, ((x+.5) * scale, (y+.5) * scale), scale/2)

        elif(tile.is_bucket()):
          pygame.draw.arc(screen, color, (x*scale, y*scale, scale, scale), pi, 0, width = 2)

        elif(tile.is_slope()):
          polygon = None
          if(tile == Tile.SLOPE_DR):
            polygon = [tl, tr, bl]
          elif(tile == Tile.SLOPE_DL):
            polygon = [tl, tr, br]
          elif(tile == Tile.SLOPE_UR):
            polygon = [tl, br, bl]
          elif(tile == Tile.SLOPE_UL):
            polygon = [tr, br, bl]

          pygame.draw.polygon(screen, color, polygon)
        else:
          pygame.draw.rect(
            screen, color,
            (x * scale, y * scale, scale, scale)
          )


  def get_tile(self, x, y):
    return self.tiles[y][x]

  def paint_tile(self, x, y):
    self.tiles[y][x] = self.tiles[y][x].paint()

  def collides(self, x, y):
    if self.tiles[y][x] == Tile.WALL:
      return True
    return False

