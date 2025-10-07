from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.speed(0)
        self.goto(x=0, y=-280)
        self.setheading(90)

    def up(self):
        new_y = self.ycor() + 5
        self.goto(x=self.xcor(), y=new_y)