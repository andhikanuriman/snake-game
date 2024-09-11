import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 1280, 720
BLOCK_SIZE = 20
SPEED = 10

# Set up some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

def game_loop():
    # Set up the snake and food
    snake = [(WIDTH / 2, HEIGHT / 2)]
    food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
            random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
    direction = (1, 0)

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        # Move the snake
        head = snake[0]
        new_head = (head[0] + direction[0] * BLOCK_SIZE,
                    head[1] + direction[1] * BLOCK_SIZE)
        snake.insert(0, new_head)

        # Check for collision with food
        if snake[0] == food:
            food = (random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE,
                    random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE)
        else:
            snake.pop()

        # Check for collision with wall or self
        if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            snake[0] in snake[1:]):
            return True

        # Draw everything
        screen.fill(BLACK)
        for pos in snake:
            pygame.draw.rect(screen, WHITE, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.delay(1000 // SPEED)

def main():
    while True:
        game_over = game_loop()
        if game_over:
            screen.fill(BLACK)
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over! Press 'R' to play again or 'Q' to quit.", True, WHITE)
            screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
            pygame.display.flip()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            main()
                        elif event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()
                pygame.time.delay(1000 // SPEED)

if __name__ == "__main__":
    main()