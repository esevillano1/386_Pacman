import pygame


class Ghost:
    def __init__(self, settings, screen, images, location):
        self.settings = settings
        self.screen = screen
        self.images = images
        self.imagename = "images/" + self.images[0]["Up"][0] + ".png"
        self.image = pygame.image.load(self.imagename)
        self.rect = self.image.get_rect()
        self.rect.x = location["x"]
        self.rect.y = location["y"]
        self.x_dir = 0
        self.y_dir = 0
        self.timer = 0
        self.direction = None

    def blitme(self):
        self.screen.blit(self.image, self.rect)