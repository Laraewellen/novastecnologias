import pygame
import sys
from bullet import Bullet
from alien import Alien

def check_events(bullets,screen,ship):

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    ship.moving_left = True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen,ship)
                    bullets.add(new_bullet)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    ship.moving_left = False

def update_screen(screen,ship,bullets,aliens):
    bg_color = (230,230,230)
    screen.fill(bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    aliens.draw(screen)
    pygame.display.flip()


def create_fleet(screen,aliens, ship):
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    available_space_x = screen.get_rect().width - alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))

    ship_height = ship.rect.height
    available_space_y = screen.get_rect().height - 3*alien_height - ship_height
    number_rows = int(available_space_y/(2*alien_height))
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            alien = Alien(screen)
            alien.x = alien_width + 2*alien_width*alien_number
            alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
            alien.rect.x = alien.x
            aliens.add(alien)


def check_fleet_edges(aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(aliens)
            break

def change_fleet_direction(aliens):
    for alien in aliens.sprites():
        alien.rect.y += alien.fleet_drop_speed
        alien.fleet_direction *=-1
    
def update_aliens(aliens):
    check_fleet_edges(aliens)
    aliens.update()
    
def update_bullets(bullets, aliens):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Verifica colisões entre bullets e aliens
    pygame.sprite.groupcollide(bullets, aliens, True, True)

def check_ship_collision(ship, aliens, screen):
    if pygame.sprite.spritecollideany(ship, aliens):
        show_game_over_screen(screen)
        return True
    return False

def show_game_over_screen(screen):
    font = pygame.font.SysFont(None, 72)
    small_font = pygame.font.SysFont(None, 48)

    screen.fill((0, 0, 0))

    msg = font.render("Você perdeu!", True, (255, 0, 0))
    retry = small_font.render("Pressione R para tentar novamente", True, (255, 255, 255))
    quit_msg = small_font.render("Pressione Q para sair", True, (255, 255, 255))

    screen.blit(msg, (screen.get_width()//2 - msg.get_width()//2, 250))
    screen.blit(retry, (screen.get_width()//2 - retry.get_width()//2, 350))
    screen.blit(quit_msg, (screen.get_width()//2 - quit_msg.get_width()//2, 400))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False  # sai do loop e reinicia o jogo
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

def check_win_condition(aliens, screen):
    if len(aliens) == 0:
        font = pygame.font.SysFont(None, 72)
        small_font = pygame.font.SysFont(None, 48)

        screen.fill((0, 0, 0))

        win_msg = font.render("Você venceu!", True, (0, 255, 0))
        retry = small_font.render("Pressione R para jogar novamente", True, (255, 255, 255))
        quit_msg = small_font.render("Pressione Q para sair", True, (255, 255, 255))

        screen.blit(win_msg, (screen.get_width()//2 - win_msg.get_width()//2, 250))
        screen.blit(retry, (screen.get_width()//2 - retry.get_width()//2, 350))
        screen.blit(quit_msg, (screen.get_width()//2 - quit_msg.get_width()//2, 400))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

        return True  # reiniciar
    return False  # continuar jogando

def check_win_condition(aliens, screen):
    if len(aliens) == 0:
        font = pygame.font.SysFont(None, 72)
        small_font = pygame.font.SysFont(None, 48)

        screen.fill((0, 0, 0))

        win_msg = font.render("Você venceu!", True, (0, 255, 0))
        retry = small_font.render("Pressione R para jogar novamente", True, (255, 255, 255))
        quit_msg = small_font.render("Pressione Q para sair", True, (255, 255, 255))

        screen.blit(win_msg, (screen.get_width()//2 - win_msg.get_width()//2, 250))
        screen.blit(retry, (screen.get_width()//2 - retry.get_width()//2, 350))
        screen.blit(quit_msg, (screen.get_width()//2 - quit_msg.get_width()//2, 400))

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        waiting = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

        return True  # reiniciar
    return False  # continuar jogando

