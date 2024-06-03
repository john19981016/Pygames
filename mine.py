import pygame
import random

# Initialize the game
pygame.init()
width, height = 500, 500
screen = pygame.display.set_mode((width, height))

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
gray = (150, 150, 150)

# Define the size of the map and the number of mines
map_width, map_height = 10, 10
mine_num = 10

# Create the map array, 0 represents no mine, 1 represents a mine
map_array = [[0 for y in range(map_height)] for x in range(map_width)]

# 0 represents not opened, 1 represents opened
map_visited = [[0 for y in range(map_height)] for x in range(map_width)]

# Initialize the mine count array, -1 represents a mine
map_num = [[0 for y in range(map_height)] for x in range(map_width)]

def ResetMap(map_array, map_visited, map_num, mine_num):
    # Reset the map
    for x in range(map_width): 
        for y in range(map_height):
            map_array[x][y]=0
            map_visited[x][y]=0
            map_num[x][y]=0

    # Calculate the number of mines around each location
    for i in range(mine_num):
        x, y = random.randint(0, map_width-1), random.randint(0, map_height-1)
        while map_array[x][y] == 1:
            x, y = random.randint(0, map_width-1), random.randint(0, map_height-1)
        map_array[x][y] = 1

    # Calculate the number of mines around each location
    for x in range(map_width): 
        for y in range(map_height):
            if map_array[x][y]==1:
                map_num[x][y]=-1
            else:
                for i in range(x-1,x+2):
                    for j in range(y-1,y+2):
                        if i < map_width and i >= 0 and j < map_height and j >= 0:
                            map_num[x][y] += map_array[i][j]


# Main game loop
ResetMap(map_array, map_visited, map_num, mine_num)
running = True
gameover = False
success = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x = pos[0] // 50
            y = pos[1] // 50
            if map_array[x][y] == 1:
                gameover = True
            else:
                map_visited[x][y] = 1
    
    # Check all position are visited except mines
    success = True
    for x in range(map_width): 
        for y in range(map_height):
            if map_visited[x][y]+map_array[x][y]!=1:
                success = False
                break
        if not success:
            break

    # Draw the map
    screen.fill(gray)
    for x in range(map_width): 
        for y in range(map_height):
            if map_visited[x][y] == 1 or success or gameover:
                if map_array[x][y] == 1:
                    if success:
                        pygame.draw.rect(screen, green, (x*50+1, y*50+1, 50-2, 50-2))
                    else:
                        pygame.draw.rect(screen, red, (x*50+1, y*50+1, 50-2, 50-2))
                else:
                    pygame.draw.rect(screen, white, (x*50+1, y*50+1, 50-2, 50-2))
                    font = pygame.font.Font(None, 50)
                    score_text = font.render(str(map_num[x][y]), 1, black)
                    screen.blit(score_text, (x*50+10, y*50+10))
            else:
                pygame.draw.rect(screen, white, (x*50+1, y*50+1, 50-2, 50-2))
    # Update the screen
    pygame.display.update()
    if gameover or success:
        pygame.time.wait(3000)
        ResetMap(map_array, map_visited, map_num, mine_num)
        gameover = False
        success = False

pygame.quit()
