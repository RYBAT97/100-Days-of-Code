# fruits = ["Apple", "Orange", "Pear"]
# for fruit in fruits:
#     print(fruit + " Pie")

# -----------------------------------------------

# student_heights = input("Input a list of student heights (Separated by a space):\n").split(sep=" ")
# sum = 0
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     sum += student_heights[n]
# print("Average height is: " + str(round(sum/len(student_heights))))

# -----------------------------------------------

# student_scores = input("Input a list of student score (Separated by space): ").split(sep=" ")
# max = 0
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
#     if student_scores[n] > max:
#         max = student_scores[n]
#
# print(f"Highest score is: {max}")

# -----------------------------------------------

# sum = 0
# for i in range(0, 101):
#     if i % 2 == 0:
#         sum += i
#
# print(f"Sum of Even numbers from 1 to 100 is: {sum}")

# -----------------------------------------------

for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# -----------------------------------------------


