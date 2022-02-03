import sys
from time import sleep
import pygame

from bullet import Bullet
from alien import Alien

def check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, screen, ship, aliens, bullets)
            game_settings.initialize_dynamic_settings()
            break

def ship_hit(game_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship beng hit by an alien"""
    if game_settings.ship_limit > 0:
        game_settings.ship_limit -= 1
        # Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        # Create a new fleet and center the ship
        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
        game_settings.initialize_dynamic_settings()
    elif game_settings.ship_limit == 0:
        stats.game_active = False

def update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets):
    """Update position for bullets and get rid of old bullets"""
    bullets.update()
    # Get rid of the old bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))
    check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(game_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet - alien collisions"""
    # Check for any bullets that have hit aliens
    # If so get rid of the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Destroy the existing bullets, speed up the game and create new fleet
        bullets.empty()
        game_settings.increase_speed()
        #Increase level
        stats.level += 1
        sb.prep_level()
        create_fleet(game_settings, screen, ship, aliens)
    if collisions:
        for aliens in collisions.values():
            stats.score += game_settings.alien_points * len(aliens)
            sb.prep_score()

def check_fleet_edges(game_settings, aliens):
    """Respond if any aliens have reached an edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            break

def change_fleet_direction(game_settings, aliens):
    """Drop the fleet and change it's direction"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.fleet_drop
    game_settings.fleet_direction *= -1

def get_number_aliens_x(game_settings, alien_width):
    """"Determine the number of aliens that fit in a row"""
    available_space_x = game_settings.width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(game_settings, alien_height):
    """Determine the number of rows of aliens that fit on the screen"""
    available_space_y = (game_settings.height - (3 * alien_height) - 60)
    number_rows = int(available_space_y / (2 * alien_height) - 1)
    return number_rows

def create_alien(game_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row"""
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(game_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    alien = Alien(game_settings, screen)
    number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
    number_rows = get_number_rows(game_settings, alien.rect.height)
    # Create the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(game_settings, screen, aliens, alien_number, row_number)

def check_keydown_events(event, game_settings, screen, ship, bullets):
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        sys.exit()

def fire_bullet(game_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached"""
    # Create a new bullet and add it to the bullet group
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False

def check_events(game_settings, screen, stats, sb , ship, bullets):
    """Check for keyboard events or mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN and stats.game_active == False:
                stats.game_active = True
                sleep(0.5)

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_aliens(game_settings, stats, screen, ship, aliens, bullets):
    """Check if the fleet is at an edge,
        and then update the position of the fleet"""
    check_fleet_edges(game_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(game_settings, stats, screen, ship, aliens, bullets)

def update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, background):
    """Update images to the screen and flip to the new screen"""
    sb.show_score()
    # Redraw all the bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    if stats.game_active == True:
        ship.blitme()
        aliens.draw(screen)
        pygame.display.flip()
