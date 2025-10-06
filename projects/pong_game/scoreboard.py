from turtle import Turtle
FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self,leftorright):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.show_score()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)

    def left_score_up(self):
        self.l_score += 1
        self.show_score_l()

    def right_score_up(self):
        self.r_score += 1
        self.show_score_r()

    def show_score_r(self):
        self.clear()
        self.write(f"{self.r_score}", align="center", font=FONT)
    
    def show_score_l(self):
        self.clear()
        self.write(f"{self.l_score}", align="center", font=FONT)