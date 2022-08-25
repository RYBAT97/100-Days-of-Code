print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")
num = input("How many people to split the bill? ")

share = float(total_bill) * (1 + int(tip_percent)/100) / int(num)
print("Each person should pay: $" + "{:.2f}".format(share))
