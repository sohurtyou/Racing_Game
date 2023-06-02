import pygame

class Start_screen:
    def __init__(self, screen):
        self.screen = screen
        self.imagebg = pygame.image.load('Images/Start_Screen/start_background.jpg')
        self.rect = self.imagebg.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.imagestart = pygame.image.load('Images/Start_Screen/start_screen_button.png')

        self.imagebgtext = pygame.image.load('Images/Start_Screen/start_screen_background_1.png')
        self.rect_start_text_bg = self.imagebgtext.get_rect()
        self.rect_start_text_bg.centerx = self.screen_rect.centerx
        self.rect_start_text_bg.centery = 250
        self.rect_start = self.imagestart.get_rect()
        self.rect_start.centerx = self.screen_rect.centerx
        self.rect_start.centery = 400
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.red = (210, 4, 45)
        self.black = (0, 0, 0)
        self.text1 = self.font.render(' Press START', True, self.black)
        self.text2 = self.font.render(' to', True, self.black)
        self.text3 = self.font.render(' Start Game:)', True, self.red)
        self.rect_text1 = self.text1.get_rect()
        self.rect_text2 = self.text2.get_rect()
        self.rect_text3 = self.text3.get_rect()
        self.rect_text1.centerx = self.screen_rect.centerx
        self.rect_text1.centery = 200
        self.rect_text2.centerx = self.screen_rect.centerx
        self.rect_text2.centery = 250
        self.rect_text3.centerx = self.screen_rect.centerx
        self.rect_text3.centery = 294
        self.Game_Start = False

    def output(self):
        self.screen.blit(self.imagebg, self.rect)
        self.screen.blit(self.imagebgtext, self.rect_start_text_bg)
        self.screen.blit(self.text1, self.rect_text1)
        self.screen.blit(self.text2, self.rect_text2)
        self.screen.blit(self.text3, self.rect_text3)
        self.screen.blit(self.imagestart, self.rect_start)
