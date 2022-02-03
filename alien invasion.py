import pygame


from pygame.sprite import Group
from settings import Settings
from background import Background
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
import game_functions as gf
from pygame import mixer


def run_game():
    pygame.init()
    mixer.init()
    game_settings = Settings()
    screen = pygame.display.set_mode((game_settings.width, game_settings.height))
    pygame.display.set_caption("Alien Invaders")
    pygame.display.set_icon(game_settings.game_icon)
    font = pygame.font.Font("Assets/ARCADE_N.TTF", 25)
    text = font.render("Press any key to start", 1, (255, 255, 255))
    mixer.music.load("Assets/bg_music.mp3")
    mixer.music.play()
    mixer.music.rewind()
    mixer.music.set_volume(0.05)

    #Create an instance to store game statistics
    stats = GameStats(game_settings)
    sb = Scoreboard(game_settings, screen, stats)
    #Make a ship
    ship = Ship(game_settings, screen)
    #Make a group to store the bullets and a group for aliens
    bullets = Group()
    aliens = Group()
    background = Background()
    gf.create_fleet(game_settings, screen, ship, aliens)


    while True:
        if stats.game_active == False:
            background.update()
            background.render()
            screen.blit(text, (650 // 2 - text.get_width() / 2, 300))
            pygame.display.flip()

        elif stats.game_active:
            ship.update()
            gf.update_bullets(game_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(game_settings, screen, stats, sb, ship, aliens, bullets, background)
        gf.check_events(game_settings, screen, stats, sb, ship, bullets)
        background.update()
        background.render()

run_game()