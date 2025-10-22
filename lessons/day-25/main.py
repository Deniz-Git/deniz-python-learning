# with open ("./weather_data.csv","r") as file:
#     place_holder_list = file.readlines()
#
# data = []
# for i in place_holder_list:
#     data.append(i.strip())
#
# print(data)
#

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)


import pandas

# database = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# def calculate_average():
#     sum_of_list = 0
#
#     for i in temp_list:
#         sum_of_list += i
#
#
#     average = sum_of_list / len(temp_list)
#     print(average)
#
# calculate_average()
#
#
# average = sum(temp_list) / len(temp_list)
# print(average)

# print(data["temp"].mean())
# print(data["temp"].max())

# print(database[database.day == "Monday"])
# print(database[database.temp == database.temp.max()])
#

# monday = database[database.day == "Monday"]
# print(monday)
#
# celcius = monday["temp"]
#
# fahrenheit = (celcius * 1.8) + 32
#
# print(fahrenheit)

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")



blacks = data[data["Primary Fur Color"] == "Black"]
grays = data[data["Primary Fur Color"] == "Gray"]
reds = data[data["Primary Fur Color"] == "Cinnamon"]

blacks_len = len(blacks)
grays_len = len(grays)
reds_len = len(reds)

number_of_colors = {
    "colors": ["blacks", "grays", "reds"],
    "amount": [blacks_len, grays_len, reds_len]
}

squirrel_data = pandas.DataFrame(number_of_colors)
squirrel_data.to_csv("squirrel_colors.csv")
