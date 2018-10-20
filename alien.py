import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, x=0, y=0):
        super().__init__()

        self.image = pygame.image.load('images/alien.png')

        # start each new alien near the top left of the screen.
        size = self.image.get_rect().size
        self.rect = pygame.Rect((x, y), size)

        self.x = float(self.rect.x)
