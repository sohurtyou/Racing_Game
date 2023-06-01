import pygame
import sys

import controls
from car import Car
from background import Background
def run():
    pygame.init()

    screen = pygame.display.set_mode((585, 600))
    car = Car(screen)
    background_game_screen = Background(screen)
    pygame.display.set_caption("Super Pro Ultra Fast Racing")

    while True:
        controls.events(car)
        controls.update(car, background_game_screen)
run()