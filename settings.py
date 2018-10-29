class Settings:
    """Initialize the settings for the game."""
    def __init__(self):
        print("Settings")
        self.init_x = 0
        self.init_y = 0
        self.bg_color = (0, 0, 0)
        self.screen_height = 715
        self.screen_width = 735
        self.speed_increase = 0
        self.pacman_lives = 3
        self.game_active = False
        self.high_score_screen = False
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initial speeds for each character that increases with each successive round
        self.pacman_speed = 5
        self.pacman_lives_left = 3

        self.inkey_speed = 1.5 + self.speed_increase
        self.clyde_speed = 2.5 + self.speed_increase
        self.pinky_speed = 3.25 + self.speed_increase
        self.blinky_speed = 4 + self.speed_increase

        # Value for each game assets that can be eaten
        self.dot_value = 10
        self.power_pill_value = 50
        self.ghost_values = [200, 400, 800, 1600]
        self.fruit_values = [100, 300, 500, 700, 1000]

    def increase_difficulty(self):
        self.speed_increase = 1
