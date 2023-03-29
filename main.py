import pygame, sys
from pygame.locals import QUIT

from player import Player, Direction
from level import Level

pygame.init()
pygame.display.set_caption('Paint the Wall')
clock = pygame.time.Clock()

player = Player(5, 3, Direction.LEFT)

scale = 20
leveltiles = [
  [1,1,1,1,1,1,1,1,1,1],
  [1,0,0,1,0,0,0,0,0,1],
  [1,0,0,1,0,0,0,0,0,1],
  [1,0,0,0,0,0,0,1,0,1],
  [1,0,0,0,0,0,0,0,0,1],
  [1,0,0,0,1,1,0,0,0,1],
  [1,1,1,1,1,1,0,0,0,1],
  [1,0,1,0,0,0,0,0,0,1],
  [1,0,0,0,1,0,0,1,0,1],
  [1,1,1,1,1,1,1,1,1,1]
]
level = Level(leveltiles)

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
  player.draw(pygame, screen, scale)
  level.draw(pygame, screen, scale)

  pygame.display.flip()
  clock.tick(60)
