import pygame
import random

# initialize pygame and create window
screen_w = 400
screen_h = 600
pygame.init()
screen = pygame.display.set_mode((screen_w, screen_h))

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 255, 255)

# define character block size
block_size = 20

# initialize character position
character_x = screen_w // 2
character_y = 0
v_y = 0
v_x = 0

# initialize stairs
stairs = []
for i in range(5):
    stair_x = random.randint(0, screen_w - block_size)
    stair_y = random.randint(0, screen_h - block_size)
    stair = [stair_x, stair_y]
    stairs.append(stair)

# initialize score
score = 0

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                v_x = -2
            elif event.key == pygame.K_RIGHT:
                v_x = 2
            else:
                v_x = 0
        else:
            v_x = 0

    # move character
    v_y += 0.1
    character_y += int(v_y)
    character_x += v_x

    # move stair
    for i in range(len(stairs)):
        stairs[i][1] -= 2+score//20
        if stairs[i][1]+block_size < 0 :
            # remove stair
            stairs.pop(i)
            # add new stair
            stair_x = random.randint(0, screen_w - block_size)
            stair_y = random.randint(screen_h, screen_h + screen_h//3)
            stair = [stair_x, stair_y]
            stairs.append(stair)
            score += 1

    # check for collision with stairs
    for stair in stairs:
        if stair[0] <= character_x+block_size and stair[0]+5*block_size >= character_x \
            and stair[1] <= character_y+block_size and stair[1] >= character_y:
            character_y = stair[1]-block_size
            v_y = 0

    # check for collision with walls
    if character_y >= screen_h:
        character_y = 0
        v_y = 0
        #running = False
        score = 0
    if character_y < 0:
        character_y = 0
        v_y = 0
        #running = False
        score = 0
    if character_x < 0:
        character_x = 0
    if character_x > screen_w - block_size:
        character_x = screen_w - block_size

    # fill screen with white
    screen.fill(white)

    # draw character
    pygame.draw.rect(screen, blue, (character_x, character_y, block_size, block_size))
    
    # draw stairs
    for stair in stairs:
        pygame.draw.rect(screen, black, (stair[0], stair[1], 5*block_size, block_size))
    
    # display score
    font = pygame.font.Font(None, 30)
    score_text = font.render("Score: " + str(score), 1, black)
    screen.blit(score_text, (screen_w-150, 10))

    # update display
    pygame.display.flip()
    pygame.time.wait(10)
# close window
pygame.quit()