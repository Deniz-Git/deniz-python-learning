#imports
from turtle import Screen, Turtle
from snake import Snake
import time




# Scren setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snek")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# The game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    snake.getheadingreading()

    





# game_over = False
# while not game_over:
#     if snake eats food:
#         create another turtle
    


















screen.exitonclick()