import pygame
import random

pygame.init()

# Screen size
WIDTH = 600
HEIGHT = 400

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
HEAD_GREEN = (0, 200, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Snake settings
BLOCK_SIZE = 20
SPEED = 3

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Live Snake Game")

# Clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, 35)


def draw_snake(block_size, snake_list):

    for i, block in enumerate(snake_list):

        x = block[0]
        y = block[1]

        # Snake head
        if i == len(snake_list) - 1:

            pygame.draw.rect(
                screen,
                HEAD_GREEN,
                [x, y, block_size, block_size],
                border_radius=5
            )

            # Eyes
            pygame.draw.circle(screen, WHITE, (int(x + 5), int(y + 6)), 2)
            pygame.draw.circle(screen, WHITE, (int(x + 15), int(y + 6)), 2)

            pygame.draw.circle(screen, BLACK, (int(x + 5), int(y + 6)), 1)
            pygame.draw.circle(screen, BLACK, (int(x + 15), int(y + 6)), 1)

        # Snake body
        else:

            pygame.draw.rect(
                screen,
                GREEN,
                [x, y, block_size, block_size],
                border_radius=4
            )


def game_loop():

    game_over = False
    game_close = False

    # Snake starting position
    x = WIDTH / 2
    y = HEIGHT / 2

    # Snake movement
    x_change = BLOCK_SIZE
    y_change = 0

    # Snake body
    snake_list = []
    snake_length = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0

    while not game_over:

        while game_close:

            screen.fill(BLACK)

            text = font.render(
                "Game Over! Press C to Play Again or Q to Quit",
                True,
                RED
            )

            screen.blit(text, [20, HEIGHT / 2])

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -BLOCK_SIZE
                    y_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = BLOCK_SIZE
                    y_change = 0

                elif event.key == pygame.K_UP:
                    y_change = -BLOCK_SIZE
                    x_change = 0

                elif event.key == pygame.K_DOWN:
                    y_change = BLOCK_SIZE
                    x_change = 0

        # Hit wall
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        # Move snake
        x += x_change
        y += y_change

        # Background
        screen.fill(BLACK)

        # Draw food
        pygame.draw.circle(
            screen,
            RED,
            (int(food_x + 10), int(food_y + 10)),
            10
        )

        # Snake head
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)

        snake_list.append(snake_head)

        # Remove extra blocks
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Snake hits itself
        for block in snake_list[:-1]:

            if block == snake_head:
                game_close = True

        # Draw snake
        draw_snake(BLOCK_SIZE, snake_list)

        # Score
        score = font.render(
            "Score: " + str(snake_length - 1),
            True,
            WHITE
        )

        screen.blit(score, [10, 10])

        pygame.display.update()

        # Eat food
        if x == food_x and y == food_y:

            food_x = round(
                random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0
            ) * 20.0

            food_y = round(
                random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0
            ) * 20.0

            snake_length += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()


game_loop()