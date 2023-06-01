import pygame

class Car:

    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('Images/Game_Screen/Car/user_green_car_front.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 500
        self.mright = False
        self.mleft = False
        self.mup = False
        self.mdown = False
        self.car_explosive = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.mright and self.rect.right < 530:
            self.rect.centerx += 2
            self.image = pygame.image.load('Images/Game_Screen/Car/user_green_car_right.png')
        if self.mleft and self.rect.left > 55:
            self.rect.centerx -= 2
            self.image = pygame.image.load('Images/Game_Screen/Car/user_green_car_left.png')
        if self.mup and self.rect.top > 55:
            self.rect.centery -= 2
        if self.mdown and self.rect.bottom < 570:
            self.rect.centery += 2