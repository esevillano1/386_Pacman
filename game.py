import pygame
import sys
from maze import Maze
from settings import Settings
from eventloop import EventLoop
from pacman import Pacman
from menu import Menu
from button import Button
from ghost import Ghost
from stats import Stats
from scoreboard import Scoreboard


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_height, self.settings.screen_width))
        pygame.display.set_caption("Pacman Portal")
        self.play_button = Button(self.settings, self.screen, "PLAY GAME", (self.settings.screen_width * 2.75) / 7,(self.settings.screen_height * 5.25) / 7)
        self.high_scores_button = Button(self.settings, self.screen, "HIGH SCORES", (self.settings.screen_width * 2.65) / 7, (self.settings.screen_height * 6) / 7)
        self.stats = Stats(self.settings)
        self.scoreboard = Scoreboard(self.settings, self.screen, self.stats)


        self.maze = Maze(self.settings, self.screen, mazefile="maze.txt", brickfile="square", portalfile="portal", shieldfile="shield", pointfile="powerpill")
        self.pacman_images = ["images/pacman_move_0.png", "images/pacman_move_1.png", "images/pacman_move_2.png"]
        self.pacman = Pacman(self.settings, self.screen, self.pacman_images[0])
        self.pacman_index = 0

        self.inkey_images = [
                                {
                                    "Up": [
                                        "blue_ghost_up_1",
                                        "blue_ghost_up_2"
                                    ]
                                },
                                {
                                    "Down": [
                                        "blue_ghost_down_1",
                                        "blue_ghost_down_2"
                                    ]
                                },
                                {
                                    "Left": [
                                        "blue_ghost_left_1",
                                        "blue_ghost_left_2"
                                    ]
                                },
                                {
                                    "Right": [
                                        "blue_ghost_right_1",
                                        "blue_ghost_right_2"
                                    ]
                                }
                            ]
        self.inkey = Ghost(self.settings, self.screen, self.inkey_images, self.maze.ghost_location[0])

        self.clyde_images = [
                                {
                                    "Up": [
                                        "yellow_ghost_up_1",
                                        "yellow_ghost_up_2"
                                    ]
                                },
                                {
                                    "Down": [
                                        "yellow_ghost_down_1",
                                        "yellow_ghost_down_2"
                                    ]
                                },
                                {
                                    "Left": [
                                        "yellow_ghost_left_1",
                                        "yellow_ghost_left_2"
                                    ]
                                },
                                {
                                    "Right": [
                                        "yellow_ghost_right_1",
                                        "yellow_ghost_right_2"
                                    ]
                                }
                            ]
        self.clyde = Ghost(self.settings, self.screen, self.clyde_images, self.maze.ghost_location[1])

        self.pinky_images = [
                                {
                                    "Up": [
                                        "pink_ghost_up_1",
                                        "pink_ghost_up_2"
                                    ]
                                },
                                {
                                    "Down": [
                                        "pink_ghost_down_1",
                                        "pink_ghost_down_2"
                                    ]
                                },
                                {
                                    "Left": [
                                        "pink_ghost_left_1",
                                        "pink_ghost_left_2"
                                    ]
                                },
                                {
                                    "Right": [
                                        "pink_ghost_right_1",
                                        "pink_ghost_right_2"
                                    ]
                                }
                            ]
        self.pinky = Ghost(self.settings, self.screen, self.pinky_images, self.maze.ghost_location[2])

        self.blinky_images = [
                                {
                                    "Up": [
                                        "red_ghost_up_1",
                                        "red_ghost_up_2"
                                    ]
                                },
                                {
                                    "Down": [
                                        "red_ghost_down_1",
                                        "red_ghost_down_2"
                                    ]
                                },
                                {
                                    "Left": [
                                        "red_ghost_left_1",
                                        "red_ghost_left_2"
                                    ]
                                },
                                {
                                    "Right": [
                                        "red_ghost_right_1",
                                        "red_ghost_right_2"
                                    ]
                                }
                            ]
        self.blinky = Ghost(self.settings, self.screen, self.blinky_images, self.maze.ghost_location[3])

        self.menu = Menu(self.settings, self.screen)

    def __str__(self):
        return "Game((Pacman Portal), maze=" + str(self.maze) + ")"

    def play(self):
        eloop = EventLoop(self.settings, self.pacman, finished=False)

        while not self.stats.game_active:
            if self.settings.high_score_screen:
                self.menu.high_scores()
            else:
                self.menu.start_menu(self.play_button, self.high_scores_button)
            self.check_events()
            pygame.display.update()

        while not eloop.finished:
            self.check_events()
            eloop.check_events()
            self.check_collision()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.pacman.update(self.pacman_images, self.pacman_index, self.pacman.direction)
        self.blit_characters()
        self.scoreboard.show_score()
        pygame.display.flip()

    def blit_characters(self):
        self.pacman.blitme()
        self.inkey.blitme()
        self.clyde.blitme()
        self.pinky.blitme()
        self.blinky.blitme()

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
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_LEFT and self.pacman.move_left:
            self.pacman.x_dir = -1
            self.pacman.y_dir = 0
            self.pacman.direction = "Left"
        if event.key == pygame.K_RIGHT and self.pacman.move_right:
            self.pacman.x_dir = 1
            self.pacman.y_dir = 0
            self.pacman.direction = "Right"
        if event.key == pygame.K_UP and self.pacman.move_up:
            self.pacman.y_dir = -1
            self.pacman.x_dir = 0
            self.pacman.direction = "Up"
        if event.key == pygame.K_DOWN and self.pacman.move_down:
            self.pacman.y_dir = 1
            self.pacman.x_dir = 0
            self.pacman.direction = "Down"

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
            self.pacman.x_dir = 0
        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            self.pacman.y_dir = 0
        # self.pacman.direction = None

    def check_collision(self):
        self.check_dot_collisions()
        self.check_power_pill_collisions()
        # self.check_brick_collisions()

    def check_dot_collisions(self):
        for dot in self.maze.dots:
            if self.pacman.rect.colliderect(dot):
                self.maze.dots.remove(dot)
                self.stats.score += self.settings.dot_value

    def check_power_pill_collisions(self):
        for pill in self.maze.pills:
            if self.pacman.rect.colliderect(pill):
                self.maze.pills.remove(pill)
                self.stats.score += self.settings.power_pill_value

    # def check_brick_collisions(self):
    #     for brick in self.maze.bricks:
    #         if self.pacman.collider.collidepoint(brick.left[0], brick.left[1]):
    #             if self.pacman.collider.left <= brick.right and brick.bottom >= self.pacman.collider_y >= brick.top:
    #                 self.pacman.move_left = False
    #                 print("cant move left")
    #             else:
    #                 self.pacman.move_left = True
    #             if self.pacman.collider.right >= brick.left and brick.bottom >= self.pacman.collider_y >= brick.top:
    #                 self.pacman.move_right = False
    #                 print("cant move right")
    #             else:
    #                 self.pacman.move_right = True
    #             if self.pacman.collider.top <= brick.bottom and brick.left <= self.pacman.collider_x <= brick.right:
    #                 self.pacman.move_up = False
    #                 print("cant move up")
    #             else:
    #                 self.pacman.move_up = True
    #             if self.pacman.collider.bottom >= brick.top and brick.left <= self.pacman.collider_x <= brick.right:
    #                 self.pacman.move_down = False
    #                 print("cant move down")
    #             else:
    #                 self.pacman.move_down = True
    #             return

    def check_play_button(self, settings, play_button, mouse_x, mouse_y):
        """Start a new game when the player clicks Play."""
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not settings.game_active:
            # Reset the game settings.
            settings.initialize_dynamic_settings()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

            self.stats.game_active = True

    def check_high_scores(self, settings, high_scores, mouse_x, mouse_y):
        """Load the list of high scores."""
        button_clicked = high_scores.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            self.menu.high_scores()
            settings.high_score_screen = True


game = Game()
game.play()
