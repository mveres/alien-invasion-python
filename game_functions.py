import sys
import pygame
from bullet import Bullet


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


def update_screen(settings, screen, ship, bullets):
    screen.fill(settings.bg_color)

    screen.blit(ship.image, ship.rect)

    for bullet in bullets:
        pygame.draw.rect(screen, bullet.color, bullet.rect)

    # make the most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets):
    bullets.update()

    def is_out(b): return b.rect.bottom <= 0

    bullets_to_delete = [b for b in bullets.copy() if is_out(b)]

    for b in bullets_to_delete:
        bullets.remove(b)
