import pygame


class Treat:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 40
        self.h = 40

    def draw(self, window):
        pygame.draw.rect(window, (0, 255, 0), [self.x, self.y, self.w, self.h])

    def __eq__(self, other):
        if other.x == self.x and other.y == self.y:
            return True
        return False

