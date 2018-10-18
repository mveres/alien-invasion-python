import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, settings)
    bullets = Group()

    while True:
        gf.check_events(settings, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(settings, screen, ship, bullets)


run_game()
