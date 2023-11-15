
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             new_temperature = int(row[1])
#             temperatures.append(new_temperature)
#     print(temperatures)

import pandas as pd

data = pd.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# print(data.to_dict())

# average_temp = data["temp"].mean()
# print(average_temp)

# max_temp = data["temp"].max()
# min_temp = data["temp"].min()

# print(max_temp)
# print(min_temp)

# Getting data in a row
# print(data[data["day"] == "Monday"])

# Using Keys for accessing to columns
# print(data[data["temp"] == data["temp"].max()])

# Using dot notation to access to columns
# print(data[data.temp == data.temp.max()])


monday = data[data["day"] == "Monday"]
# print(monday.condition)
# print(monday.temp)


def fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9 / 5) + 32
    return temp_fahrenheit


print(fahrenheit(monday.temp))

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

my_data = pd.DataFrame(data_dict)
print(my_data)
my_data.to_csv("new_data.csv")
