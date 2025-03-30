import pygame  # , sys
from pygame.locals import QUIT

pygame.init()

# INITIALS
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT)) # creates window to play in
pygame.display.set_caption("PING PONG GAME") # names window
run = True

#colors
BLUE = (0,0,255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius #Puts ball in the center
ball_vel_x, ball_vel_y = 1, 1

#paddle dimensions
paddle_width, paddle_height = 20, 150
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2) 
right_paddle_vel = left_paddle_vel = 0

#Main loop
while run:
    wn.fill(BLACK) #erases the balls previous positions so it doesn't trail (no blue line)
    for i in pygame.event.get(): #stores the events of the user (which buttons they click, etc.)
        if i.type == pygame.QUIT: #allows user to exit out of game
            run = False
        elif i.type == pygame.KEYDOWN: #checks any keys are pressed
            if i.key == pygame.K_UP:
                right_paddle_vel = -1.2 #subtracts y-coordinate so paddle moves up
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 1.2 #paddle moves down
            if i.key == pygame.K_w:
                left_paddle_vel = -1.2 
            if i.key == pygame.K_s:
                left_paddle_vel = 1.2 

        if i.type == pygame.KEYUP: #when key is released, paddle stops moving
            right_paddle_vel = 0
            left_paddle_vel = 0

    #ball's movement controls
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius: #checking to see if ball touches top or bottom of game window
        ball_vel_y *= -1 #reverses direction when hits either top or bottom
    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_y *= -1
        ball_vel_y *= -1
    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x, ball_vel_y = 0.7, 0.7
    
    #paddle's movement controls
    if left_paddle_y >= HEIGHT - paddle_height:  #Keeps paddle from going off screen
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    #paddle collisions
    #left paddle
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= -1
    
    #right paddle
    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= -1

    #movements
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel

    

    #OBJECTS
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update()

    pygame.display.update()        

    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius) #wn stands for window       
    
    