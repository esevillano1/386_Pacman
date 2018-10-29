class Stats():
    """Track statistics for Space Invaders."""

    def __init__(self, settings):
        """Initialize statistics."""
        self.settings = settings
        self.reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.pacman_lives = self.settings.pacman_lives_left
        self.score = 0
        self.level = 1
