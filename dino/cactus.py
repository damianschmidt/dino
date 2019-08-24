import pygame
from random import randint


class Cactus:
    def __init__(self, x):
        self.y = 0
        self.x = x
        self.type_of_obstacle = self.get_type_of_obstacle()
        self.img = self.load_img()
        self.velocity = 8.0
        self.next_added = False

    def get_type_of_obstacle(self):
        random_type = randint(0, 2)
        if random_type == 0:
            return 'cactus_big'
        elif random_type == 1:
            return 'cactus_small'
        else:
            return 'cactus_small_many'

    def load_img(self):
        img = pygame.image.load(f'src/img/{self.type_of_obstacle}.png')
        img = pygame.transform.scale(img, (img.get_width() // 2, img.get_height() // 2))
        return img

    def move(self):
        self.x -= self.velocity

    def collide(self, dino):
        dino_mask = pygame.mask.from_surface(dino.img)
        cactus_mask = pygame.mask.from_surface(self.img)
        cactus_offset = (int(round(self.x)) - dino.x, int(round(self.y)) - round(dino.y))

        cactus_collision = dino_mask.overlap(cactus_mask, cactus_offset)

        if cactus_collision:
            return True
        return False

    def draw(self, screen, ground):
        self.y = screen.get_height() - ground.height - self.img.get_height() + 15
        screen.blit(self.img, (self.x, self.y))
