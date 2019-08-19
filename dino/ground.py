import pygame
from dino.rock import Rock


class Ground:
    def __init__(self, width):
        self.width = width
        self.height = 100
        self.rocks = self.create_rocks()
        self.velocity = 10

    def create_rocks(self):
        return [Rock(self.height, self.width + i * 100) for i in range(8)]

    def move(self):
        [rock.move(self.velocity) for rock in self.rocks]

    def draw(self, screen):
        [rock.draw(screen) for rock in self.rocks]
        pygame.draw.line(screen, (0, 0, 0), (0, screen.get_height() - self.height),
                         (self.width, screen.get_height() - self.height), 2)
