import pygame

class Car:

    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('Images/Game_Screen/Car/user_green_car_front.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 500

    def output(self):
        self.screen.blit(self.image, self.rect)