from turtle import Turtle


class Ball(Turtle):
    def __init__(self,pos_data):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(pos_data)
    
    def move(self,speedx,speedy):
        new_x = self.xcor() + speedx
        new_y = self.ycor() + speedy
        self.goto(new_x, new_y)

    # def change_direction(self,speed):
    #     new_x = self.xcor() + (speed * -1)
    #     new_y = self.ycor() + (speed * -1)
    #     self.goto(new_x, new_y)

