from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,pos_data):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(pos_data)
    
    def upwards(self):
        """Moves the paddle on y-axis"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def downwards(self):
        """Moves the paddle on x-axis"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    







