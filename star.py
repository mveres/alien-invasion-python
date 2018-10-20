import pygame
from pygame.sprite import Sprite


class Star(Sprite):

    def __init__(self, settings, pos=(0, 0)):
        super().__init__()

        self.rect = pygame.Rect(pos, (settings.star.size, settings.star.size))
        self.color = settings.star.color
