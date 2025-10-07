from turtle import Turtle, Screen
from scoreboard import Scoreboard
from car_manager import CarManager
from player import Player
from car_manager import LEVELS
import time

# GLOBALS

CAR_STEP_SPEED = 10
CAR_ANIMATION_SPEED = 10
NUMBER_OF_CARS = 10

# Screen settings
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("Turtle Crossing")
screen.tracer(0)
screen.colormode(255)


# Scoreboard settings
scoreboard = Scoreboard()


# CarManager
car_manager = CarManager()

# Player
player = Player()

# Inputs
screen.listen()
screen.onkey(player.up,"Up")


level = 1



game_over = False
while not game_over:
    screen.update()
    time.sleep(.1)
    car_manager.spawn_cars(animspeed=CAR_ANIMATION_SPEED,number=1,level=level)
    car_manager.move_cars(CAR_STEP_SPEED)
    if player.ycor() > 300:
        level += 1
        car_manager.clearcars()
        car_manager.car_list = []
        scoreboard.level_up(level=level)
        player.goto(x=0,y= -280)
    if car_manager.check_for_collision(player):
        level = 1
        scoreboard.game_over()
        game_over = True

        


screen.exitonclick()
