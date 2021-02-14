from Segment import Segment
import pygame


class SnakeObject:
    def __init__(self, x, y):
        self.body = [Segment(x, y), Segment(x - 40, y), Segment(x - 80, y), Segment(x - 120, y), Segment(x - 160, y),
                     Segment(x - 200, y), Segment(x - 240, y)]
        self.length = 7
        self.tempo = 0
        self.increase = 0
        self.direction = "E"

    def draw(self, window):
        for segment in self.body:
            pygame.draw.rect(window, (255, 0, 0), [segment.x, segment.y, segment.w, segment.h])

    def move(self):
        pre_x = self.body[0].x
        pre_y = self.body[0].y

        if self.tempo == 7:
            if self.direction == "N":
                self.body[0].y -= 40
            elif self.direction == "E":
                self.body[0].x += 40
            elif self.direction == "S":
                self.body[0].y += 40
            else:
                self.body[0].x -= 40

            for segment in self.body[1:]:
                segment.x, pre_x = pre_x, segment.x
                segment.y, pre_y = pre_y, segment.y

            self.tempo = 0
            self.grow()

    def grow(self):
        if self.increase > 0:
            self.body.append(Segment(self.body[-1].x, self.body[-1].y))
            self.length += 1
            self.increase -= 1


if __name__ == "Main":
    pass
