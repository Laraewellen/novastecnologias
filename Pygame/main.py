import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
import game_functions as gf

from pygame.sprite import Group


def run_game():
    pygame.init()
    
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Invasão Aliens")

    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(screen,aliens,ship)

    while True:
        gf.check_events(bullets, screen, ship)
        ship.update()
        gf.update_bullets(bullets, aliens)
        gf.update_aliens(aliens)

        # ⚠️ Essa parte precisa estar dentro do while e depois da criação de 'ship'
        if gf.check_ship_collision(ship, aliens, screen):
            ship = Ship(screen)
            bullets = Group()
            aliens = Group()
            gf.create_fleet(screen, aliens, ship)
        if gf.check_win_condition(aliens, screen):
            ship = Ship(screen)
            bullets = Group()
            aliens = Group()
            gf.create_fleet(screen, aliens, ship)



        gf.update_screen(screen, ship, bullets, aliens)

run_game()
