import pygame

WHITE    = ( 255, 255, 255 )

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, 700))
        pygame.draw.circle(self.image, WHITE, (5, 5), 5)

    def update(self, delta):
        self.rect.y -= 300 * delta

