import pygame
import sys
from maze import Maze
from settings import Settings
from eventloop import EventLoop
from pacman import Pacman
from menu import Menu
from button import Button

class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("Pacman Portal")
        self.play_button = Button(self.settings, self.screen, "PLAY GAME", (self.settings.screen_width * 2.75) / 7,(self.settings.screen_height * 5.25) / 7)
        self.high_scores_button = Button(self.settings, self.screen, "HIGH SCORES", (self.settings.screen_width * 2.65) / 7, (self.settings.screen_height * 6) / 7)

        self.maze = Maze(self.settings, self.screen, mazefile="maze.txt", brickfile="square", portalfile="portal", shieldfile="shield", pointfile="powerpill")
        self.pacman_images = ["images/pacman_move_0.png", "images/pacman_move_1.png", "images/pacman_move_2.png", "images/pacman_move_1.png"]
        self.pacman = Pacman(self.settings, self.screen, self.pacman_images[0])
        self.pacman_index = 0
        self.menu = Menu(self.settings, self.screen)

    def __str__(self):
        return "Game((Pacman Portal), maze=" + str(self.maze) + ")"

    def play(self):
        eloop = EventLoop(self.settings, self.pacman, finished=False)

        while not self.settings.game_active:
            if self.settings.high_score_screen:
                self.menu.high_scores()
            else:
                self.menu.start_menu(self.play_button, self.high_scores_button)
            self.check_events()
            pygame.display.update()

        while not eloop.finished:
            self.check_events()
            eloop.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.pacman.update(self.pacman_images, self.pacman_index)
        self.pacman.blitme()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_play_button(self.settings, self.play_button, mouse_x, mouse_y)
                self.check_high_scores(self.settings, self.high_scores_button, mouse_x, mouse_y)

    def check_keydown_event(self, event):
        if event.key == pygame.K_SPACE:
            self.settings.high_score_screen = False
            self.menu.reset_animation()
        elif event.key == pygame.K_q:
            sys.exit()
        else:
            self.check_collision(event)

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self.pacman.x_dir = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            self.pacman.y_dir = 0

    def check_collision(self, event):
        for dot in self.maze.dots:
            if self.pacman.rect.colliderect(dot):
                self.maze.dots.remove(dot)
        for brick in self.maze.bricks:
            if self.pacman.rect.colliderect(brick):
                return
        if event.key == pygame.K_LEFT:
            self.pacman.x_dir = -1
        if event.key == pygame.K_RIGHT:
            self.pacman.x_dir = 1
        if event.key == pygame.K_UP:
            self.pacman.y_dir = -1
        if event.key == pygame.K_DOWN:
            self.pacman.y_dir = 1

    def check_play_button(self, settings, play_button, mouse_x, mouse_y):
        """Start a new game when the player clicks Play."""
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not settings.game_active:
            # Reset the game settings.
            settings.initialize_dynamic_settings()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

            settings.game_active = True

    def check_high_scores(self, settings, high_scores, mouse_x, mouse_y):
        """Load the list of high scores."""
        button_clicked = high_scores.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            self.menu.high_scores()
            settings.high_score_screen = True


game = Game()
game.play()
