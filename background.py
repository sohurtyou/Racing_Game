import pygame

class Background:

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Images/Game_Screen/Background/background_road.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = 600
        self.speed = 4
        self.y = float(self.rect.y)
    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.rect.bottom < 715:
             self.y += self.speed
             self.rect.y = self.y

        else:
           self.rect.bottom = self.screen_rect.bottom
           self.y = self.rect.y

