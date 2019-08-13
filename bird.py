class Bird:
    def __init__(self, type_of_bird, screen_width):
        self.width = 60
        self.height = 50
        self.x_position = screen_width
        self.type_of_bird = type_of_bird

        self.y_position = self.set_y()
        self.flap_count = 0

    def set_y(self):
        if self.type_of_bird == 'high':
            return 180
        elif self.type_of_bird == 'mid':
            return 100
        else:
            return 10 + self.height/2

    def move(self):
        pass

    def collide(self):
        pass

    def draw(self):
        pass
