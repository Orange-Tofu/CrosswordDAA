import pygame
import string
import random

# --------------------------------word_grid FUNCTION--------------------------------------------
#Creating 15x15 word_grid with '-' as the placeholders
width = 10
height = 10
word_grid = [['-' for i in range(0, width)] for j in range(0, height)]

def generator(word_list):
    
    k=0    #Number of completed iterations
    while(k<len(word_list)):
        m = 0       #flag bit to keep track of number of characters placed
        word = word_list[k]

        d = random.choice([[1, 0], [0, 1], [1, 1]])     #To choose between horizontal, vertical and diagonal placement
        xsize = width if d[0] == 0 else width - len(word)
        ysize = height if d[1] == 0 else height - len(word)
        x = random.randrange(0, xsize)
        y = random.randrange(0, ysize)

        for i in range(0, len(word)):
            x_coordinate = y + d[1]*i
            y_coordinate = x + d[0]*i

            if word_grid[x_coordinate][y_coordinate] == '-' or word_grid[x_coordinate][y_coordinate] == word[i]:
                word_grid[x_coordinate][y_coordinate] = word[i]
                m += 1
            else:
                break
        
        if (m==len(word)):
            #print(word,"==",[x+1, y+1])
            k += 1

def get_grid():
    # To get words from a file
    # file = open(r"words.txt", "r")
    # sentence = file.read()
    # word_list = sentence.split()

    word_list = ["HELLO","FIRE","NOOB","PLANETS","EARTH","MARS","VENUS"]
    word_list.sort()

    for i in range(0, len(word_list)):
        x = word_list[i]
        word_list[i] = random.choice([x, x[::-1]])      #To choose between normal and reverse string

    generator(word_list)

    for i in range(0, width):
        for j in range(0,height):
            if word_grid[i][j] == '-':
                word_grid[i][j] = random.choice(string.ascii_uppercase)      #Filing the empty spots with characters
    
    return word_grid    

    #print("\n".join(map(lambda row: " ". join(row), word_grid)))
    #print("],\n[".join(map(lambda row: '","'. join(row), word_grid)))

#---------------------------word_grid PART END-----------------------------------------------------------

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each game_grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
game_grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    game_grid.append([])
    for column in range(10):
        game_grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#game_grid[1][5] = 1

game_grid2 = get_grid()

# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed game_grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to game_grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            game_grid[row][column] = 1
            print("Click ", pos, "game_grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the game_grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if game_grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

            font = pygame.font.SysFont(None, 24)
            img = font.render(game_grid2[row][column], True, BLACK)
            screen.blit(img, ((MARGIN + WIDTH) * column + MARGIN + 4, (MARGIN + HEIGHT) * row + MARGIN + 4)) 
    
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()