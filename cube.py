import pygame

COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)


class Cube(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()

        self.image = pygame.Surface([30, 30])
        self.image.fill(COLOR)
        self.image.set_colorkey(SURFACE_COLOR)

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, 30, 30))
        
        self.rect = self.image.get_rect()

def makeCubes(number_cubes, offset):
    all_sprites_list = pygame.sprite.Group()
    x_loc = 50
    y_loc = 50

    for i in range(number_cubes):
        object_ = Cube('RED')
        object_.rect.x = x_loc
        object_.rect.y = y_loc
        all_sprites_list.add(object_)
        x_loc = x_loc + offset

    return all_sprites_list