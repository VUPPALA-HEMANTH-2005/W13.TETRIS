import pygame as pg
import random as rm
from playsound import playsound

#Screen size of the main menu
SCREEN_HEIGTH = 400
SCREEN_WIDTH = 800

screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
pg.display.set_caption('Tetris')

#For printing the images on the main menu
start_img = pg.image.load('start.png').convert_alpha()
exit_img = pg.image.load('exit_btn.png').convert_alpha()
tetris_img = pg.image.load('Tetris.png').convert_alpha()

#Creating a class for pressing the button on the screen
class Button():
# initializing the class
    def __init__(rha,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        rha.image = pg.transform.scale(image,(int(width*scale),int(height*scale)))
        rha.rect = rha.image.get_rect()
        rha.rect.topleft = (x,y)
        rha.click = False

# defining a function for clicking the buttons
    def draw(rha):
        motion = False

        pos = pg.mouse.get_pos()

        if rha.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and rha.click == False:
                rha.click = True
                motion = True
                
        if pg.mouse.get_pressed()[0] == 0:
            rha.click = False
        screen.blit(rha.image,(rha.rect.x,rha.rect.y))

        return motion

# For the pos and size of the image
start_button = Button(100,300,start_img,0.25)
exit_button = Button(450,300,exit_img,0.4)
tetris_button = Button(200,0,tetris_img,0.4)

run = True
while run:

#Background of main page
    screen.fill((0,0,0))
#Creating the start button
    if start_button.draw() == True:
        run = False
        completed = False
#Creating the exit button
    elif exit_button.draw() == True:
        run = False
        completed = True
#Creating the logo
    elif tetris_button.draw() == True:
        print('1')

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    pg.display.update()
# similarly we can add return button and exit button (functions) in the second page 
# which can be used while running the game to return back to initial page and closing the game respectively 
                                                                            #Till here Home page

#The colours of the blocks
colors = [
    (255,0,191),
    (255,128,128),
    (0, 119, 179),
    (45,134,45),
    (0,255,205),
    (204,204,0),
    (179,26,255),
]
#Creating a class for generating different figures
class Figure:

#postion of the top left corner
    p = 0
    q = 0

    different_shapes = [
        [[3,7,11,15], [12,13,14,15]], # staright line
        [[4, 5, 11, 10], [2, 6, 13, 9]], # Different Z shapes
        [[6, 7, 9, 8], [1, 5, 14, 10]],# Different reverse Z shapes
        [[3,2,6,10], [8,12,13,14], [3,7,11,10], [9,10,11,15]],# different L shapes
        [[0,1,5,9], [11,10,9,13], [0,4,8,9], [11,15,14,13]],# different 7 shapes
        [[10,13,14,15], [3,7,6,11], [1,2,3,6], [6,10,11,14]],# different T shapes
        [[10,11,14,15]],# square
        [[4,0,1,2,6],[0,1,5,8,9],[0,4,5,6,2],[1,0,4,8,9]]# differnt U shapes
    ]
# initializing the class
    def __init__(rha, a, b):
        rha.a = a
        rha.b = b
        rha.type = rm.randint(0, len(rha.different_shapes) - 1)
        rha.color = rm.randint(1, len(colors) - 1)
        rha.rotation = 0
# For generating random figures
    def shape(rha):
        return rha.different_shapes[rha.type][rha.rotation]
# For rotating the figures
    def rotate(rha):
        rha.rotation = (rha.rotation + 1) % len(rha.different_shapes[rha.type])

#Creating a class for working of the game
class Tetris_Game:
    speed = 3
    result = 0
    state = "start"
    blocks = []
    length = 0
    breadth = 0
    a = 30 #position of left corner x-coordinate
    b = 30 #position of left corner y-coordinate
    enlarge = 25 #size of unit block
    figure = None
# initializing the class
    def __init__(rha, length, breadth):
        rha.breadth = breadth
        rha.length = length
        rha.blocks = []
        rha.result = 0
        rha.state = "start"
        for i in range(length):
            new_line = []
            for j in range(breadth):
                new_line.append(0)
            rha.blocks.append(new_line)

# defining the function for generating new figures when the previous figure is placed
    def new_figure(rha):
        rha.figure = Figure(11, 0)

#Defining the function for the movement of the figures
    def movement(rha):
        joining = False
        for i in range(0,4):
            for j in range(0,4):
                if i * 4 + j in rha.figure.shape():
                    if i + rha.figure.b> rha.length - 1 or \
                            j + rha.figure.a > rha.breadth - 1 or \
                            j + rha.figure.a < 0 or \
                            rha.blocks[i + rha.figure.b][j + rha.figure.a] > 0:
                        joining = True
        #playsound('step.wav')
        return joining

# Defing a function for breaking of lines when the line is filled
    def break_lines(rha):
        Line = 0
        for i in range(1, rha.length):
            k = 0
            for j in range(rha.breadth): 
                if rha.blocks[i][j] == 0:
                    k += 1

#when line is completely filled it breaks off (the excess blocks are eliminated) and adds ten points
            if k == 0:
                Line += 1
                for l in range(i, 1, -1):
                    for m in range(rha.breadth):
                        rha.blocks[l][m] = rha.blocks[l - 1][m]
                playsound("blast.wav")
        rha.result += Line * 10

# Defining a function for the figure to move down
    def enter_down(rha):
        rha.figure.b += 1
        if rha.movement():
            rha.figure.b -= 1
            rha.freeze()

#For rotating the figure
    def rotate(rha):
        old_rotation = rha.figure.rotation
        rha.figure.rotate()
        if rha.movement():
            rha.figure.rotation = old_rotation

#For moving the block side wise
    def enter_side(rha, da):
        old_a = rha.figure.a
        rha.figure.a += da
        if rha.movement():
            rha.figure.a = old_a

#For the game to end when the figures touched the top line 
    def freeze(rha):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in rha.figure.shape():
                    rha.blocks[i + rha.figure.b][j + rha.figure.a] = rha.figure.color
        rha.break_lines()
        rha.new_figure()
        if rha.movement():
            rha.state = "The End"
                                            #Till Here the game appearance and the conditions of the game
# Initializing the game engine
pg.init()

# Defining background colours
COLOUR_1 = (0, 0, 0)
COLOUR_2 = (255,255,255)
COLOUR_3 = (65,74,156)
#Size of the game screen
size = (700, 800)
pg.display.set_caption("Tetris")
screen = pg.display.set_mode(size)


# Loop until the user clicks the close button.
clock = pg.time.Clock()
fps = 60
game = Tetris_Game(20, 25)
no_of_blocks = 0

pressing_down = False

while not completed:
    
    #The condition for the new block to come
    if game.figure is None:
        game.new_figure()
    no_of_blocks += 1

    #When the result is above 100000 the game resets
    if no_of_blocks > 100000:
        no_of_blocks = 0

    #
    if no_of_blocks % (fps // game.speed // 2) == 0 or pressing_down:
        if game.state == "start":
            game.enter_down()

    for event in pg.event.get():
        #For the game to close when you pressed the cross button
        if event.type == pg.QUIT:
            completed = True
        #KEYDOWN is a function in pygame that enables to use the keyboard keys
        if event.type == pg.KEYDOWN:
            #when we press up arrow the figure rotates
            if event.key == pg.K_UP:
                game.rotate()
            #when we press left arrow the figure moves one block to the left
            if event.key == pg.K_LEFT:
                game.enter_side(-1)
            #when we press down arrow the figure moves one block Down
            if event.key == pg.K_DOWN:
                pressing_down = True
            #when we press right arrow the figure move one block to the right
            if event.key == pg.K_RIGHT:
                game.enter_side(1)
            #when we press Esc button after the game ends the game restarts
            if event.key == pg.K_ESCAPE:
                game.__init__(30, 25)
    #KEYUP is a function for seeing wheather the key is pressed or not
    if event.type == pg.KEYUP:
            if event.key == pg.K_DOWN:
                pressing_down = False
                                    #The controls of the game
    #To fill the game with given colour
    screen.fill(COLOUR_1)

    #for creating the grid of the game
    for i in range(game.length):
        for j in range(game.breadth):
            pg.draw.rect(screen, COLOUR_3, [game.a + game.enlarge * j, game.b + game.enlarge * i, game.enlarge, game.enlarge], 1)
            if game.blocks[i][j] > 0:
                pg.draw.rect(screen, colors[game.blocks[i][j]],
                                 [game.a + game.enlarge * j + 1, game.b + game.enlarge * i + 1, game.enlarge - 2, game.enlarge - 1])

    #for taking the coordinates of the shapes
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.shape():
                    pg.draw.rect(screen, colors[game.figure.color],
                                     [game.a + game.enlarge * (j + game.figure.a) + 1,
                                      game.b + game.enlarge * (i + game.figure.b) + 1,
                                      game.enlarge - 2, game.enlarge - 2])

    #For the font and size of the texts
    font = pg.font.SysFont('Arial', 25, True, False)
    font1 = pg.font.SysFont('Arial', 40, True, False)
    text = font.render("result: " + str(game.result), True, COLOUR_2)

    #For printing "GameOver" when the game ends
    text_game_over = font1.render("Game Finished", True, (215,37,3))
    #For printing "Press Esc to Restart" when the game ends
    text_game_over1 = font1.render("Press Esc to Restart", True, (215, 255, 0))

    #Blit is a function that places the image on the screen
    screen.blit(text, [0, 0])
    #playsound("end.wav")
    if game.state == "The End":
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])
    pg.display.flip()
    clock.tick(fps)
pg.quit()
