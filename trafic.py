import random
import pygame

class Trafic(pygame.sprite.Sprite):

    def __init__(self,screen):
        super(Trafic,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Images/Game_Screen/Trafic/trafic_red_car.png')
        self.image_reverse = pygame.image.load(('Images/Game_Screen/Trafic/trafic_red_car_reverse.png'))
        self.rect = self.image.get_rect()
        random_speed_front = [1.0, 1.2, 1.4, 1.5]
        self.speed_front = random.choice(random_speed_front)
        random_speed_reverse = [4.0, 4.4, 4.8, 5]
        self.speed_reverse = random.choice(random_speed_reverse)
        random_road = [115, 233, 350, 470]
        self.rect.centerx = random.choice(random_road)
        self.rect.bottom = 40
        self.y = float(self.rect.y)

    def draw(self):
        if self.rect.centerx > 300:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.image_reverse, self.rect)

    def update(self):
        if self.rect.centerx > 300:
            self.y += self.speed_front
            self.rect.y = self.y
        else:
            self.y += self.speed_reverse
            self.rect.y = self.y
