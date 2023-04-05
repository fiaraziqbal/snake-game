import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game screen
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up the snake initial position
snake_block = 10
x1 = 250
y1 = 250

# Set up the snake movement
x1_change = 0       
y1_change = 0

# Set up the food position
foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# Set up the score
score = 0

# Set up the speed
speed = 15

# Set up the clock
clock = pygame.time.Clock()

# Define the function to draw the snake and the food
def snake(snake_block, snake_List):
    for x in snake_List:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    font = pygame.font.SysFont(None, 25)
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [width / 6, height / 3])

# Set up the game loop
game_over = False
snake_List = []
Length_of_snake = 1

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # Check if the snake hits the boundary
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_over = True

    # Update the snake position
    x1 += x1_change
    y1 += y1_change

    # Clear the screen
    screen.fill(white)

    # Draw the food
    pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

    # Update the snake list
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)

    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    # Check if the snake hits itself
    for x in snake_List[:-1]:
        if x == snake_Head:
            game_over = True

    # Draw the snake
    snake(snake_block, snake_List)

    # Update the score
    font_style = pygame.font.SysFont(None, 30)
    value = font_style.render("Your Score: " + str(score), True, black)
    screen.blit(value, [0, 0])

    # Update the display
    pygame.display.update()

    # Check if the snake hits the food
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1
        score += 1
        speed += 1

    # Set up the snake speed
    clock.tick(speed)

# Show the game over screen
font_style = pygame.font.SysFont(None, 50)
game_over_text = font_style.render("Game Over! Your Score Was: " + str(score), True, black)
screen.blit(game_over_text, [width / 6, height / 3])
pygame.display.update()

# Wait for 2 seconds before closing the window
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()
quit()


   
