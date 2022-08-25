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
            with open("data.txt", mode="a") as my_file:
                my_data = f"{website_entry.get()} | {email_or_username_entry.get()} | {password_entry.get()}\n"
                my_file.writelines(my_data)
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
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
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
