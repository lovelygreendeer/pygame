# Example file showing a basic pygame "game loop"
import pygame
from cube import Cube, makeCubes

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

block_y = screen.get_width() / 4

all_sprites_list = makeCubes(10, 50)



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites_list.update()
    screen.fill("purple")
    all_sprites_list.draw(screen)
   


    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()