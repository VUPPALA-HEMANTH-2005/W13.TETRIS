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

