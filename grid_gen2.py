import string
import random

#Creating 15x15 grid with '-' as the placeholders
width = 10
height = 10
grid = [['-' for i in range(0, width)] for j in range(0, height)]

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

            if grid[x_coordinate][y_coordinate] == '-' or grid[x_coordinate][y_coordinate] == word[i]:
                grid[x_coordinate][y_coordinate] = word[i]
                m += 1
            else:
                break
        
        if (m==len(word)):
            print(word,"==",[x+1, y+1])
            k += 1

def main():
    # To get words from a file
    # file = open(r"words.txt", "r")
    # sentence = file.read()
    # file.close()
    # word_list = sentence.split()

    word_list = ["HELLO","FIRE","NOOB","PLANETS","EARTH","MARS","VENUS"]
    word_list.sort()

    for i in range(0, len(word_list)):
        x = word_list[i]
        word_list[i] = random.choice([x, x[::-1]])      #To choose between normal and reverse string

    generator(word_list)

    for i in range(0, width):
        for j in range(0,height):
            if grid[i][j] == '-':
                grid[i][j] = random.choice(string.ascii_uppercase)      #Filing the empty spots with characters

    print("\n".join(map(lambda row: " ". join(row), grid)))
    #print("],\n[".join(map(lambda row: '","'. join(row), grid)))

main()    
