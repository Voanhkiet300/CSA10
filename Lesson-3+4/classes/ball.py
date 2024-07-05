import pygame


class Ball:
    def __init__(self, img_url, speed_x, speed_y) -> None:
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.img_url = pygame.image.load(img_url)

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

    # set image
    def setImgUrl(self, img_url):
        self.img_url = img_url

    # get image
    def getImgUrl(self):
        return self.img_url

    def move(self, paddle_1_x, paddle_1_y, paddle_1_distance, paddle_2_x, paddle_2_y, paddle_2_distance):
        self.x += self.speed_x
        self.y += self.speed_y

        # kiem tra cham paddle
        if self.x <= (paddle_1_x + paddle_1_distance) and paddle_1_y <= self.y <= (
            paddle_1_y + 120
        ):
            self.speed_x *= -1
        
        if self.x <= (paddle_2_x + paddle_2_distance) and paddle_2_y <= self.y <= (
            paddle_2_y + 120
        ):
            self.speed_x *= -1

        # kiem tra cham edge
        if self.x <= 0 or self.x >= 570:
            self.speed_x = -self.speed_x
        if self.y <= 0 or self.y >= 570:
            self.speed_y = -self.speed_y