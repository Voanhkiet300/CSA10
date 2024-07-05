import pygame
class Paddle:
    def __init__(self, img_url) -> None:
        self.img = pygame.image.load(img_url)

    # set location
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    # get location
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, direction, bound_top, bound_down):
        # neu con trong man choi thi choi tiep
        if  bound_top <= self.y <= bound_down:
            self.y += direction * 5
        elif self.y < bound_top:
            self.y = bound_top + 1
        elif self.y > bound_down:
            self.y = bound_down - 1