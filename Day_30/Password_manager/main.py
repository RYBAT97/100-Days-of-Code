import json
import os
import string
import random
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    total_length = 16
    symbol_length = 4
    numbers_length = 4

    lowercase_letters_list = list(string.ascii_lowercase)
    uppercase_letters_list = list(string.ascii_uppercase)
    letters_list = lowercase_letters_list + uppercase_letters_list
    numbers_list = list(string.digits)
    symbols_list = list(string.punctuation)

    password = []
    password += random.sample(symbols_list, symbol_length)
    password += random.sample(numbers_list, numbers_length)
    password += random.sample(letters_list, total_length - (symbol_length + numbers_length))

    random.shuffle(password)
    password = ''.join(password)

    # Copy generated password to clipboard
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def search():
    searched_website = website_entry.get()
    searched_email = ""
    searched_password = ""

    if website_entry.get() == "":
        messagebox.showwarning(title="Oops!", message="Website entry is empty!")
        return "searching_for_nothing_error"

    try:
        with open("data.json", mode="r") as my_file:
            data = json.load(my_file)
            if searched_website in data:
                searched_email = data[searched_website]["email"]
                searched_password = data[searched_website]["password"]
            else:
                raise KeyError("No details for the website exists")

    except (FileNotFoundError, ValueError):
        # Note: ValueError exception is added for the times when data.json exists, but it is empty. This
        # prevents JSON decoding error.
        messagebox.showerror(title="Oops!", message="Sorry, the data file is empty or does not exist.")
    except KeyError as error_message:
        messagebox.showerror(title="Oops!", message=error_message)
    else:
        messagebox.showinfo(title=searched_website, message=f"Email: {searched_email}\nPassword: {searched_password}")


def add_to_file():
    if len(email_or_username_entry.get()) == 0 or len(password_entry.get()) == 0 or len(website_entry.get()) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
        return "form_validation_warning"
    else:
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered:\n"
                                                                          f"Email: {email_or_username_entry.get()}\n"
                                                                          f"Password: {password_entry.get()}\n"
                                                                          f"Is it OK to save?")
        if is_ok:
            json_data = {
                website_entry.get(): {
                    "email": email_or_username_entry.get(),
                    "password": password_entry.get()
                }
            }
            try:
                with open("data.json", mode="r") as my_file:
                    data = json.load(my_file)
            except (FileNotFoundError, ValueError):
                # Note: ValueError exception is added for the times when data.json exists, but it is empty. This
                # prevents JSON decoding error.
                with open("data.json", mode="w") as my_file:
                    json.dump(json_data, my_file, indent=4)
            else:
                data.update(json_data)
                with open("data.json", mode="w") as my_file:
                    json.dump(data, my_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PyPass Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_photo)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=22)
website_entry.grid(row=1, column=1)
website_entry.focus()
search_button = Button(text="Search", command=search, width=14)
search_button.grid(row=1, column=2)
email_or_username_label = Label(text="Email/Username:")
email_or_username_label.grid(row=2, column=0)
email_or_username_entry = Entry(width=40)
email_or_username_entry.grid(row=2, column=1, columnspan=2)
email_or_username_entry.insert(0, "my_email@yahoo.com")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", width=33, command=add_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
