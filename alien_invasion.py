import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, settings)
    alien = Alien()
    bullets = Group()

    while True:
        gf.check_events(settings, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(settings, screen, ship, alien, bullets)


run_game()
