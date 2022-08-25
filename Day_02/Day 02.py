# user_input = input("Enter a 2 digit number: ")
# print(int(user_input[0]) + int(user_input[1]))

# --------------------------------------------

# height = input("Enter your height in M: ")
# weight = input("Enter your weight in KG: ")
#
# BMI = float(weight)/(float(height)**2)
#
# print("Your BMI is: " + str(int(BMI)))

# --------------------------------------------

age = input("What is your current age?\n")
years_left = 90 - int(age)
months_left = int(years_left * 12)
weeks_left = int((years_left * 365) / 7)
days_left = years_left * 365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
