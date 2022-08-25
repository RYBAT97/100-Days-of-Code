art = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""


def calculate(num1, num2, op):
    more = 'n'
    result = 0
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            result = "Cannot divide by Zero!"
            print(result)
            more = input("Start a new calculation? (Y/n): ")
            if more.lower() == 'y':
                more = 'n'
            else:
                print("Thank you for using Python Calculator. Bye!")
                exit()
        else:
            result = num1 / num2
    return more, result


print(art)

reset = True
first_number = 0
next_number = 0
operation = '+'

while True:
    if reset:
        first_number = float(input("What is the 1st number?: "))
        operation = input("Pick an operation (from +, -, *, /): ")
        next_number = float(input("What is the next number?: "))

    to_continue, calc_result = calculate(first_number, next_number, operation)

    print(f"{first_number} {operation} {next_number} = {calc_result}")
    if to_continue == 'n':
        continue
    else:
        to_continue = input(f"Type 'y' to continue calculating with {calc_result}, or type 'n' to start a new "
                            f"calculation. Type 'exit' to end the program: ")
    if to_continue.lower() == "y":
        reset = False
        first_number = calc_result
        operation = input("Pick an operation (from +, -, *, /): ")
        next_number = int(input("What is the next number?: "))
    elif to_continue.lower() == 'n':
        reset = True
    else:
        print("Thank you for using Python Calculator. Bye!")
        exit()
