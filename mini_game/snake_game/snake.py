import curses
from random import randint

WINDOW_WIDTH = 40  # number of columns of window box
WINDOW_HEIGHT = 15 # number of rows of window box 

# set up window 
curses.initscr()
win = curses.newwin(WINDOW_HEIGHT, WINDOW_WIDTH, 0, 0) # careful means the y cord is coming first then x - most apllication other way round
win.keypad(1) # able to use arrow keys
curses.noecho() # use echo so doesn't listen to any other input characters and echo to our terminal
curses.curs_set(0) # hide curses
win.border(0) # set border
win.nodelay(1) # true - means not waiting for next user input - instead continuing then using -1 if dont get another event loop can continue

# snake and food 
snake = [(4, 4), (4, 3), (4, 2)] # use a list to keep track - inside store coordinates - use Tuple because its immutable which is good want to keep coord 
food = (6, 6) # has initail coord - use Tuple 

win.addch(food[0], food[1], '#') # add first food right away

# game logic
score = 0 # keep track of score - will increase everytime hit the food '#'
high_score = 0

# need to say it should run as long as the user hits the escape key = defined as 27 in cursor model 
ESC = 27
key = curses.KEY_RIGHT # Start by moving snake to the right

while key != ESC: # while the key isnt ESC we continue. 'TRUE' runs endlessly because its True always have the box layout in terminal
    # add some information 
    win.addstr(0, 2, ' Score ' + str(score) + ' ') # (line, coloum, str)
    # increase speed of snake when it gets bigger / based on the snake
    win.timeout(150 - (len(snake)) // 5 + len(snake) //10 % 120) # increase speed
    
    # want to get the next key - ^ its right arrow key
    prev_key = key
    event = win.getch() # waiting for next user input = get next character 
    key = event if event != -1 else prev_key
    
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]: # if not in these keys we use the previous key 
        key = prev_key
        
        # want to calculate the next coord for the snake - by getting the coord for the head of the snake
    y = snake[0][0] # double 0 - because getting index of the Tuple ^^ first Tuple = head
    x = snake[0][1] # tail
    # check the keys must be one of those keys
    if key == curses.KEY_DOWN:
        y += 1 # increase coord y to move down 
    if key == curses.KEY_UP:
        y -= 1 # want to go up have to decrease our y so its minus
    if key == curses.KEY_LEFT:
        x -= 1 # decrease coord X to move LEFT
    if key == curses.KEY_RIGHT:
        x += 1 # increase coord X to move right
        
    # Now have new coord we want to insert them into our snake
    snake.insert(0, (y, x)) # assign new a head 
    
    # want to check if we hit the border 
    if y == 0: break
    if y == WINDOW_HEIGHT-1: break # 20 max width ^ 
    if x == 0 : break
    if x == WINDOW_WIDTH -1: break 
    
    # if snake runs over itself 
    # check if head is alreayd in our list / [1:] called list slicing so checks all coords from 1 till end 
    if snake[0] in snake[1:]: break
    
    # check if hit the food
    if snake[0] == food: # if same position as coord of food want to eat the food
        # eat food so increase score  
        score += 10
        
        if score > high_score:
            high_score = score
        
        food = () # draw a new food equal empty tuple 
        while food == (): #  get new food 
            food = (randint(1, WINDOW_HEIGHT-2), randint(1, WINDOW_WIDTH -2))
            if food in snake:
                food = () # while true loop continues
        win.addch(food[0], food[1], '#') # if at position of the food we add a new character onto the chain otherwise --- 
    else:
        # move snake - remove last coord of the tail 
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
    
    
     
    
    # for c in snake:
        # win.addch(c[0], c[1], '*') # use for to log to terminal - so for every coordinate want to add character to Y  
    
    win.addch(snake[0][0], snake[0][1], '*')
    
    
curses.endwin() # call curses - which destroys window again
print(f"GAME OVER! Final score = {score} High Score = {high_score}")