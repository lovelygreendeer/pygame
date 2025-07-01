import pygame, random

COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)


class Cube(pygame.sprite.Sprite):
    def __init__(self, color, pos):
        super().__init__()

        self.image = pygame.Surface([30, 30])
        self.image.fill(COLOR)
        self.image.set_colorkey(SURFACE_COLOR)
        self.color = color
        self.pos = pos

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, 30, 30))
        
        self.rect = self.image.get_rect()

    
    def fill(self, cube_list):
        check_space = Cube('WHITE', 1)
        check_space.rect.x = self.rect.x
        check_space.rect.y = self.rect.y + 40
        check_space.pos = self.pos + 1
        colors = ["RED", "GREEN", "BLUE", "YELLOW"]
        if self.pos < 6 and not pygame.sprite.spritecollideany(check_space, cube_list):
            new_cube = Cube(random.choice(colors), 1)
            new_cube.rect.x = self.rect.x
            new_cube.rect.y = 5
            self.rect.y += 40
            self.pos += 1
            cube_list.add(new_cube)

    
    def touching(self, cube_b):
        if self.color == cube_b.color:
            if (self.rect.x + 40 == cube_b.rect.x or self.rect.x - 40 == cube_b.rect.x) and self.rect.y == cube_b.rect.y:
                return True
            elif (self.rect.y + 40 == cube_b.rect.y or self.rect.y - 40 == cube_b.rect.y) and self.rect.x == cube_b.rect.x:
                return True
        return False


    def break_blocks(self, cube_list):
        for cube in cube_list:
            if self.touching(cube):
                self.kill()
                cube.kill()
                cube.break_blocks(cube_list)



                
    def update(self, bullet_list, cube_list):
        for bullet in bullet_list:
            if self.rect.colliderect(bullet):
                self.break_blocks(cube_list)                
                bullet.kill()

        self.fill(cube_list)

            
   
def makeCubes(number_cubes, num_rows, offset):
    all_sprites_list = pygame.sprite.Group()
    colors = ["RED", "GREEN", "BLUE", "YELLOW"]
    x_loc = 5
    y_loc = 5

    for j in range(num_rows):
        for i in range(number_cubes):
            object_ = Cube(random.choice(colors), j + 1)
            object_.rect.x = x_loc
            object_.rect.y = y_loc
            all_sprites_list.add(object_)
            x_loc = x_loc + offset
        x_loc = 5
        y_loc = y_loc + offset

    return all_sprites_list

def printcord(cube_list):
    for cube in cube_list:
        print('x: ', cube.rect.x, 'y: ', cube.rect.y, 'pos: ', cube.pos)