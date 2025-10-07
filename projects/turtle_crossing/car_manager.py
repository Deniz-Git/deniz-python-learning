
            

    




from turtle import Turtle
import random


color_list = [
    (155, 80, 50), (21, 29, 67), (194, 153, 134), (37, 104, 164), (246, 219, 69),
    (121, 165, 192), (157, 67, 100), (171, 155, 161), (24, 50, 128), (65, 24, 40),
    (67, 30, 16), (118, 189, 151), (119, 31, 53), (223, 85, 51), (20, 88, 37),
    (196, 82, 118), (126, 32, 15), (58, 126, 50), (56, 125, 209), (16, 64, 36),
    (10, 86, 106), (253, 216, 0), (175, 167, 54), (210, 181, 188), (73, 174, 111),
    (226, 177, 166)
    ]


class CarManager():

    def __init__(self):
        self.car_list = []


    
    #TODO SPAWN CAR RANDOMIZE THEIR POSITION FIXED X BUT RANDOM Y BETWEEN 290 - 290
    #TODO CAR SPECS HERE 
    def car(self,speed,difficulty):
        random_y = random.choice(range(-270,300))
        random_x = random.choice(range(300, difficulty)) 
        new_car = Turtle("square")
        new_car.speed(speed)
        new_car.color(random.choice(color_list))
        new_car.penup()
        # new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(random_x,random_y) #spawn
        self.car_list.append(new_car)

    def spawn_cars(self,speed,number,difficulty):
        for i in range(number):
            self.car(speed,difficulty)
    
    def move_cars(self,speed):
        for car in self.car_list:
            car.backward(speed)

    