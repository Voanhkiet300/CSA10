import pygame as py
import time
import random

# khai bao cua so tro choi
py.init()
py.display.set_caption('Ping Ponggggg')
size = (600, 600)
canvas = py.display.set_mode(size)
bg_color = (186, 194, 227)
clock = py.time.Clock()


# chen tai nguyen
ball_img = py.image.load('Lesson-13/assets/ball.png')
paddle_img = py.image.load('Lesson-13/assets/paddle.png')


# setup toa do
paddle_1_x = 0
paddle_1_y = 250
paddle_2_x = 570
paddle_2_y = 250
ball_x = 285
ball_y = 300

# setup bien danh cho nut bam
w_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False

# speed
paddle_speed = 5
speed_x = 3
speed_y = 2.5
speed_x = float(random.choice([f'-{speed_x}', f'{speed_x}']))
speed_y = float(random.choice([f'-{speed_y}', f'{speed_y}']))
if speed_x < 0:
    move_left = True
else:
    move_left = False

count = 0
loop = True
while loop: # play game
    count += 1
    events = py.event.get() # bat su kien
    for e in events:
        # quit
        if e.type == py.QUIT:
            loop = False
        # keyboard check
        elif e.type == py. KEYDOWN:
            if e.key == py.K_w:
                w_pressed = True
            elif e.key == py.K_s:
                s_pressed = True
            elif e.key == py.K_UP:
                up_pressed = True
            elif e.key == py.K_DOWN:
                down_pressed = True


        elif e.type == py.KEYUP:
            if e.key == py.K_w:
                w_pressed = False
            elif e.key == py.K_s:
                s_pressed = False
            elif e.key == py.K_UP:
                up_pressed = False
            elif e.key == py.K_DOWN:
                down_pressed = False
    # ball move
    if count >= 50:
        ball_x += speed_x
        ball_y += speed_y
    if count >= 150:
        count = 50
        if move_left:
            speed_x -= 0.1
            paddle_speed += 0.2
        else:
            speed_x += 0.1
    # check collision with paddles and edges
    # >< paddles
    if ball_x <= (paddle_1_x + 30) and paddle_1_y <= ball_y <= (paddle_1_y + 120):
        move_left = False
        speed_x = -speed_x
    if ball_x >= (paddle_2_x - 23) and paddle_2_y <= ball_y <= (paddle_2_y + 120):
        move_left = True
        speed_x = -speed_x
    
    # >< edges
    if ball_x <= 0 or ball_x >= 577:
        speed_x = 0
        speed_y = 0
    if ball_y <= 0 or ball_y >= 577:
        speed_y = -speed_y

    # paddle >< edges
    if paddle_1_y <= 0:
        w_pressed = False
    if paddle_2_y <= 0:
        up_pressed = False
    if paddle_1_y >= 480:
        s_pressed = False
    if paddle_2_y >= 480:
        down_pressed = False

    # paddles move
    if w_pressed:
        paddle_1_y -= paddle_speed
    elif s_pressed:
        paddle_1_y += paddle_speed
    if up_pressed:
        paddle_2_y -= paddle_speed
    elif down_pressed:
        paddle_2_y += paddle_speed

    canvas.fill(bg_color)
    canvas.blit(ball_img, (ball_x, ball_y))
    canvas.blit(paddle_img, (paddle_1_x, paddle_1_y))
    canvas.blit(paddle_img, (paddle_2_x, paddle_2_y))


    clock.tick(60)

    py.display.flip()