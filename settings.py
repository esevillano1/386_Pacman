class Settings:
    """Initialize the settings for the game."""
    def __init__(self):
        print("Settings")
        self.init_x = 0
        self.init_y = 0
        self.screen_height = 740
        self.screen_width = 715
        self.game_active = False
        self.high_score_screen = False
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.pacman_speed = 5
