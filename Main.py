from SnakeObject import SnakeObject
import pygame

# Initialize
pygame.init()
window = pygame.display.set_mode((501, 501))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
snake = SnakeObject(200, 200)
run = True

while run:
    window.fill((46, 46, 46))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    inputs = pygame.key.get_pressed()

    if inputs[pygame.K_UP]:
        if not snake.direction == "S":
            snake.direction = "N"
    if inputs[pygame.K_DOWN]:
        if not snake.direction == "N":
            snake.direction = "S"
    if inputs[pygame.K_LEFT]:
        if not snake.direction == "E":
            snake.direction = "W"
    if inputs[pygame.K_RIGHT]:
        if not snake.direction == "W":
            snake.direction = "E"

    for i in range(0, 520, 20):
        pygame.draw.line(window, (255, 255, 255), (i, 0), (i, 500))
        pygame.draw.line(window, (255, 255, 255), (500, 0), (500, 500))
        pygame.draw.line(window, (255, 255, 255), (0, i), (500, i))

    snake.tempo += 1
    snake.move()
    snake.draw(window)
    pygame.display.update()
    clock.tick(60)

pygame.quit()




