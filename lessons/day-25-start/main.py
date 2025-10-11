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

data = pandas.read_csv("weather_data.csv")

data_dict = data.to_dict()

temp_list = data["temp"].to_list()


def calculate_average():
    sum_of_list = 0

    for i in temp_list:
        sum_of_list += i


    average = sum_of_list / len(temp_list)
    print(average)

calculate_average()


average = sum(temp_list) / len(temp_list)
print(average)
