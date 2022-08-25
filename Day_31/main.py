import random

import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
data_dictionary = {}
current_card = {}


def open_data_file():
    global data_dictionary
    try:
        data = pandas.read_csv("data/words_to_learn.csv")
    except (FileNotFoundError, ValueError):
        data = pandas.read_csv("data/french_words.csv")
        data.to_csv("data/words_to_learn.csv", index=False)
    finally:
        data_dictionary = data.to_dict(orient="records")


def show_english_card():
    global current_card
    canvas.itemconfig(my_canvas, image=flashcard_back_photo)
    canvas.itemconfig(canvas_1st_line, text="English", fill='white')
    canvas.itemconfig(canvas_2nd_line, text=current_card["English"], fill='white')


def update_canvas():
    global current_card, flip_timer
    canvas.itemconfig(my_canvas, image=flashcard_front_photo)
    canvas.itemconfig(canvas_1st_line, text="French", fill='black')
    canvas.itemconfig(canvas_2nd_line, text=current_card["French"], fill='black')
    flip_timer = window.after(3000, func=show_english_card)


def initiate():
    global current_card
    current_card = random.choice(data_dictionary)
    update_canvas()


def right_button_pressed():
    global current_card, flip_timer, data_dictionary
    window.after_cancel(flip_timer)
    data_dictionary.remove(current_card)
    pandas.DataFrame.from_dict(data_dictionary).to_csv("data/words_to_learn.csv", index=False)
    try:
        current_card = random.choice(data_dictionary)
    except IndexError:
        open_data_file()
        current_card = random.choice(data_dictionary)
    update_canvas()


def wrong_button_pressed():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(data_dictionary)
    except IndexError:
        open_data_file()
        current_card = random.choice(data_dictionary)
    update_canvas()


open_data_file()
window = Tk()
window.title("Flashcard App 1.0")
window.config(padx=40, pady=40, background=BACKGROUND_COLOR)
flip_timer = window.after(0)
canvas = Canvas(width=800, height=600, highlightthickness=0, background=BACKGROUND_COLOR)
flashcard_front_photo = PhotoImage(file="images/card_front.png")
flashcard_back_photo = PhotoImage(file="images/card_back.png")
my_canvas = canvas.create_image(400, 300, image=flashcard_front_photo)
canvas_1st_line = canvas.create_text(400, 175, text="French", font=("Century Gothic", 32, 'italic'))
canvas_2nd_line = canvas.create_text(400, 300, text="French", font=("Century Gothic", 32, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)
wr_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wr_image, highlightthickness=0, command=wrong_button_pressed)
wrong_button.grid(row=1, column=0)
rt_image = PhotoImage(file="images/right.png")
right_button = Button(image=rt_image, highlightthickness=0, command=right_button_pressed)
right_button.grid(row=1, column=1)

initiate()

window.mainloop()
