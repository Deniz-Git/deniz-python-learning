import turtle
from turtle import Turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "/home/deniz/deniz-python-learning/projects/us_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer_turtle = Turtle()
writer_turtle.penup()
writer_turtle.hideturtle()

def write_state(nameofthestate,x,y):
    """writer turtle writes the state name on x,y cordinate"""
    writer_turtle.goto(x,y)
    writer_turtle.write(f"{nameofthestate}", align=ALIGNMENT, font=FONT)

states_df = pandas.read_csv("50_states.csv")


list_of_states = states_df["state"].tolist()
correct_guesses = []


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title= f"{len(correct_guesses)}/50 States Correct", prompt= "What's another state's name?").title()
    print(states_df[states_df["state"] == answer_state]["x"])

    if answer_state == "Exit":
        place_holder_all_states = list_of_states
        missing = [state for state in place_holder_all_states if state not in correct_guesses]

        df = pandas.DataFrame(missing)
        df.to_csv('states_to_learn.csv')

        break

    if answer_state in list_of_states:
        correct_guesses.append(answer_state)
        goto_x = int(states_df[states_df["state"] == answer_state]["x"])
        goto_y = int(states_df[states_df["state"] == answer_state]["y"])
        write_state(answer_state,goto_x,goto_y)
        print("awesome")
