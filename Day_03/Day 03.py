# num = float(input("Enter a number: "))
# if num % 2 == 0:
#     stat = "Even"
# else:
#     stat = "Odd"
# print(f"You've entered an {stat} number.")

# -----------------------------------------------

# print("Welcome to the Ticket Shop!")
# height = float(input("Please Enter your height (in centimeters): "))
# age = int(input("Now, please enter your age: "))
#
# if height >= 120:
#     print("You can ride the roller coaster :)")
#     if age < 12:
#         print("Please pay $5.")
#     elif (age >= 12) and (age < 18):
#         print("Please pay $7.")
#     else:
#         print("Please pay $12.")
# else:
#     print("Sorry, you cannot ride the roller coaster :(")

# -----------------------------------------------

# print("Welcome to BMI Calculator 2.0!")
# weight = int(input("Please Enter your weight in KG: "))
# height = float(input("Now, please Enter your height in M: "))
#
# BMI = weight / (height**2)
#
# if BMI < 18.5:
#     print(f"Your BMI is {round(BMI)}, you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {round(BMI)}, you have a normal weight.")
# elif BMI < 30:
#     print(f"Your BMI is {round(BMI)}, you are overweight.")
# elif BMI < 35:
#     print(f"Your BMI is {round(BMI)}, you are obese.")
# else:
#     print(f"Your BMI is {round(BMI)}, you are clinically obese.")

# -----------------------------------------------

# year = int(input("Enter a year: "))
#
# if year % 4 != 0:
#     print("Not a Leap Year :(")
# else:
#     if year % 100 != 0:
#         print("Leap Year! :)")
#     elif year % 100 == 0 and year % 400 == 0:
#         print("Leap Year! :)")
#     else:
#         print("Not a Leap Year :(")

# -----------------------------------------------

# print("Welcome to the Ticket Shop!")
# height = float(input("Please Enter your height (in centimeters): "))
#
# if height < 120:
#     print("Sorry, you cannot ride the roller coaster :(")
#     exit(0)
#
# age = int(input("Now, please enter your age: "))
# photo = input("Would you like to have a picture? (Y/n): ")
# bill = 0
#
# print("You can ride the roller coaster :)")
# if age < 12:
#     bill += 5
# elif (age >= 12) and (age < 18):
#     bill += 7
# else:
#     bill += 12
#
# if photo == "Y":
#     bill += 3
#
# print(f"Please pay ${bill}.")

# -----------------------------------------------

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S, M, or L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
#
# bill = 0
#
# if size == "S":
#     bill += 15
# if size == "M":
#     bill += 20
# if size == "L":
#     bill += 25
#
# if add_pepperoni == "Y" and size == "S":
#     bill += 2
# if add_pepperoni == "Y" and (size == "M" or size == "L"):
#     bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is ${bill}.")

# -----------------------------------------------

print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is his/her name?\n")

T = name1.lower().count("t") + name2.lower().count("t")
R = name1.lower().count("r") + name2.lower().count("r")
U = name1.lower().count("u") + name2.lower().count("u")
E = name1.lower().count("e") + name2.lower().count("e")
L = name1.lower().count("l") + name2.lower().count("l")
O = name1.lower().count("o") + name2.lower().count("o")
V = name1.lower().count("v") + name2.lower().count("v")

TRUE = T + R + U + E
LOVE = L + O + V + E

score = int(str(TRUE) + str(LOVE))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40 < score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

