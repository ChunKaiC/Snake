from SnakeObject import SnakeObject
from Button import Button
from Treat import Treat
import pygame
import random


class SnakeGame:
    def __init__(self):
        """Initialize"""
        pygame.init()
        self.board = [(j, i) for j in range(0, 600, 40) for i in range(0, 600, 40)]
        self.snake = SnakeObject(320, 320)
        self.treat = self.spawn_treat()
        self.window = pygame.display.set_mode((601, 601))
        pygame.display.set_caption("Snake")
        self.font = pygame.font.SysFont("Corbel", 35)
        self.clock = pygame.time.Clock()
        self.run = True

    def spawn_treat(self):
        """Spawns a treat on the board"""
        pos_board = []
        for space in self.board:
            flag = True
            for segment in self.snake.body:
                if space[0] == segment.x and space[1] == segment.y:
                    flag = False
                    break
            if flag:
                pos_board.append(space)
        choice = random.choice(pos_board)
        return Treat(choice[0], choice[1])

    def draw_grid(self, window):
        """Draws Grid"""
        for i in range(0, 620, 40):
            pygame.draw.line(window, (255, 255, 255), (i, 0), (i, 600))
            pygame.draw.line(window, (255, 255, 255), (600, 0), (600, 600))
            pygame.draw.line(window, (255, 255, 255), (0, i), (600, i))

    def check_collision(self):
        """Checks collision with treat, self, and border"""
        # Collision with treat
        if self.treat == self.snake.body[0]:
            self.snake.increase += 6
            self.treat = self.spawn_treat()

        # Collision with self
        head = self.snake.body[0]
        for segment in self.snake.body[1:]:
            if segment == head:
                self.run = False

        # Collision with Border
        if 560 < head.x or head.x < 0 or 560 < head.y or head.y < 0:
            self.run = False

    def play(self):
        """Plays the game"""
        while self.run:
            self.window.fill((46, 46, 46))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            inputs = pygame.key.get_pressed()

            if inputs[pygame.K_UP]:
                if not self.snake.direction == "S":
                    self.snake.direction = "N"
            if inputs[pygame.K_DOWN]:
                if not self.snake.direction == "N":
                    self.snake.direction = "S"
            if inputs[pygame.K_LEFT]:
                if not self.snake.direction == "E":
                    self.snake.direction = "W"
            if inputs[pygame.K_RIGHT]:
                if not self.snake.direction == "W":
                    self.snake.direction = "E"

            self.draw_grid(self.window)
            self.snake.tempo += 1
            self.snake.move()
            self.treat.draw(self.window)
            self.snake.draw(self.window)
            self.snake.grow()
            self.check_collision()
            pygame.display.update()
            self.clock.tick(60)
        self.end()

    def end(self):
        replay = False
        self.window.fill((46, 46, 46))
        play_button = Button(200, 350, 200, 50, (255, 255, 255), self.font, "PLAY AGAIN")
        quit_button = Button(200, 450, 200, 50, (255, 255, 255), self.font, "QUIT")

        while not replay:

            mouse_pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] == 1:
                if play_button.hover(mouse_pos):
                    self.board = [(j, i) for j in range(0, 600, 40) for i in range(0, 600, 40)]
                    self.snake = SnakeObject(320, 320)
                    self.treat = self.spawn_treat()
                    self.run = True
                    replay = True

                if quit_button.hover(mouse_pos):
                    pygame.quit()

            play_button.display(self.window)
            play_button.hover(mouse_pos)
            quit_button.display(self.window)
            quit_button.hover(mouse_pos)

            pygame.display.update()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    replay = True
                    pygame.quit()

        self.play()


if __name__ == "__main__":
    game = SnakeGame()
    game.play()
