import pygame
class GameStats:
    """Tracks Game stats"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Starting game in an active state
        self.game_active = True

        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.reset_stats()

        # Starting game in an inactive state
        self.game_active = False

        # High score
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

        # Restart bg music
        pygame.mixer.stop()
        pygame.mixer.init()
        pygame.mixer.music.load("Sounds/invaders.wav")
        pygame.mixer.music.play(-1)
