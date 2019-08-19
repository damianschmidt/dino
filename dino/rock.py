import pygame
from random import randint


class Rock:
    def __init__(self, ground_height, width):
        self.ground_height = ground_height
        self.width = width
        self.x = self.width
        self.y = randint(3, 30)
        self.size = randint(1, 10)

    def move(self, velocity):
        self.x -= velocity
        if self.x + self.size < 0:
            self.x = self.width

    def draw(self, screen):
        pygame.draw.line(screen, (0, 0, 0), (self.x, screen.get_height() - self.ground_height + self.y),
                         (self.x + self.size, screen.get_height() - self.ground_height + self.y), 2)
