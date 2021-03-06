import sys
import pygame
from random import randint
from time import sleep
from pygame.sprite import Group

from bullet import Bullet
from alien import Alien
from star import Star


def fire_bullet(settings, ship, bullets):
    if len(bullets) < settings.allowed_bullets_no:
        bullets.add(Bullet(settings, ship))


def check_keydown_events(event, settings, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(settings, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(settings, screen, ship, stars, aliens, bullets):
    screen.fill(settings.bg_color)

    for star in stars:
        pygame.draw.rect(screen, star.color, star.rect)

    screen.blit(ship.image, ship.rect)

    for alien in aliens:
        screen.blit(alien.image, alien.rect)

    for bullet in bullets:
        pygame.draw.rect(screen, bullet.color, bullet.rect)

    # make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets, aliens):
    bullets.update()

    def is_outside(b):
        return b.rect.bottom <= 0

    for bullet in [b for b in bullets if is_outside(b)]:
        bullets.remove(bullet)

    pygame.sprite.groupcollide(bullets, aliens, True, True)


def update_aliens(aliens, screen):
    if any([alien.has_reached_edge(screen) for alien in aliens]):
        for alien in aliens:
            alien.drop()

    aliens.update()


def handle_hit(settings, ship, bullets, aliens, stats):
    stats.ships_left -= 1
    aliens.empty()
    bullets.empty()

    create_fleet(settings, ship, aliens)
    ship.to_center()

    sleep(1)


def collisions_check(settings, screen, ship, bullets, aliens, stats):
    if pygame.sprite.spritecollideany(ship, aliens):
        handle_hit(settings, ship, bullets, aliens, stats)

    if any([alien.has_reached_bottom(screen) for alien in aliens]):
        handle_hit(settings, ship, bullets, aliens, stats)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, ship, aliens)


def get_rows_no(settings, alien_height, ship_height):
    vertical_space = settings.screen_size[1] - 3 * alien_height - ship_height
    return int(vertical_space / (2 * alien_height))


def get_cols_no(settings, alien_width):
    horizontal_space = settings.screen_size[0] - 2 * alien_width
    return int(horizontal_space / (2 * alien_width))


def create_fleet(settings, ship, aliens):
    alien_rect = Alien(settings).rect
    alien_width = alien_rect.width
    alien_height = alien_rect.height
    ship_height = ship.rect.height

    rows = get_rows_no(settings, alien_height, ship_height)
    cols = get_cols_no(settings, alien_width)

    def create_alien(pos):
        (row, col) = pos
        x = alien_width + col * 2 * alien_width
        y = alien_height + row * 2 * alien_height
        return Alien(settings, (x, y))

    table = [(row, col) for row in range(rows) for col in range(cols)]
    for alien in map(create_alien, table):
        aliens.add(alien)


def create_stars(settings):
    (width, height) = settings.screen_size
    no_of_stars = int(width * height * settings.star.density)

    def create_star(_):
        x = randint(0, width)
        y = randint(0, height)
        return Star(settings, (x, y))

    stars = map(create_star, range(no_of_stars))
    return Group(list(stars))
