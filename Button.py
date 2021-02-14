import pygame


class Button:
    def __init__(self, x, y, w, h, color, font, text):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text = font.render(text, 1, (0, 0, 0))

    def hover(self, pos):
        if self.x <= pos[0] <= self.x + self.w and self.y <= pos[1] <= self.y + self.h:
            self.color = (200, 200, 200)
            return True
        self.color = (255, 255, 255)
        return False

    def display(self, window):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.w, self.h])
        window.blit(self.text, (self.x + (self.w/2 - self.text.get_width()//2),
                                self.y + (self.h/2 - self.text.get_height()//2)))



