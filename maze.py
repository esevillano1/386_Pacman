import pygame
from imagerect import ImageRect

class Maze:
    RED = (200, 0, 0)
    BRICK_SIZE = 13

    def __init__(self, settings, screen, mazefile, brickfile, portalfile, shieldfile, pointfile):
        self.settings = settings
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, "r") as f:
            self.rows = f.readlines()

        self.bricks = []
        self.dots = []
        self.pills = []
        self.shields = []
        self.hportals = []
        self.vportals = []

        sz = Maze.BRICK_SIZE
        self.brick = ImageRect(screen, brickfile, sz, sz)
        self.dot = ImageRect(screen, pointfile, sz, sz)
        self.pill = ImageRect(screen, pointfile, sz * 2, sz * 2)
        self.shield = ImageRect(screen, shieldfile, sz, sz)
        self.hportal = ImageRect(screen, portalfile, sz, sz)
        self.vportal = self.hportal
        self.vportal.image = pygame.transform.rotate(self.hportal.image, 90)
        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def __str__(self): return 'maze(' + self.filename + ')'

    def build(self):
        r = self.brick.rect
        rdot = self.dot.rect
        rpill = self.pill.rect
        rshield = self.shield.rect
        rhportal = self.hportal.rect
        rvportal = self.vportal.rect
        w, h = r.width, r.height
        dx, dy = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == "X":
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                if col == "." and ncol * dx % 2 == 0 or col == "n":
                    self.dots.append(pygame.Rect(ncol * dx, nrow * dy, rdot.width, rdot.height))
                if col == "O":
                    self.pills.append(pygame.Rect(ncol * dx - w/2, nrow * dy - w/2, rpill.width, rpill.height))
                if col == "o":
                    self.shields.append(pygame.Rect(ncol * dx, nrow * dy, rshield.width, rshield.height))
                if col == "h":
                    self.hportals.append(pygame.Rect(ncol * dx, nrow * dy, rhportal.width, rhportal.height))
                if col == "v":
                    self.vportals.append(pygame.Rect(ncol * dx, nrow * dy, rvportal.width, rvportal.height))
                if col == "p":
                    self.settings.init_x = ncol * dx - 5
                    self.settings.init_y = nrow * dy - 5

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.dots:
            self.screen.blit(self.dot.image, rect)
        for rect in self.pills:
            self.screen.blit(self.pill.image, rect)
        for rect in self.shields:
            self.screen.blit(self.shield.image, rect)
        for rect in self.hportals:
            self.screen.blit(self.hportal.image, rect)
        for rect in self.vportals:
            self.screen.blit(self.vportal.image, rect)
