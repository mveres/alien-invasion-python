import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, settings, ship):
        super().__init__()

        self.rect = pygame.Rect((0, ship.rect.top), settings.bullet.size)
        self.rect.centerx = ship.rect.centerx

        self.y = float(self.rect.y)
        self.color = settings.bullet.color

        self.speed_factor = settings.bullet.speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
