# made a turtle craw polygons, automated color change, enter a rang of corners you want and it draws
from turtle import Turtle, Screen
import turtle
import random

tim = Turtle()
tim.shape("turtle")
tim.color("DarkOrchid4")
tim.speed(0)
turtle.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    x = (r, g, b)
    return x

# def make_a_circle(radius, speed):
#     quotient = 360/radius
#     tim.color(random_color())

#     for i in range(radius):
#         tim.forward(speed)
#         tim.right(quotient)


# for i in range(100):
#     make_a_circle(70,10)
#     tim.setheading(i*4)

tim.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


draw_spirograph(5)






screen = Screen()
screen.exitonclick()