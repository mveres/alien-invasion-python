import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, settings, pos=(0, 0)):
        super().__init__()

        self.image = pygame.image.load('images/alien.png')

        size = self.image.get_rect().size
        self.rect = pygame.Rect(pos, size)

        self.x = float(self.rect.x)
        self.speed_factor = settings.alien.speed_factor
        self.direction = settings.alien.fleet_initial_direction
        self.drop_speed = settings.alien.fleet_drop_speed

    def update(self):
        self.x += self.speed_factor * self.direction
        self.rect.x = self.x

    def drop(self):
        self.rect.y += self.drop_speed
        self.direction *= -1

    def has_reached_edge(self, screen):
        has_reached_right_edge = self.rect.right >= screen.get_rect().right
        has_reached_left_edge = self.rect.left <= 0
        return has_reached_left_edge or has_reached_right_edge

    def has_reached_bottom(self, screen):
        return self.rect.bottom >= screen.get_rect().bottom
