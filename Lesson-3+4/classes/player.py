import pygame
from classes.ball import Ball
from classes.paddle import Paddle


class Player:
    def __init__(self) -> None:
        self.key_up_1 = False
        self.key_down_1 = False
        self.key_up_2 = False
        self.key_down_2 = False

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

    # set key press
    def setKeyUp1(self, key_up_1):
        self.key_up_1 = key_up_1

    def setKeyDown1(self, key_down_1):
        self.key_down_1 = key_down_1

    def setKeyUp2(self, key_up_2):
        self.key_up_2 = key_up_2

    def setKeyDown2(self, key_down_2):
        self.key_down_2 = key_down_2

    # get key press
    def getKeyUp1(self):
        return self.key_up_1

    def getKeyDown1(self):
        return self.key_down_1

    def getKeyUp2(self):
        return self.key_up_2

    def getKeyDown2(self):
        return self.key_down_2