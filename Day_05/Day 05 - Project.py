import random
import string

print("Welcome to the PyPassword Generator!")
total_length = int(input("How many letters would you like in your password?\n"))
symbol_length = int(input("How many symbols would you like?\n"))
numbers_length = int(input("How many numbers would you like?\n"))

lowercase_letters_list = list(string.ascii_lowercase)
uppercase_letters_list = list(string.ascii_uppercase)
letters_list = lowercase_letters_list + uppercase_letters_list
numbers_list = list(string.digits)
symbols_list = list(string.punctuation)

password = []

for i in range(0, symbol_length):
    password += random.choice(symbols_list)
for j in range(0, numbers_length):
    password += random.choice(numbers_list)
for k in range(0, (total_length - (symbol_length + numbers_length))):
    password += random.choice(letters_list)

random.shuffle(password)
password = ''.join(password)

print(password)
