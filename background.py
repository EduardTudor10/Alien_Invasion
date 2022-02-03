import pygame
from settings import Settings
screen = pygame.display.set_mode((650, 650))
game_settings = Settings()

class Background():
    def __init__(self):
        self.bg_image = game_settings.bg_image
        self.bg_image = pygame.transform.scale(self.bg_image, (650, 650))
        self.rectbg_image= self.bg_image.get_rect()
        self.bgY1 = 0
        self.bgX1 = 0
        self.bgY2 = self.rectbg_image.height
        self.bgX2 = 0
        self.moving_speed = game_settings.bg_moving_speed

    def update(self):
        self.bgY1 -= self.moving_speed
        self.bgY2 -= self.moving_speed
        if self.bgY1 <= -self.rectbg_image.height:
            self.bgY1 = self.rectbg_image.height
        if self.bgY2 <= -self.rectbg_image.height:
            self.bgY2 = self.rectbg_image.height

    def render(self):
        screen.blit(self.bg_image, (self.bgX1, self.bgY1))
        screen.blit(self.bg_image, (self.bgX2, self.bgY2))