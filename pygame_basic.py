# Example file showing a basic pygame "game loop"
import pygame
from cube import Cube, makeCubes, printcord
from bullet import Bullet

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
shoot = False

block_y = screen.get_width() / 4
all_sprites_list = makeCubes(32, 6, 40)
bullet_list = pygame.sprite.Group()
player_loc = pygame.Vector2(640, 700)
printcord(all_sprites_list)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bullet_list.add(Bullet(player_loc.x))

    #updates
    all_sprites_list.update(bullet_list, all_sprites_list)  
    bullet_list.update(dt)  

    #screenfill
    screen.fill("purple")

    #draw 
    all_sprites_list.draw(screen)
    bullet_list.draw(screen)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_loc.x - 300 * dt > 10:
        player_loc.x -= 300 * dt
    if keys[pygame.K_RIGHT] and player_loc.x + 300 * dt < 1270:
        player_loc.x += 300 * dt



    pygame.draw.circle(screen, "BLACK", player_loc, 20)

    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()