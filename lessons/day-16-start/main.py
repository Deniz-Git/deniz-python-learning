# Class and Object
# Class is the blueprint
# Details of what to be created
# With class we can generate as many objects as we want
# Object is what we are going to use 

#code example:
# car = CarBlueprint() 
# car is the object
# gets created by class CarBlueprint()

# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable() #notice the pascal casing


# poke name and type field names

# table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])

print(table)

table.align = "l"

print(table)