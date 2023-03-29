import pygame, sys
from pygame.locals import QUIT

from util import Direction, Color
from player import Player
from level import Level

pygame.init()
pygame.display.set_caption('Paint the Wall')
clock = pygame.time.Clock()

player = Player(5, 3, Direction.LEFT, Color.WHITE)

scale = 20
level_data = [
  "00000000000000",
  "0rR1 cC2 gG300",
  "0yY4  0      0",
  "0            0",
  "0pq          0",
  "0bd   0 000  0",
  "0     0 0 0  0",
  "0     0   0  0",
  "00000000000  0",
  "0            0",
  "00000000000000",
]
level = Level(level_data)

screen = pygame.display.set_mode((level.width * scale, level.height * scale))


run = True
while run:
  pygame.event.pump()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False


  # Update
  player.update(pygame, level)

  # Render
  screen.fill((0, 0, 0))
  level.draw(pygame, screen, scale)
  player.draw(pygame, screen, scale)  # player should appear above level

  pygame.display.flip()
  clock.tick(60)
