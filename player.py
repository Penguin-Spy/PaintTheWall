from util import Direction

class Player:
  x = None
  y = None
  direction = None
  color = None
  onground = None

  def __init__(self, x, y, direction, color):
    self.x = x
    self.y = y
    self.direction = direction
    self.color = color
    self.onground = True

  def respawn(self):
    self.x = 0
    self.y = 0
    self.direction = Direction.RIGHT

  def update(self, pygame, level):
    if self.onground:   # if we're attached to a wall, allow player input
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
        self.onground = False
        self.direction = Direction.LEFT
        self.move(level, Direction.LEFT)

      elif keys[pygame.K_RIGHT]:
        self.onground = False
        self.direction = Direction.RIGHT
        self.move(level, Direction.RIGHT)

      elif keys[pygame.K_UP]:
        self.onground = False
        self.direction = Direction.UP
        self.move(level, Direction.UP)

      elif keys[pygame.K_DOWN]:
        self.onground = False
        self.direction = Direction.DOWN
        self.move(level, Direction.DOWN)

    else:   # if not, keep careening towards whatever direction we're facting
      self.move(level, self.direction)


  def move(self, level, direction):
    value = direction.value
    x = self.x + value[0]
    y = self.y + value[1]

    next_tile = level.get_tile(x, y)
    print(next_tile, direction, next_tile.solid(direction))
    if next_tile.solid(direction):  # if we hit a wall, we're on the ground now
      self.onground = True
    else:
      self.x = x
      self.y = y

  def draw(self, pygame, screen, scale):
    pygame.draw.rect(
      screen,
      self.color.value,
      (self.x * scale, self.y * scale, scale, scale))
