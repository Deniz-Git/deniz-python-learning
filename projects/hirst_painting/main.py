import turtle as t
from turtle import Screen
import random
import colorgram


# For files absolute path is required
colors = colorgram.extract('/home/deniz-victus/deniz-python-learning/projects/hirst_painting/image.jpg', 30)


cagri = t.Turtle()
t.colormode(255)
cagri.pensize(20)


cagri.speed("fastest")

# tuple_list_colors = []
#
# for i in range(30):
#
#     pull_rgb = colors[i]
#     rgb = pull_rgb.rgb
#     print(rgb)
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     my_empty_list = (red,green,blue)
#     tuple_list_colors.append(my_empty_list)
#
# print(tuple_list_colors)


color_list = [(155, 80, 50), (21, 29, 67), (194, 153, 134), (37, 104, 164), (246, 219, 69), (121, 165, 192), (157, 67, 100), (171, 155, 161), (24, 50, 128), (65, 24, 40), (67, 30, 16), (118, 189, 151), (119, 31, 53), (223, 85, 51), (20, 88, 37), (196, 82, 118), (126, 32, 15), (58, 126, 50), (56, 125, 209), (16, 64, 36), (10, 86, 106), (253, 216, 0), (175, 167, 54), (210, 181, 188), (73, 174, 111), (226, 177, 166)]

# size 20, pace 50

cagri.pendown()



def draw():
    cagri.pencolor(random.choice(color_list))
    cagri.pendown()
    cagri.forward(1)
    cagri.penup()

def move_fifty():
    cagri.forward(49)

def turn_right_move_turn_right():
    cagri.right(90)
    cagri.forward(50)
    cagri.right(90)
    cagri.forward(50)

def turn_left_move_turn_left():
    cagri.left(90)
    cagri.forward(50)
    cagri.left(90)

a=0

for i in range(10):
    a += 50
    cagri.teleport(x = 0,y=a)
    for x in range(10):
        draw()
        move_fifty()




screen = Screen()
screen.exitonclick()
