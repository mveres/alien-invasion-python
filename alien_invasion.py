import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats


def run_game():
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(settings, ship, aliens)
    stars = gf.create_stars(settings)

    stats = GameStats(settings)

    while True:
        gf.check_events(settings, ship, bullets)
        ship.update()
        gf.update_aliens(aliens, screen)
        gf.update_bullets(bullets, aliens)

        gf.collisions_check(settings, screen, ship, bullets, aliens, stats)

        gf.update_screen(settings, screen, ship, stars, aliens, bullets)


run_game()
