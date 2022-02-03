import pygame
pygame.font.init()

class Settings():
    """A class to store al the settings of the game"""
    def __init__(self):
        """Initialize tge game's static settings"""
        #Screen, Background and Icon settings
        self.dimension_variable = 650
        self.width = self.dimension_variable
        self.height = self.dimension_variable
        self.bg_image = pygame.image.load("Assets/bg_image.png")
        self.bg_image = pygame.transform.scale(self.bg_image, (self.dimension_variable, self.dimension_variable))
        self.bg_moving_speed = 3
        self.game_icon = pygame.image.load("Assets/game_icon.png")
        self.game_icon = pygame.transform.scale(self.game_icon, (32, 32))

        # Ship settings
        self.ship_velocity = 3
        self.ship_speed = 4
        self.ship_limit = 3

        #Bullet settings
        self.bullet_velocity = 7
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = 255, 20, 28
        self.bullets_allowed = 3

        #Alien settings
        self.alien_speed = 1
        self.fleet_drop = 10

        #How quickly the game speeds up
        self.speedup_scale = 1.2
        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1
        # Fleet direction oaf 1 represents right, -1 represents left
        self.fleet_direction = 1
        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

