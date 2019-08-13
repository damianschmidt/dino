class Obstacle:
    def __init__(self, screen_width, type_of_obstacle):
        self.x_position = screen_width
        self.type_of_obstacle = type_of_obstacle
        self.width, self.height = self.set_width_and_height()

    def set_width_and_height(self):
        if self.type_of_obstacle == 'small_cactus':
            return 40, 80
        elif self.type_of_obstacle == 'big_cactus':
            return 60, 120
        else:
            return 120, 80

    def move(self):
        pass

    def collide(self):
        pass

    def draw(self):
        pass
