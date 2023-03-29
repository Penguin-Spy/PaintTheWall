class Level():
  width = None
  height = None
  tiles = None

  def __init__(self, tiles):
    self.height = len(tiles)
    self.width = len(tiles[0])  # note: this assumes every row is the same length (which should always be the case)
    self.tiles = tiles

  def draw(self, pygame, screen, scale):
    for x in range(self.width):
      for y in range(self.height):
        if self.tiles[y][x] == 1:
          pygame.draw.rect(
            screen,
            (0, 0, 255),
            (x * scale, y * scale, scale, scale))


  def collides(self, x, y):
    if self.tiles[y][x] == 1:
      return True
    return False

