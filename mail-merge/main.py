# with open("Input/Letters/starting_letter.txt") as file:
#     letter = file.read()
#
# with open("Input/Names/invited_names.txt") as file:
#     names = file.readlines()
#
# for name in names:
#     with open(f"Output/ReadyToSend/letter_for_{name.strip()}", mode="w") as file:
#         file.write(letter.replace("[name]", name.strip()))
# import csv
#
# temperatures = []
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for index, row in enumerate(data):
#         if index != 0:
#             temperatures.append(int(row[1]))
#
# print(temperatures)
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# color = data["Primary Fur Color"]
# color.groupby(color).count().to_frame(name="Count").to_csv("squirrel_count.csv")



