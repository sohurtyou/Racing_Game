import pygame

class Sounds:
    def __init__(self):
        self.back_ground_start_screen = pygame.mixer.Sound('Sounds/Start_screen_music.mp3')
        self.back_ground_game_screen = pygame.mixer.Sound('Sounds/Game_screen_music.mp3')
        self.motor_sound = pygame.mixer.Sound('Sounds/Motor_sound.mp3')
        self.car_crash = pygame.mixer.Sound('Sounds/car_crash.mp3')
        self.start_pressed = pygame.mixer.Sound('Sounds/Start_pressed.mp3')
