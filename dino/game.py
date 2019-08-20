import pygame
from random import randint
from math import floor

from dino.dino import Dino
from dino.ground import Ground
from dino.cactus import Cactus
from dino.bird import Bird

pygame.init()
pygame.display.set_caption('Dino')
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.score = 0
        self.run = False

    def move(self, dinos, ground, obstacles):
        [dino.move() for dino in dinos]
        for obstacle in obstacles:
            if obstacle.x < self.screen_width and not obstacle.next_added:
                obstacle.next_added = True
                random = randint(0, 3)
                obstacles.append(Cactus(self.screen_width + randint(500, 1000))) if random == 3 \
                    else obstacles.append(Bird(self.screen_width + randint(500, 1000)))
        [obstacle.move() for obstacle in obstacles]
        [obstacles.remove(obstacle) for obstacle in obstacles if obstacle.x + obstacle.img.get_width() < 0]
        ground.move()

    def draw_score(self):
        pygame.font.init()
        font = pygame.font.SysFont('Comic-Sans', 20)
        score_surface = font.render(f'Score: {floor(self.score)}', True, (0, 0, 0))
        self.screen.blit(score_surface, (10, 10))

    def draw_screen(self, dinos, ground, obstacles):
        self.screen.fill((255, 255, 255))

        ground.draw(self.screen)
        [obstacle.draw(self.screen, ground) for obstacle in obstacles]
        [dino.draw(self.screen, ground) for dino in dinos]

        self.draw_score()

        clock.tick(30)
        pygame.display.update()

    def collide(self, dinos, obstacles):
        for dino in dinos:
            for obstacle in obstacles:
                if obstacle.collide(dino):
                    self.run = False

    def restart(self):
        self.score = 0
        self.run = True
        return [Dino()], Ground(self.screen_width), [Cactus(self.screen_width)]

    def game_loop(self):
        dinos = [Dino()]
        ground = Ground(self.screen_width)
        obstacles = [Cactus(self.screen_width)]
        self.run = True
        space_down_timer = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    dinos, ground, obstacles = self.restart()

            while self.run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        if dinos[0].y_change == 0:
                            dinos[0].gravity = 2
                            dinos[0].y_velocity = 22
                            space_down_timer = 0
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                        if dinos[0].y_change != 0:
                            dinos[0].gravity = 5
                        dinos[0].duck = True
                        dinos[0].run = False
                    elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                        if space_down_timer < 15:
                            dinos[0].gravity = 3
                    elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                        dinos[0].duck = False
                        dinos[0].run = True

                space_down_timer += 1
                self.move(dinos, ground, obstacles)
                self.draw_screen(dinos, ground, obstacles)
                self.collide(dinos, obstacles)
                self.score += 0.3
