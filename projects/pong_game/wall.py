from turtle import Turtle
#

class Wall(Turtle):
    def __init__(self,xposypos):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(xposypos)
        self.shapesize(1, 40)
        self.shapetransform()
