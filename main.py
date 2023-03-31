import pygame, sys
from pygame.locals import QUIT

from util import Direction, Color
from player import Player
from level import Level

pygame.init()
pygame.display.set_caption('Paint the Wall')
clock = pygame.time.Clock()

player = Player(5, 3, Direction.DOWN, Color.WHITE)

scale = 25
level_data = [
  "00000000000000000000",
  "0   1 0        00000",
  "000            00000",
  "0    0 00r       2 0",
  "0      00          0",
  "0rr   c0           0",
  "00000000           0",
  "0gg       0000000000",
  "0gg      0p       30",
  "0       00 000000000",
  "04      00b   yy  q0",
  "0             00   0",
  "000           yy  d0",
  "00000000000000000000",
]
level = Level(level_data)

screen = pygame.display.set_mode((level.width * scale, level.height * scale))
font = pygame.font.SysFont(None, 24)


run = True
while run:
  pygame.event.pump()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False


  # Update
  player.update(pygame, level)
  level.update()

  # Render
  screen.fill((0, 0, 0))
  level.draw(pygame, screen, scale, font)
  player.draw(pygame, screen, scale)  # player should appear above level

  pygame.display.flip()
  clock.tick(60)

