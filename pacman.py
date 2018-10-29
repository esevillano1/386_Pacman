import pygame, decimal
from pygame.sprite import Sprite


class Pacman(Sprite):

    def __init__(self, settings, screen, imagename):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load(imagename)
        self.rect = self.image.get_rect()
        self.x_dir = 0
        self.y_dir = 0
        self.rect.x = settings.init_x
        self.rect.y = settings.init_y
        self.centerx = self.rect.x
        self.centery = self.rect.y
        self.timer = 0
        self.direction = "Right"
        self.move_left = True
        self.move_right = True
        self.move_up = True
        self.move_down = True
        self.collider_x = 0
        self.collider_y = 0
        self.update_centers()
        self.create_collider()

    def blitme(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.collider)
        self.screen.blit(self.image, self.rect)

    def update_centers(self):
        # self.top_x = self.rect.midtop[0]
        # self.top_y = self.rect.midtop[1]
        # self.bottom_x = self.rect.midbottom[0]
        # self.bottom_y = self.rect.midbottom[1]
        # self.left_x = self.rect.midleft[0]
        # self.left_y = self.rect.midleft[1]
        # self.right_x = self.rect.midright[0]
        # self.right_y = self.rect.midright[1]
        if self.direction == "Up":
            self.collider_x = self.rect.midtop[0]
            self.collider_y = self.rect.midtop[1]
        elif self.direction == "Down":
            self.collider_x = self.rect.midbottom[0]
            self.collider_y = self.rect.midbottom[1]
        elif self.direction == "Left":
            self.collider_x = self.rect.midleft[0]
            self.collider_y = self.rect.midleft[1]
        elif self.direction == "Right":
            self.collider_x = self.rect.midright[0]
            self.collider_y = self.rect.midright[1]

    def create_collider(self):
        # self.colliders = []
        # self.left_collider = pygame.Rect(self.left_x, self.left_y, 3, 3)
        # self.right_collider = pygame.Rect(self.right_x, self.right_y, 3, 3)
        # self.top_collider = pygame.Rect(self.top_x, self.top_y, 3, 3)
        # self.bottom_collider = pygame.Rect(self.bottom_x, self.bottom_y, 3, 3)
        #
        # self.colliders.append(self.left_collider)
        # self.colliders.append(self.right_collider)
        # self.colliders.append(self.top_collider)
        # self.colliders.append(self.bottom_collider)
        self.collider = pygame.Rect(self.collider_x, self.collider_y, 4, 4)

    def update(self, images, index, direction=None):
        if direction is not None:
            timer = decimal.Decimal(pygame.time.get_ticks() / 1000)
            timer = round(timer, 2)
            if timer - self.timer >= 0.55:
                self.timer = timer
                if index < len(images) - 1:
                    index += 1
                else:
                    index = 0
        self.image = pygame.image.load(images[index])
        if direction == "Up":
            self.image = pygame.transform.rotate(self.image, 90)
        if direction == "Down":
            self.image = pygame.transform.rotate(self.image, -90)
        if direction == "Left":
            self.image = pygame.transform.rotate(self.image, 180)
        if direction == "Right":
            self.image = pygame.transform.rotate(self.image, 0)

        self.centerx += (self.settings.pacman_speed * self.x_dir)
        self.centery += (self.settings.pacman_speed * self.y_dir)

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        self.update_centers()
        self.create_collider()
