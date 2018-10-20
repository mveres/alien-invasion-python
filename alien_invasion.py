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
    aliens = gf.create_fleet(settings, ship)
    stars = gf.create_stars(settings)

    while True:
        gf.check_events(settings, ship, bullets)
        ship.update()
        bullets = gf.update_bullets(bullets)

        gf.update_screen(settings, screen, ship, stars, aliens, bullets)


run_game()
