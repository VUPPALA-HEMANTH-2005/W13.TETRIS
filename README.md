# W13.TETRIS
Description

Tetris game used to be one of the famous classic single player game in which we manuplate the falling blocks-tetriminoes(geometric shapes made up of four square blocks). Rearranging them from middle-top and freezes them, when it touchs bottom or other blocks.Once a horizontal row is completely filled(every grid of the row is filled with a block irrespective of the type of colour and shape of object) it clears from the board giving a point

Features

Interactive game play: we can play this game with basic arrow keys to operate the functions like rotate and move the tetriminoes.
Scoring: We could earn points by filling the lines.
Leveling: As the game goes on it becomes more challenging as we clear more lines by increasing the falling speed of tetriminoes.
Game Over: When the Tetriminoes fill upto top of the grid(play field) the games ends.

How to Play:

Extract the given file
Insatll python3,Open a terminal and navigate to the extrated file. And run the command('Tetris.py') to access and run the file. 
Left arrow(<-):to move the Tetriminoes one block towards left for each press.
Right arrow(->):to move the Tetriminoes one block towards right for each press.
Down arrow:to move the Tetriminoes one row towards down for each press.
Up arrow: To rotate the Tetriminoes randomly(clockwise or anti-clockwise)
clear as many lines as possible to increase your score.
The game ends when Tetriminoes stackup to the top.

Dependencies:

The Tetris game has folloeing dependencies,
modules like pygame,random,playsound

File Structure:

The repository consists the following file sturctures,
Tetris.py - The main python script that impliments the game
Tetris.png - The image of Tetris logo in the starting page
start.png - The image of start button in the starting page
exit_btn.png - The image of exit button in the starting page
blast.wav - The sound when the line is cleared

Contributions:

Abhinay - Creating the starting page which includes placing the Tetris Logo,Start and exit Buttons,To begin and close respectively. Colours of the Tetriminoes.

Rahul - Genetrating different figures and plasing them creating functions like rotate,all moments(down,left,right). Breaking the lines when it is filled and giving a new tetriminoe every time when the previous one touches it's base,givinng sound when the line breaks.

Hemanth - Initializing the game, defining the background and grid colours, controlling the speed(the rate at it falls) of tetriminoes, implementing conditions for the controlls, creating a grid and defining co-ordinates of the grid,font and size of the text,Ending the game.
