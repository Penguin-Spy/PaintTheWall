from util import Direction

class Player:
  x = None
  y = None
  direction = None
  color = None
  onground = None
  visible = None  # can't move while invisible
  complete = None

  def __init__(self):
    self.visible = False
    self.complete = False
    # invalid to call update until respawn is called once!

  def respawn(self, x, y, direction, color):
    self.x = x
    self.y = y
    self.direction = direction
    self.color = color
    self.onground = True
    self.visible = True
    self.complete = False

  def update(self, pygame, level):
    if not self.visible or self.complete:
        return

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

    else:   # if not, keep careening towards whatever direction we're facing
      self.move(level, self.direction)


  def move(self, level, direction):
    value = direction.value
    x = self.x + value[0]
    y = self.y + value[1]

    next_tile = level.get_tile(x, y)
    if next_tile.solid(direction):  # if we hit a wall, we're on the ground now
      self.onground = True
    else:
      if next_tile.is_bucket():
        self.color = next_tile.color()
      elif next_tile.is_paintable():
        if next_tile.color() == self.color:
          level.paint_tile(x, y)
      elif next_tile.is_slope():
        self.direction = next_tile.reflect(self.direction)
      elif next_tile.is_exit() and level.complete:
        self.complete = True
      self.x = x
      self.y = y


  def draw(self, pygame, screen, scale):
    if self.visible:
      pygame.draw.rect(
        screen,
        self.color.value,
        (self.x * scale, self.y * scale, scale, scale))
