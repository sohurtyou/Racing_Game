import pygame,sys
from trafic import Trafic
import time
def events(car,trafics,screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                car.mright = True
            elif event.key == pygame.K_a:
                car.mleft = True
            elif event.key == pygame.K_w:
                car.mup = True
            elif event.key == pygame.K_s:
                car.mdown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                car.mright = False
                car.image = pygame.image.load('Images/Game_Screen/Car/user_green_car_front.png')
            elif event.key == pygame.K_a:
                car.mleft = False
                car.image = pygame.image.load('Images/Game_Screen/Car/user_green_car_front.png')
            elif event.key == pygame.K_w:
                car.mup = False
            elif event.key == pygame.K_s:
                car.mdown = False
        elif event.type == pygame.USEREVENT:
            new_trafic = Trafic(screen)
            trafics.add(new_trafic)

def update(car,background,trafics,stats):
    background.update()
    background.output()
    car.update()
    car.output()
    update_trafic_cars(trafics,car)
    stats.output()
    stats.update()
    if car.car_explosive == True:
        stats.reset_stats()
        car_dead(trafics, car)
        time.sleep(1.5)
        car.car_explosive = False
    pygame.display.flip()


def update_trafic_cars(trafics,car):
    trafics.update()
    for trafic in trafics.copy():
        if trafic.rect.top > 600 :
            trafics.remove(trafic)
        elif pygame.sprite.collide_rect(car, trafic):
            car.car_explosive = True
    for trafic in trafics.sprites():
        trafic.draw()

def car_dead(trafics,car):
    trafics.empty()
    car.rect.centerx = car.screen_rect.centerx
    car.rect.centery = 500
