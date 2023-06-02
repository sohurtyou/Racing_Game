import pygame

class End_screen:
    def __init__(self, screen):
        self.screen = screen
        self.imagebg = pygame.image.load('Images/End_Screen/end_screen_background.jpg')
        self.bg_rect = self.imagebg.get_rect()
        self.screen_rect = screen.get_rect()
        self.bg_rect.centerx = self.screen_rect.centerx
        self.bg_rect.bottom = self.screen_rect.bottom
        self.imagend = pygame.image.load('Images/End_Screen/end_screen_restart_button.png')
        self.rect_end = self.imagend.get_rect()
        self.rect_end.centerx = self.screen_rect.centerx
        self.rect_end.centery = 500
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.black = (0, 0, 0)
        self.text1 = self.font.render(' Press RESTART to Restart Game:)', True, self.black)
        self.rect_text1 = self.text1.get_rect()
        self.rect_text1.centerx = self.screen_rect.centerx
        self.rect_text1.centery = 80
        self.image_reset_back_ground = pygame.image.load('Images/End_Screen/reset_button_background.png')
        self.rect_reset_back_ground = self.image_reset_back_ground.get_rect()

        self.rect_reset_back_ground.centerx = self.screen_rect.centerx
        self.rect_reset_back_ground.centery = 500
        self.game_restart = False

    def output(self):
        self.screen.blit(self.imagebg, self.bg_rect)
        self.screen.blit(self.text1, self.rect_text1)
        self.screen.blit(self.image_reset_back_ground, self.rect_reset_back_ground)
        self.screen.blit(self.imagend, self.rect_end)
