# random walk and random color picker rgb

import turtle as t
from turtle import Screen
import random

{
# go forward, go backward, turnleftgo,turnright go

# def go_forward():
#     cagri.forward(20)

# def go_backwards():
#     cagri.right(180)
#     cagri.forward(20)

# def go_left():
#     cagri.left(90)
#     cagri.forward(20)

# def go_right():
#     cagri.right(90)
#     cagri.forward(20)

# possible_options = [go_forward,go_backwards,go_left,go_right]

# for i in range(100):
#     cagri.color(random.choice(colours))
#     random.choice(possible_options)()
}

# TODO make it faster
# TODO make it thicker 
# TODO make it change colours


cagri = t.Turtle()
t.colormode(255) 

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    x = (r, g, b)
    return x


cagri.shape("turtle")
cagri.speed(0)
cagri.pensize(15)


directions = [0, 90, 180, 270]

for _ in range(1000):
    cagri.pencolor(random_color())
    cagri.setheading(random.choice(directions))
    cagri.forward(30)







screen = Screen()
screen.exitonclick()
