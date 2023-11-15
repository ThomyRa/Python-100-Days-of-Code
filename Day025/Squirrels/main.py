
import pandas as pd

squirrels_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_furs = squirrels_data["Primary Fur Color"]
print(squirrel_furs.value_counts())
