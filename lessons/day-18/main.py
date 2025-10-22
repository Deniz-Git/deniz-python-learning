# made a turtle craw polygons, automated color change, enter a rang of corners you want and it draws
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("DarkOrchid4")




def draw_and_turn(angle,divisor,side):
    for i in range(divisor):
        tim.forward(100)
        if side == "right":
            tim.right(angle)
        elif side == "left":
            tim.left(angle)

def dashed_10_paces():
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_a_polygon(a_start, a_end, side):
    corner_angles = []
    corner_divisor = []
    for i in range(a_start,a_end):
        angle_degree = int(360/i)
        corner_angles.append(angle_degree)
        corner_divisor.append(int(i))

    for _ in range(len(corner_angles)):
        tim.color(random.choice(colours))
        draw_and_turn(corner_angles[_],corner_divisor[_],side)

draw_a_polygon(3,100,"left")


















screen = Screen()
screen.exitonclick()
