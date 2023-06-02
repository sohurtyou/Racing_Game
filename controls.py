import pygame,sys
from trafic import Trafic
import time
def events(car,trafics,screen,start,stats,end):
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
            elif end.rect_end.collidepoint(mouse):

                stats.reset_stats()
                start.Game_Start = True

def update(car,background,trafics,stats,start,end,sound):
    background.update()
    background.output()
    update_trafic_cars(trafics,car,sound)
    car.output()
    car.update()
    stats.output()
    stats.update()
    pygame.display.flip()
    if car.car_explosive :
        sound.car_crash.play()
        car_dead(trafics, car,start,end)
        time.sleep(1.5)
        car.car_explosive = False
        car.image = pygame.image.load('Images/Game_Screen/Car/user_green_car_front.png')



def update_trafic_cars(trafics,car,sound):
    trafics.update()
    for trafic in trafics.copy():
        if trafic.rect.top > 600 :
            trafics.remove(trafic)
        elif pygame.sprite.collide_rect(car, trafic):
            car.image = pygame.image.load('Images/Game_Screen/Car/explosive.png')
            sound.back_ground_game_screen.stop()
            sound.motor_sound.stop()
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


def car_dead(trafics,car,start,end):
    start.Game_Start = False
    trafics.empty()
    end.game_restart = True
    car.rect.centerx = car.screen_rect.centerx
    car.rect.centery = 500
