import pygame
import sys
from pacman import Pacman

class EventLoop:
    def __init__(self, settings, pacman, finished):
        self.settings = settings
        self.pacman = pacman
        self.finished = finished

    def __str__(self):
        return "eventloop, finished=" + str(self.finished) + ")"

    @staticmethod
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()