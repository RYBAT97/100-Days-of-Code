import pandas
import random

# Console exercises [List]
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
name = "Angela"
new_list = [letter for letter in name]
my_range = range(1, 5)
range_list = [item * 2 for item in my_range]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]

# Interactive coding 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)

# Interactive coding 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]
print(result)

# Interactive coding 3
with open("file1.txt") as file1:
    file1_data = file1.readlines()
    file1_data = [int(item.rstrip()) for item in file1_data]
with open("file2.txt") as file2:
    file2_data = file2.readlines()
    file2_data = [int(item.rstrip()) for item in file2_data]

mutual_items = [item for item in file1_data if item in file2_data]
print(mutual_items)

# Console exercises {Dictionary}
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
student_scores = {name: random.randint(1, 100) for name in names}
passed_students = {key: value for (key, value) in student_scores.items() if value > 60}

# Interactive coding 4
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_dict = {statement: len(statement) for statement in sentence.split()}
print(words_dict)

# Interactive coding 5
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}
weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

# Iterate through Pandas Dataframe
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
for (index, row) in student_data_frame.iterrows():
    print(row.student)
