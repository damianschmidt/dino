import pygame


class Dino:
    def __init__(self):
        self.y = 0
        self.x = 100
        self.y_change = 0
        self.y_velocity = 0
        self.gravity = 1

        self.imgs = self.load_images()
        self.img = self.imgs[0]
        self.img_count = 0
        self.animation_time = 3

        self.is_run = True
        self.is_duck = False
        self.is_jump = False

    def load_images(self):
        imgs = [[pygame.image.load(f'src/img/dino_run_{str(x)}.png') for x in range(1, 3)],
                [pygame.image.load(f'src/img/dino_duck_{str(x)}.png') for x in range(1, 3)],
                [pygame.image.load(f'src/img/dino_jump.png')]]

        scaled_imgs = [pygame.transform.scale(img, (img.get_width() // 2, img.get_height() // 2))
                       for img_set in imgs
                       for img in img_set]
        return scaled_imgs

    def jump(self):
        if self.y_change == 0:
            self.gravity = 2
            self.y_velocity = 22

    def duck(self):
        if self.y_change != 0:
            self.gravity = 6
        self.is_duck = True
        self.is_run = False

    def run(self):
        if self.y_change != 0:
            self.gravity = 4
        self.is_duck = False
        self.is_run = True

    def move(self):
        self.y_change += self.y_velocity
        if self.y_change > 0:
            self.y_velocity -= self.gravity
        else:
            self.y_velocity = 0
            self.y_change = 0

        if not self.is_duck and self.y_change != 0:
            self.is_run = False
            self.is_jump = True
        elif not self.is_duck:
            self.is_jump = False
            self.is_run = True

    def draw(self, screen, ground):
        if self.is_run:
            i, j = 0, 1
        elif self.is_duck:
            i, j = 2, 3
        else:
            i, j = 4, 4

        if self.img_count <= self.animation_time:
            self.img = self.imgs[i]
        elif self.img_count <= 2 * self.animation_time:
            self.img = self.imgs[j]
        elif self.img_count <= 3 * self.animation_time + 1:
            self.img = self.imgs[i]
            self.img_count = 0

        self.img_count += 1
        self.y = screen.get_height() - ground.height - self.img.get_height() + 15 - self.y_change
        screen.blit(self.img, (self.x, self.y))
