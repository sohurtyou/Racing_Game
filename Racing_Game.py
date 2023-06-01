import pygame
import sys
from car import Car

def run():
    pygame.init()

    screen = pygame.display.set_mode((585, 600))
    car = Car(screen)
    pygame.display.set_caption("Super Pro Ultra Fast Racing")
    black = (0,0,0)
    while True:
        screen.fill(black)
        car.output()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
run()