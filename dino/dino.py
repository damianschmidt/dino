import pygame


class Dino:
    def __init__(self):
        self.y_position = 0
        self.y_velocity = 0
        self.gravity = 1

        self.imgs = self.load_images()
        self.img = self.imgs[0]
        self.img_count = 0
        self.animation_time = 3

        self.run = True
        self.duck = False
        self.jump = False

    def load_images(self):
        imgs = [[pygame.image.load(f'src/img/dino_run_{str(x)}.png') for x in range(1, 3)],
                [pygame.image.load(f'src/img/dino_duck_{str(x)}.png') for x in range(1, 3)],
                [pygame.image.load(f'src/img/dino_jump.png')]]

        scaled_imgs = [pygame.transform.scale(img, (img.get_width() // 2, img.get_height() // 2))
                       for img_set in imgs
                       for img in img_set]
        return scaled_imgs

    def big_jump(self):
        pass

    def small_jump(self):
        pass

    def duck(self):
        pass

    def collide(self):
        pass

    def draw(self, screen, ground):
        if self.run:
            i, j = 0, 1
        elif self.duck:
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
        screen.blit(self.img, (100, screen.get_height() - ground.height - self.img.get_height() + 15))
