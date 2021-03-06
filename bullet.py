import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage the bullets fired from the ship"""
    def __init__(self, game_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        #Create a bullet rect at (0, 0) and then set it's correct position
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.velocity = game_settings.bullet_velocity

    def update(self):
        """Move the bullet up on the screen"""
        self.y -= self.velocity
        # Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet pon the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)