import pygame

from settings import Settings
from menu import Menu
# from portal import Portal
# from maze import Maze
# from ghost import Ghost


def run_game():
    """Initialize the game"""
    pp_settings = Settings()

    screen = pygame.display.set_mode((pp_settings.screen_width, pp_settings.screen_height))
    pygame.display.set_caption("Pacman Portal")

    menu = Menu(pp_settings, screen)

    menu.main_menu()


if __name__ == "__main__":
    run_game()
