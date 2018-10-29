import pygame.font
from pygame.sprite import Group
from pacman import Pacman


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, settings, screen, stats):
        """Initialize scorekeeping attributes."""
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score images.
        self.prep_scoreboard()

    def prep_scoreboard(self):
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def prep_score(self):
        """Turn the score into a rendered image."""
        score_text = "Score:"
        self.score_text_image = self.font.render(score_text, True, self.text_color, self.settings.bg_color)
        self.score_text_rect = self.score_text_image.get_rect()
        self.score_text_rect.left = self.screen_rect.left + 10
        self.score_text_rect.top = self.settings.screen_height - 20

        rounded_score = int(self.stats.score)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the bottom left of the screen.
        self.score_rect = self.score_image.get_rect()
        if self.stats.score < 100:
            self.score_rect.right = self.score_text_rect.right + 45
        elif self.stats.score < 1000:
            self.score_rect.right = self.score_text_rect.right + 65
        elif self.stats.score < 10000:
            self.score_rect.right = self.score_text_rect.right + 90
        self.score_rect.top = self.settings.screen_height - 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = int(self.stats.high_score)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        self.prep_scoreboard()
        """Draw score and lives to the screen."""
        self.screen.blit(self.score_text_image, self.score_text_rect)
        self.screen.blit(self.score_image, self.score_rect)

        # Draw pacman lives.
        self.screen.blit(self.lives_text, self.lives_text_rect)
        self.lives.draw(self.screen)

    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_lives(self):
        """Show how many ships are left."""
        self.lives = Group()
        for life in range(self.stats.pacman_lives):
            self.pacman = Pacman(self.settings, self.screen, "images/pacman_move_1.png")
            self.pacman.rect.x = self.screen_rect.right - (self.pacman.rect.width * 1.5 + life * self.pacman.rect.width * 1.25)
            self.pacman.rect.y = self.settings.screen_height - 20
            self.lives.add(self.pacman)

        lives_text = "Lives:"
        self.lives_text = self.font.render(lives_text, True, self.text_color, self.settings.bg_color)
        self.lives_text_rect = self.lives_text.get_rect()
        self.lives_text_rect.left = self.screen_rect.right - ((self.settings.pacman_lives * 2.5) * self.pacman.rect.width)
        self.lives_text_rect.top = self.settings.screen_height - 20
