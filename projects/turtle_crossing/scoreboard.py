from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 16, "bold"))

    def level_up(self):
        return
