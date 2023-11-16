from prettyprinter import pprint

weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:
def cels_to_fahr(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f


weather_f = {day: cels_to_fahr(temp_c) for (day, temp_c) in weather_c.items()}
pprint(weather_f)
