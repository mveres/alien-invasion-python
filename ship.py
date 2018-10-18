import pygame


class Ship():

    def __init__(self, screen, settings):
        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

        self.speed_factor = settings.ship.speed_factor

    def update(self):
        if self.moving_left and self.rect.centerx > 0:
            self.center -= self.speed_factor
        elif self.moving_right and self.rect.centerx < self.screen_rect.right:
            self.center += self.speed_factor

        self.rect.centerx = self.center
