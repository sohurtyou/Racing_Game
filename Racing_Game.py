import pygame
import sys

def run():
    pygame.init()
    screen = pygame.display.set_mode((585, 600))
    pygame.display.set_caption("Super Pro Ultra Fast Racing")
    black = (0,0,0)
    while True:
        screen.fill(black)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
run()