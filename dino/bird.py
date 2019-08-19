from random import randint

import pygame


class Bird:
    def __init__(self, x):
        self.type_of_bird = self.get_type_of_bird()
        self.x = x
        self.y = self.set_y()
        self.velocity = 10
        self.next_added = False

        self.imgs = self.load_img()
        self.img = self.imgs[0]
        self.flap_count = 0
        self.animation_time = 5

    def get_type_of_bird(self):
        random_type = randint(0, 2)
        if random_type == 0:
            return 'high'
        elif random_type == 1:
            return 'mid'
        else:
            return 'low'

    def set_y(self):
        if self.type_of_bird == 'high':
            return 60
        elif self.type_of_bird == 'mid':
            return 28
        else:
            return 5

    def load_img(self):
        imgs = [pygame.image.load(f'src/img/bird_{i}.png') for i in range(1, 3)]
        imgs = [pygame.transform.scale(img, (img.get_width() // 2, img.get_height() // 2)) for img in imgs]
        return imgs

    def move(self):
        self.x -= self.velocity

    def collide(self):
        pass

    def draw(self, screen, ground):
        if self.flap_count < self.animation_time:
            self.img = self.imgs[0]
        elif self.flap_count < 2 * self.animation_time:
            self.img = self.imgs[1]
        elif self.flap_count < 3 * self.animation_time + 1:
            self.img = self.imgs[0]
            self.flap_count = 0

        self.flap_count += 1
        screen.blit(self.img, (self.x, screen.get_height() - ground.height - self.img.get_height() - self.y))

