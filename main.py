import pygame, sys
from pygame.locals import QUIT

from player import Player, Direction

pygame.init()
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Paint the Wall')

window.fill((255, 0, 0))

player = Player(0, 0, Direction.LEFT)

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((0, 0, 0))
    player.draw(pygame, window)
    pygame.display.flip()
