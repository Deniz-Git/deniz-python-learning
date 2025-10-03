import turtle as t
from turtle import Screen
import random
import colorgram

colors = colorgram.extract('image.jpg', 30)

cagri = t.Turtle()
t.colormode(255)
cagri.speed("fastest")

color_list = [(155, 80, 50), (21, 29, 67), (194, 153, 134), (37, 104, 164), (246, 219, 69), (121, 165, 192), (157, 67, 100), (171, 155, 161), (24, 50, 128), (65, 24, 40), (67, 30, 16), (118, 189, 151), (119, 31, 53), (223, 85, 51), (20, 88, 37), (196, 82, 118), (126, 32, 15), (58, 126, 50), (56, 125, 209), (16, 64, 36), (10, 86, 106), (253, 216, 0), (175, 167, 54), (210, 181, 188), (73, 174, 111), (226, 177, 166)]

cagri.hideturtle()


cagri.penup()

a=-200




for i in range(10):
    a += 50
    cagri.teleport(x = -200,y=a)
    for x in range(10):
        cagri.dot(20,random.choice(color_list))
        cagri.forward(50)



screen = Screen()
screen.exitonclick()
