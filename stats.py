import pygame


class Stats:
    def __init__(self, screen):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.screen = screen
        self.i = 0.0
        self.black = (0, 0, 0)
        self.text = self.font.render(f'Score{self.i}', True, self.black)
        self.rect = self.text.get_rect()
        self.imagestart = pygame.image.load('Images/Game_Screen/Stats/stats_background.png')
        self.rect_bg = self.imagestart.get_rect()
        self.rect_bg.centerx = 115
        self.rect_bg.centery = 50

    def output(self):
        self.screen.blit(self.imagestart, self.rect_bg)
        self.screen.blit(self.text, self.rect)
        self.rect_bg.centerx = 115
        self.rect_bg.centery = 50
        self.rect.centerx = 100
        self.rect.centery = 50

    def output_restart(self):
        self.screen.blit(self.imagestart, self.rect_bg)
        self.rect_bg.centerx = 290
        self.rect_bg.centery = 150
        self.screen.blit(self.text, self.rect)
        self.rect.centerx = 270
        self.rect.centery = 150

    def reset_stats(self):
        self.i = 0.0

    def update(self):
        self.i += 0.2
        self.text = self.font.render(f'Score : {int(self.i)}', True, self.black)
