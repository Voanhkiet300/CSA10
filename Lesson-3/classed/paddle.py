import pygame

class Paddle:

    def __init__(self, img_url) -> None:
        self.img = pygame.image.load(img_url)
        
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
        
    # set key press
    def set_key_up(self, key_up):
        self.key_up = key_up
    def set_key_down(self, key_down):
        self.key_down = key_down

    # get key press
    def get_key_up(self):
        return self.key_up
    def get_key_down(self):
        return self.key_down
    
    # move
    def move(self, key_pressed):
        match key_pressed:
            case self.key_up:
                if self.y >= 0:
                    self.y -= 5
            case self.key_down:
                if self.y <= 480:
                    self.y += 5