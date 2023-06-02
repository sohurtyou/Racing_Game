import pygame
import controls
from car import Car
from background import Background
from stats import Stats
from pygame.sprite import Group
from start_screen import Start_screen
from end_screen import End_screen
from sounds import Sounds


def run():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    screen = pygame.display.set_mode((585, 600))
    pygame.display.set_caption("Super Pro Ultra Fast Racing")
    car = Car(screen)
    background_game_screen = Background(screen)
    trafics = Group()
    stats = Stats(screen)
    start_screen = Start_screen(screen)
    end_screen = End_screen(screen)
    sounds = Sounds()
    pygame.time.set_timer(pygame.USEREVENT, 3000)
    FPS = 80
    clock = pygame.time.Clock()
    flStartScreenSound = True
    while True:
        flStartGameSound = True
        controls.events(car, trafics, screen, start_screen, stats, end_screen)
        if flStartScreenSound:
            sounds.back_ground_start_screen.play(-1)
            flStartScreenSound = False
        if not end_screen.game_restart:
            sounds.back_ground_start_screen.play(-1)
            flStartScreenSound = False
            start_screen.output()
            pygame.display.flip()
        else:
            end_screen.output()
            stats.output_restart()
            pygame.display.flip()
        while start_screen.Game_Start:
            controls.events(car, trafics, screen, start_screen, stats, end_screen)
            if flStartGameSound:
                sounds.back_ground_start_screen.stop()
                sounds.start_pressed.play()
                sounds.back_ground_game_screen.play(-1)
                sounds.motor_sound.play(-1)
                flStartGameSound = False
            controls.update(car, background_game_screen, trafics, stats, start_screen, end_screen, sounds)
            pygame.display.flip()
            clock.tick(FPS)
            flStartScreenSound = True


run()
