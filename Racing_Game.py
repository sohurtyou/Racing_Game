import pygame
import sys

import controls
from car import Car

def run():
    pygame.init()

    screen = pygame.display.set_mode((585, 600))
    car = Car(screen)
    pygame.display.set_caption("Super Pro Ultra Fast Racing")
    black = (0,0,0)
    while True:
        screen.fill(black)
        controls.update(car)
        pygame.display.flip()
        controls.events()
        pygame.display.flip()
run()