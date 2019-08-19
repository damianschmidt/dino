import pygame
from random import randint


class Cactus:
    def __init__(self, x):
        self.x = x
        self.type_of_obstacle = self.get_type_of_obstacle()
        self.img = self.load_img()
        self.velocity = 10
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

    def collide(self):
        pass

    def draw(self, screen, ground):
        screen.blit(self.img, (self.x, screen.get_height() - ground.height - self.img.get_height() + 15))
