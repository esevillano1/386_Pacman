import pygame, decimal


class Pacman:

    def __init__(self, settings, screen, imagename):
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load(imagename)
        self.rect = self.image.get_rect()
        self.x_dir = 0
        self.y_dir = 0
        self.rect.x = settings.init_x
        self.rect.y = settings.init_y
        self.timer = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, images, index):
        timer = int(round(pygame.time.get_ticks() / 1000))
        # timer = round(timer, 3)
        if timer - self.timer >= 1:
            self.timer = timer
            if index < len(images) - 1:
                index += 1
            else:
                index = 0
        self.image = pygame.image.load(images[index])
        self.rect.x += (self.settings.pacman_speed * self.x_dir)
        self.rect.y += (self.settings.pacman_speed * self.y_dir)
