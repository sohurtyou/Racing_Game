import pygame,sys
from trafic import Trafic
import time
def events(car,trafics,screen,start,stats):
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
        elif start.Game_Start and event.type == pygame.USEREVENT:
            new_trafic = Trafic(screen)
            trafics.add(new_trafic)
        mouse = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if start.rect_start.collidepoint(mouse):
                start.Game_Start = True
                stats.reset_stats()

def update(car,background,trafics,stats,start):
    background.update()
    background.output()
    update_trafic_cars(trafics,car)
    car.output()
    car.update()
    stats.output()
    stats.update()
    pygame.display.flip()
    if car.car_explosive :
        car_dead(trafics, car,start)
        time.sleep(1.5)
        car.car_explosive = False
        car.image = pygame.image.load('Images/Game_Screen/Car/user_green_car_front.png')



def update_trafic_cars(trafics,car):
    trafics.update()
    for trafic in trafics.copy():
        if trafic.rect.top > 600 :
            trafics.remove(trafic)
        elif pygame.sprite.collide_rect(car, trafic):
            car.image = pygame.image.load('Images/Game_Screen/Car/explosive.png')
            if trafic.rect.centerx < 300:
                trafic.image_reverse = pygame.image.load('Images/Game_Screen/Car/explosive.png')
                car.car_explosive = True
                break
            else:
                trafic.image = pygame.image.load('Images/Game_Screen/Car/explosive.png')
                car.car_explosive = True
                break
    for trafic in trafics.sprites():
        trafic.draw()


def car_dead(trafics,car,start):
    start.Game_Start = False
    trafics.empty()
    car.rect.centerx = car.screen_rect.centerx
    car.rect.centery = 500
