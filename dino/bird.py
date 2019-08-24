from random import randint

import pygame


class Bird:
    def __init__(self, x):
        self.type_of_bird = self.get_type_of_bird()
        self.x = x
        self.y = 0
        self.y_type = self.set_y_type()
        self.velocity = 8.0
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

    def set_y_type(self):
        if self.type_of_bird == 'high':
            return 45
        elif self.type_of_bird == 'mid':
            return 20
        else:
            return -10

    def load_img(self):
        imgs = [pygame.image.load(f'src/img/bird_{i}.png') for i in range(1, 3)]
        imgs = [pygame.transform.scale(img, (img.get_width() // 2, img.get_height() // 2)) for img in imgs]
        return imgs

    def move(self):
        self.x -= self.velocity

    def collide(self, dino):
        dino_mask = pygame.mask.from_surface(dino.img)
        bird_mask = pygame.mask.from_surface(self.img)
        bird_offset = (int(round(self.x)) - dino.x, int(round(self.y)) - round(dino.y))
        bird_collision = dino_mask.overlap(bird_mask, bird_offset)

        if bird_collision:
            return True
        return False

    def draw(self, screen, ground):
        if self.flap_count < self.animation_time:
            self.img = self.imgs[0]
        elif self.flap_count < 2 * self.animation_time:
            self.img = self.imgs[1]
        elif self.flap_count < 3 * self.animation_time + 1:
            self.img = self.imgs[0]
            self.flap_count = 0

        self.flap_count += 1
        self.y = screen.get_height() - ground.height - self.img.get_height() - self.y_type
        screen.blit(self.img, (self.x, self.y))

