import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """A class to represent the scoreboard of the game"""
    def __init__(self, game_settings, screen, stats):
        """Initialize scorekeeping attributes"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        #Font settings for score
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font("Assets/ARCADE_N.TTF", 20)

        #Prepare the initial score image
        self.prep_score()
        self.prep_level()

    def prep_level(self):
        """Turn the level into a rendered image"""
        self.level_image = self.font.render("Level" + " " + str(self.stats.level), True, self.text_color)

        #Position
        self.level_rect = self.level_image.get_rect()
        self.level_rect.y = self.screen_rect.left - 20
        self.level_rect.top = 20

    def prep_score(self):
        """Turn the score into a rendered image"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color)

        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw the score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
