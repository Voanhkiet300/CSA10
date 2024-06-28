import pygame
from classed.ball import Ball
from classed.paddle import Paddle



class Player:
    def __init__(self,title, size_x, size_y):
        self.title = title
        self.size_x = size_x
        self.size_y = size_y
        # create canvas
        pygame.init()
        pygame.display.set_caption(title)
        self.canvas = pygame.display.set_mode(size=(size_x, size_y))
        self.clock = pygame.time.Clock()


    def run(self):
        ball = Ball("Lesson-3/assets/ball.png")
        paddle1 = Ball("Lesson-3/assets/paddle.png")
        paddle2 = Ball("Lesson-3/assets/paddle.png")

        # setup location
        ball.set_x(285)
        ball.set_y(300)

        paddle1.set_x(0)
        paddle1.set_y(250)

        paddle2.set_x(570)
        paddle2.set_y(250)

        # setup key press
        paddle1.set_key_up("w")
        paddle1.set_key_down("s")
        paddle2.set_key_up("Up")
        paddle2.set_key_down("Down")