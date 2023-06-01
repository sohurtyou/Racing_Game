import pygame,sys

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
def update(car):
    car.output()