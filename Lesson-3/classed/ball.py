import pygame

class Ball:
    def __init__(self, img_url, speed_x, speed_y) -> None:
        self.img = pygame.image.load(img_url)
        self.speed_x = speed_x
        self.speed_y = speed_y

    # set location
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y

    # get location
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    
    def move(self, paddle_x, paddle_y, paddle_distance):
        self.x += self.speed_x
        self.y += self.speed_y

        # check paddle
        if self.x <= (paddle_x + paddle_distance) and (paddle_x + paddle_distance) <= self.y <= (paddle_y + 120):
            self.speed_x *= -1

        # check edge
        if self.x <= 0 or self.x >= 570:
            self.speed_x = -self.speed_x
        if self.y <= 0 or self.y >= 570:
            self.speed_y = -self.speed_y
