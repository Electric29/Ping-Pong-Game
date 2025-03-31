import pygame  # , sys
from pygame.locals import QUIT
import random
#from random import choice, randint, uniform
#from effects import Particle, ExplodingParticle, FloatingParticle

pygame.init()

# INITIALS
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT)) # creates window to play in
pygame.display.set_caption("PING PONG GAME") # names window
run = True
player_1 = player_2 = 0
direction = [0, 1]
angle = [0, 1, 2]
clock = pygame.time.Clock()
particle_group = pygame.sprite.Group()

floating_particle_timer = pygame.event.custom_type()
pygame.time.set_timer(floating_particle_timer, 10)

#colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

#for the ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius #Puts ball in the center
ball_vel_x, ball_vel_y = 0.7, 0.7

#paddle dimensions
paddle_width, paddle_height = 20, 150
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2) 
right_paddle_vel = left_paddle_vel = 0

'''
End effects
def spawn_particles(n: int):
    for _ in range(n):
        pos = pygame.mouse.get_pos()
        color = choice(("red", "green", "blue"))
        direction = pygame.math.Vector2(uniform(-1, 1), uniform(-1, 1))
        direction = direction.normalize()
        speed = randint(50, 400)
        Particle(particle_group, pos, color, direction, speed)


def spawn_exploding_particles(n: int):
    for _ in range(n):
        pos = pygame.mouse.get_pos()
        color = choice(("red", "yellow", "orange"))
        direction = pygame.math.Vector2(uniform(-0.2, 0.2), uniform(-1, 0))
        direction = direction.normalize()
        speed = randint(50, 400)
        ExplodingParticle(particle_group, pos, color, direction, speed)


def spawn_floating_particle():
    init_pos = pygame.mouse.get_pos()
    pos = init_pos[0] + randint(-10, 10), init_pos[1] + randint(-10, 10)
    color = "white"
    direction = pygame.math.Vector2(0, -1)
    speed = randint(50, 100)
    FloatingParticle(particle_group, pos, color, direction, speed)

'''

#Main loop
while run:
    dt = clock.tick() / 1000
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
        player_1 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
        
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4

        ball_vel_x *= -1

    if ball_x <= 0 + radius:
        player_2 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_vel_x, ball_vel_y = 0.7, 0.7
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if ang == 0:
                ball_vel_y, ball_vel_x = -1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = -0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = -0.7, 1.4
        
        if dir == 1:
            if ang == 0:
                ball_vel_y, ball_vel_x = 1.4, 0.7
            if ang == 1:
                ball_vel_y, ball_vel_x = 0.7, 0.7
            if ang == 2:
                ball_vel_y, ball_vel_x = 0.7, 1.4
    
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

    #Scoreboard
    font = pygame.font.SysFont("laila", 32)
    score_1 = font.render("Player_1:  " + str(player_1), True, WHITE)
    wn.blit(score_1, (25, 25))
    score_2 = font.render("Player_2:  " + str(player_2), True, WHITE)
    wn.blit(score_2, (825, 25))

    #OBJECTS
    pygame.draw.circle(wn, BLUE, (ball_x, ball_y), radius) #wn stands for window 
    pygame.draw.rect(wn, RED, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, RED, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    #Endscreen
    winning_font = pygame.font.SysFont("laila", 100)
    if player_1 >= 5:
        wn.fill(BLACK)
        endscreen = winning_font.render("PLAYER_1 WON!!!", True, YELLOW)
        wn.blit(endscreen, (200, 250))
        #spawn_exploding_particles(3)

    
    if player_2 >= 5:
        wn.fill(BLACK)
        endscreen = winning_font.render("PLAYER_2 WON!!!", True, YELLOW)
        wn.blit(endscreen, (200, 250))
        #spawn_exploding_particles(3)


    pygame.display.update()        
    
'''
Resources used:

https://www.youtube.com/watch?v=tS8F7_X2qB0

https://www.pygame.org/docs/tut/newbieguide.html

https://www.youtube.com/watch?v=ZiPWN39mGM0

'''
