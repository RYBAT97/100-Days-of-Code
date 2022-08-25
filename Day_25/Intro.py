# The usual way to import data from a file. We're not going to use it.
with open("weather_data.csv", mode='r') as file:
    temp = file.readlines()
    data = []
    for item in temp:
        data.append(item.rstrip())

import csv

# Now we use the csv reader to read a comma-separated file.
with open("weather_data.csv", mode='r') as file:
    csv_data = csv.reader(file)
    next(csv_data, None)  # To skip the header titles
    temperatures = []
    for row in csv_data:
        temperatures.append(int(row[1]))

import pandas

# We can do the same thing much easier with pands!
pandas_data = pandas.read_csv("weather_data.csv")
pandas_temperatures = pandas_data['temp'].to_list()

summation = 0
for item in pandas_temperatures:
    summation += int(item)

average = summation / len(pandas_temperatures)

# Or...
print(pandas_data['temp'].mean())

# To find the max temperature:
print(pandas_data['temp'].max())

# Extract the row that has max temperature
print(pandas_data[pandas_data['temp'] == pandas_data['temp'].max()])


# Convert Monday's temperature to Fahrenheit
def f(x):
    x = x * 1.8 + 32
    return float(x)


print(pandas_data[pandas_data['day'] == 'Monday']['temp'].apply(f))

# To create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

my_dataframe = pandas.DataFrame(data_dict)
my_dataframe.to_csv("new_data.csv")

# Counting squirrels
squirrels_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Black = 0
Cinnamon = 0
Gray = 0

squirrels_colors_data = squirrels_data['Primary Fur Color']

for color in squirrels_colors_data:
    if color == 'Black':
        Black += 1
    elif color == 'Gray':
        Gray += 1
    elif color == 'Cinnamon':
        Cinnamon += 1

my_squirrel_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [Black, Cinnamon, Gray]
}

my_squirrel_dataframe = pandas.DataFrame(my_squirrel_dict)
my_squirrel_dataframe.to_csv("squirrel_count.csv")
