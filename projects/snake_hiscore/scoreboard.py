from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.read_data()
        self.update_scoreboard()

    def read_data(self):
        with open("data.txt",mode="r") as file:
            place_holder = file.read()
            self.high_score = int(place_holder)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def write_data(self):
        with open ("data.txt", mode="w") as file:
            place_holder2 = int(self.high_score)
            file.write(f"{place_holder2}")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_data()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
