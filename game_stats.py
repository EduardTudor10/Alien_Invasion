class GameStats():

    """Track statistics of the game"""
    def __init__(self, game_settings):
        """Initialize game statistics"""
        self.game_settings = game_settings
        self.reset_stats()
        #Start Alien Invasion in an active state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1
