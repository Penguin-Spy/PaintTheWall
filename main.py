import pygame, sys

from util import Direction, Color
from player import Player
from level import Level

def load_level(level_name, player, scale):
  with open(f"assets/levels/{level_name}") as level_data:
    level = Level(level_data)
  spawn_x, spawn_y = level.get_spawn_pos()
  player.respawn(spawn_x, spawn_y, Direction.DOWN, Color.WHITE)

  screen = pygame.display.set_mode((level.width * scale, level.height * scale))
  
  return level, screen

def main():
  pygame.init()
  pygame.display.set_caption('Paint the Wall')
  icon = pygame.image.load("assets/icon.png")
  pygame.display.set_icon(icon)
  
  clock = pygame.time.Clock()
  font = pygame.font.SysFont(None, 24)
  
  scale = 25
  player = Player()
  level, screen = load_level("demo.dat", player, scale)
  
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
    if player.complete:
      img = font.render('Level complete!', True, Color.WHITE.value)
      x = (level.width*scale - img.get_width()) // 2
      y = (level.height*scale - img.get_height()) // 2
      screen.blit(img, (x, y))
    else:
      level.draw(pygame, screen, scale, font)
      player.draw(pygame, screen, scale)  # player should appear above level
  
    pygame.display.flip()
    clock.tick(60)

main()