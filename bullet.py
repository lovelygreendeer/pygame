import pygame

COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([50, 50])
        #self.image.fill(COLOR)
        #self.image.set_colorkey(SURFACE_COLOR)

        pygame.draw.ellipse(self.image, 'WHITE', pygame.Rect(0, 0, 50, 50))
        
        self.rect = self.image.get_rect()