import pygame
import decimal

class Menu:

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.title = "PACMAN PORTAL"
        self.timer = 0
        self.indices = [0, 0, 0, 0, 0]
        self.x = -2
        self.turn = False
        self.ghost_intro = False

    def start_menu(self, play_button, high_scores):
        pacman_images = ["images/pacman_move_0.png", "images/pacman_move_1.png", "images/pacman_move_2.png", "images/pacman_move_1.png"]
        light_blue_ghost_images = ["images/blue_ghost_right_1.png", "images/blue_ghost_right_2.png"]
        yellow_ghost_images = ["images/yellow_ghost_right_1.png", "images/yellow_ghost_right_2.png"]
        pink_ghost_images = ["images/pink_ghost_right_1.png", "images/pink_ghost_right_2.png"]
        red_ghost_images = ["images/red_ghost_right_1.png", "images/red_ghost_right_2.png"]
        blue_ghost_images = ["images/blue_ghost_1.png", "images/blue_ghost_2.png"]

        if not self.ghost_intro:
            timer = int(round(pygame.time.get_ticks() / 1000))
            if 2 <= timer < 5:
                self.animateGhost(light_blue_ghost_images, 0, "Clyde", (2.25/3), (1/3), (0, 0, 255))
            elif 5 <= timer < 8:
                self.animateGhost(yellow_ghost_images, 0, "iNKEY", (2.25/3), (1/3), (255, 255, 0))
            elif 8 <= timer < 11:
                self.animateGhost(pink_ghost_images, 0, "PiNKY", (2.25/3), (1/3), (255, 0, 240))
            elif 11 <= timer < 14:
                self.animateGhost(red_ghost_images, 0, "BLiNKY", (2.25/3), (1/3), (255, 0, 0))
            elif timer > 14:
                self.ghost_intro = True
        else:
            font = pygame.font.SysFont(None, 192)
            title = font.render("PACMAN", True, (255, 255, 255))
            self.screen.fill((0, 0, 0))
            self.screen.blit(title, (self.settings.screen_width/8, self.settings.screen_height/24))

            font = pygame.font.SysFont(None, 128)
            title = font.render("Portal", True, (255, 255, 255))
            self.screen.blit(title, (self.settings.screen_width / 3, self.settings.screen_height / 5.5))

            if self.x < 7.5 and not self.turn:
                self.x += 0.02
                self.animate(light_blue_ghost_images, self.indices, 1, (self.x/6), (3/7))
                self.animate(yellow_ghost_images, self.indices, 1, ((self.x + 0.25)/6), (3/7))
                self.animate(pink_ghost_images, self.indices, 1, ((self.x + 0.5)/6), (3/7))
                self.animate(red_ghost_images, self.indices, 1, ((self.x + 0.75)/6), (3/7))
                self.animate(pacman_images, self.indices, 0, ((self.x + 1.75)/6), (3/7))

            elif self.x > -2 and self.turn:
                self.x -= 0.02
                self.animate(blue_ghost_images, self.indices, 1, (self.x / 6), (3 / 7))
                self.animate(blue_ghost_images, self.indices, 1, ((self.x + 0.25) / 6), (3 / 7))
                self.animate(blue_ghost_images, self.indices, 1, ((self.x + 0.5) / 6), (3 / 7))
                self.animate(blue_ghost_images, self.indices, 1, ((self.x + 0.75)/ 6), (3 / 7))
                self.animate(pacman_images, self.indices, 0, ((self.x + 1.75)/6), (3/7))

            else:
                self.turn = True

            play_button.draw_button()
            high_scores.draw_button()

    def high_scores(self):
        file = open("text_files/scores.txt", "r")
        line_num = 1
        title_font = pygame.font.SysFont(None, 128)
        title = title_font.render("HIGH SCORES", True, (255, 255, 255))
        self.screen.fill((0, 0, 0))
        self.screen.blit(title, (self.settings.screen_width / 6, self.settings.screen_height / 12))
        for line in file:
            line_font = pygame.font.SysFont(None, 48)
            high_score_line = line_font.render(str(line).strip(), True, (255, 255, 255))
            self.screen.blit(high_score_line, ((self.settings.screen_width * 2.5) / 7, (self.settings.screen_height * (1 + line_num)) / 8))
            line_num += 0.5
        returnToStart = line_font.render("Press Space to return to the start menu...", True, (255, 255, 255))
        self.screen.blit(returnToStart, ((self.settings.screen_width / 7), ((self.settings.screen_height * 7) / 8)))
        file.close()

    def animate(self, images, list, index, x, y):
        timer = decimal.Decimal(pygame.time.get_ticks()/1000)
        timer = round(timer, 3)
        if timer - self.timer >= 0.065:
            self.timer = timer
            if list[index] < len(images) - 1:
                list[index] += 1
            else:
                list[index] = 0
        self.player = pygame.image.load(images[list[index]])
        self.rect = self.player.get_rect()
        if self.rect.left > self.settings.screen_width * 1.25 or self.rect.right < self.settings.screen_width and self.turn:
            self.player = pygame.transform.flip(self.player, True, False)
        if self.turn and self.x < 0 and index == len(list) - 1:
            self.turn = False
        self.screen.blit(self.player, (self.settings.screen_width * x, self.settings.screen_height * y))

    def animateGhost(self, ghost_images, index, name, x, y, color):
        font = pygame.font.SysFont(None, 96)
        title = font.render('"' + name + '"', True, color)
        self.screen.fill((0, 0, 0))
        self.screen.blit(title, (self.settings.screen_width/4, self.settings.screen_height/3))

        timer = decimal.Decimal(pygame.time.get_ticks()/1000)
        timer = round(timer, 3)
        if timer - self.timer >= 0.065:
            self.timer = timer
            if index < len(ghost_images) - 1:
                index += 1
            else:
                index = 0
        self.player = pygame.image.load(ghost_images[index])
        player = pygame.transform.scale2x(self.player)
        self.rect = player.get_rect()
        self.screen.blit(player, (self.settings.screen_width * x, self.settings.screen_height * y))

    def reset_animation(self):
        self.x = -2
