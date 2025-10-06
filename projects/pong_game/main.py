from turtle import Turtle, Screen
from paddle import Paddle
import time

# Globals
RIGHT_PADDLE_XY = (350, 0)
LEFT_PADDLE_XY = (-350, 0)

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



# Inputs / Keybinds
screen.onkey(right_paddle.upwards,"Up")
screen.onkey(right_paddle.downwards,"Down")

screen.onkey(left_paddle.upwards,"w")
screen.onkey(left_paddle.downwards,"s")



# Main game loop
games_is_on = True

while games_is_on:
    screen.update()






screen.exitonclick()