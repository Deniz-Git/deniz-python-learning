from turtle import Turtle, Screen
from scoreboard import Scoreboard
from car_manager import CarManager
import time

# GLOBALS

CAR_STEP_SPEED = 10
CAR_ANIMATION_SPEED = 10
NUMBER_OF_CARS = 10
DIFFICULTY = 8000 # 1000-2000-3000-4000-5000... HARDER TO EASIER


# Screen settings
screen = Screen()
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.colormode(255)

# TODO DO NOT FORGET TRRACER AND SCREEN UPDATE


# Scoreboard settings
scoreboard = Scoreboard()


# CarManager
car_manager = CarManager()


game_over = False
while not game_over:
    screen.update()
    time.sleep(.1)
    car_manager.move_cars(CAR_STEP_SPEED)
    
    car_manager.spawn_cars(speed=CAR_ANIMATION_SPEED,number=1,difficulty=DIFFICULTY)



screen.exitonclick()
