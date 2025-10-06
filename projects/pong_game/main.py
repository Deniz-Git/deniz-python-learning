from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from scoreboard import Scoreboard
import time
import random



# Globals

    # Padels
RIGHT_PADDLE_XY = (350, 0)
LEFT_PADDLE_XY = (-350, 0)

    # Ball
BALL_START_POS = (0, 0)
BALL_SPEED_X= -20
BALL_SPEED_Y= -20

    # Wall
UPPER_WALL = (0,300)
LOWER_WALL = (0,-300)




# Screen 
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
screen.listen()

# Creation of paddles
right_paddle = Paddle(RIGHT_PADDLE_XY)
left_paddle = Paddle(LEFT_PADDLE_XY)

# Creation of ball
ball = Ball(BALL_START_POS)

#Creation of wall
upper_wall = Wall(UPPER_WALL)
lower_wall = Wall(LOWER_WALL)


# Scoreboard
left_scoreboard = Scoreboard()
left_scoreboard.goto(-280,250)
left_scoreboard.show_score()

right_scoreboard = Scoreboard()
right_scoreboard.goto(280,250)
right_scoreboard.show_score()

# Inputs / Keybinds
screen.onkey(right_paddle.upwards,"Up")
screen.onkey(right_paddle.downwards,"Down")

screen.onkey(left_paddle.upwards,"w")
screen.onkey(left_paddle.downwards,"s")

# screen.onkey(ball.reset, "c")
  
# screen.onkey(ball.change_direction(BALL_SPEED),"Space")

 

# Main game loop
games_is_on = True

while games_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move(BALL_SPEED_X,BALL_SPEED_Y)

    # Check wall collision
    if ball.ycor() > 270 or ball.ycor() < -270:
        BALL_SPEED_Y *= -1

    # Detect collision with paddle
    if ball.distance(right_paddle) < 40 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        BALL_SPEED_X *= -1.2


    # Left side scores
    if ball.xcor() > 390 and ball.distance(right_paddle) > 40:
        left_scoreboard.nomnom()
        ball.teleport(0,0,)
        BALL_SPEED_X *= -1


    # Right side scores
    if ball.xcor() < -390 and ball.distance(left_paddle) > 40:
        right_scoreboard.nomnom()
        ball.teleport(0,0,)
        BALL_SPEED_X *= -1




screen.exitonclick()