import pygame
from pygame.sprite import Group


class Ship():
    """A class to store al the settings for the player/ship"""
    def __init__(self, game_settings, screen):
        #Loading the ship and get rectangles for the ship and the screen
        self.screen = screen
        self.game_settings = game_settings
        self.image = pygame.image.load("Assets/player_ship.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Setting the ship's position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 10

        #Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)
        #Moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.game_settings.ship_velocity
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.game_settings.ship_velocity

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx