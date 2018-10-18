import sys
import pygame
from pygame.sprite import Group

from bullet import Bullet
from alien import Alien


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


def update_screen(settings, screen, ship, aliens, bullets):
    screen.fill(settings.bg_color)

    screen.blit(ship.image, ship.rect)

    for alien in aliens:
        screen.blit(alien.image, alien.rect)

    for bullet in bullets:
        pygame.draw.rect(screen, bullet.color, bullet.rect)

    # make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()

    def is_inside(b):
        return b.rect.bottom > 0

    return Group([b for b in bullets if is_inside(b)])


def get_rows_no(settings, alien_height, ship_height):
    vertical_space = settings.screen_size[1] - 3 * alien_height - ship_height
    return int(vertical_space / (2 * alien_height))


def get_cols_no(settings, alien_width):
    horizontal_space = settings.screen_size[0] - 2 * alien_width
    return int(horizontal_space / (2 * alien_width))


def create_fleet(settings, screen, ship):
    alien_width = Alien().rect.width
    alien_height = Alien().rect.height
    ship_height = ship.rect.height

    rows = get_rows_no(settings, alien_height, ship_height)
    cols = get_cols_no(settings, alien_width)

    def create_alien(pos):
        x = alien_width + pos[1] * 2 * alien_width
        y = alien_height + pos[0] * 2 * alien_height
        return Alien(x, y)

    table = [(row, col) for row in range(rows) for col in range(cols)]
    aliens = map(create_alien, table)
    return Group(list(aliens))
