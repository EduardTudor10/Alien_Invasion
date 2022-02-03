import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, game_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        #Load the alien ship and get it's rectangle
        self.image = pygame.image.load("Assets/alien.png")
        self.image = pygame.transform.scale(self.image, (45, 45))
        self.rect = self.image.get_rect()

        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height - 20

        #Store the alien's exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move alien right or left"""
        self.x += (self.game_settings.alien_speed * self.game_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location"""
        self.screen.blit(self.image, self.rect)

