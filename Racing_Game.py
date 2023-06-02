import pygame
import sys

import controls
from car import Car
from background import Background
from stats import Stats
from pygame.sprite import Group
from start_screen import Start_screen
def run():
    pygame.init()
    screen = pygame.display.set_mode((585, 600))
    pygame.display.set_caption("Super Pro Ultra Fast Racing")
    car = Car(screen)
    background_game_screen = Background(screen)
    trafics = Group()
    stats = Stats(screen)
    start_screen = Start_screen(screen)
    pygame.time.set_timer(pygame.USEREVENT, 3000)
    FPS = 80
    clock = pygame.time.Clock()
    while True:
        controls.events(car,trafics,screen,start_screen,stats)
        start_screen.output()
        pygame.display.flip()

        while start_screen.Game_Start:
            controls.events(car,trafics,screen,start_screen,stats)
            controls.update(car,background_game_screen,trafics,stats,start_screen)
            pygame.display.flip()
            clock.tick(FPS)


run()