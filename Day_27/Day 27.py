import tkinter

window = tkinter.Tk()

window.title("My 1st GUI program")
window.minsize(width=400, height=300)

# Label
my_label = tkinter.Label(text="I am a label.", font=("Century Gothic", 24, "bold"))
my_label.pack()
my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    my_label.config(text=my_input.get())


my_button = tkinter.Button(text="Click Me", command=button_clicked)
my_button.pack()

# Entry
my_input = tkinter.Entry(width=10)
my_input.insert(tkinter.END, string="Some text to begin with")
my_input.pack()

# Textbox
my_textbox = tkinter.Text(height=5, width=30)
my_textbox.focus()
my_textbox.insert(tkinter.END, "Example of multi-line text entry.")
my_textbox.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()


def checkbutton_used():
    print(checked_state.get())


checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


def radio_used():
    print(radio_state.get())


radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
