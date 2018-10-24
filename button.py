import pygame.font


class Button():

    def __init__(self, si_settings, screen, msg, x=0, y=0, text_color=(255, 255, 255)):
        """Initialize button attributes."""
        self.si_settings = si_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = text_color
        self.font = pygame.font.SysFont(None, 48)
        self.msg = msg

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(x, y, self.width, self.height)

        # The button message needs to be prepped only once.
        self.prep_msg()

    def prep_msg(self):
        """Turn msg into a rendered image and center text on the bottom."""
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, (self.rect.x, self.rect.y))
