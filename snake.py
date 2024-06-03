import pygame
import random

# initialize pygame and create window
screen_w = 600
screen_h = 400
pygame.init()
screen = pygame.display.set_mode((screen_w, screen_h))

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# define snake block size
block_size = 20

screen.fill(white)
# initialize snake
snake = [(screen_w//block_size//2 *block_size, screen_h//block_size//2*block_size),
            (screen_w//block_size//2 *block_size + block_size, screen_h//block_size//2*block_size)]

# initialize food
food = (random.randint(0, screen_w // block_size-1) * block_size,
        random.randint(0, screen_h // block_size-1) * block_size)
while(food in snake):
    food = (random.randint(0, screen_w // block_size-1) * block_size,
        random.randint(0, screen_h // block_size-1) * block_size)

# initialize score
score = 0

# initialize game speed
speed = 20

# initialize game over flag
game_over = False

# initialize direction of snake
direction = 'right'

# game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # change snake direction 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 'left'
            if event.key == pygame.K_RIGHT:
                direction = 'right'
            if event.key == pygame.K_DOWN:
                direction = 'down'
            if event.key == pygame.K_UP:
                direction = 'up'
    
    # move snake
    head = snake[-1]
    x, y = head
    tail = snake.pop(0) # remove tail
    new_head = None
    if direction == 'left':
        new_head = (x - block_size, y)
    elif  direction == 'right':
        new_head = (x + block_size, y)
    elif direction == 'down':
        new_head = (x, y + block_size)
    else:
        new_head = (x, y - block_size)
    snake.append(new_head) # add new head

    # check for collision with food
    if snake[-1] == food:
        food = (random.randint(0, screen_w // block_size-1) * block_size,
                random.randint(0, screen_h // block_size-1) * block_size)
        while(food in snake):
            food = (random.randint(0, screen_w // block_size-1) * block_size,
                random.randint(0, screen_h // block_size-1) * block_size)
        snake.insert(0,tail)
        score += 1
        speed += 20

    # check for collision with walls
    if snake[-1][0] >= screen_w or snake[-1][0] < 0 or snake[-1][1] >= screen_h or snake[-1][1] < 0:
        running = False

    # check for collision with snake body
    if snake[-1] in snake[:-1]:
        running = False

    # fill screen with white
    screen.fill(white)

    # draw snake
    for x, y in snake:
        pygame.draw.rect(screen, black, (x, y, block_size, block_size))

    # draw food
    pygame.draw.rect(screen, red, (food[0], food[1], block_size, block_size))

    # display score
    font = pygame.font.Font(None, 30)
    score_text = font.render("Score: " + str(score), 1, black)
    screen.blit(score_text, (screen_w-150, 10))

    # update display
    pygame.display.update()

    # wait
    pygame.time.wait(200 - speed)

    # game over message
    if not running:
        font = pygame.font.Font(None, 50)
        game_over_text = font.render("Game Over", 1, black)
        screen.blit(game_over_text, (screen_w//2-50, screen_h//2))
        pygame.display.update()
        pygame.time.wait(5000)

pygame.quit()




