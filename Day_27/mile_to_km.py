import tkinter

window = tkinter.Tk()

window.title("Mile to Km Convertor")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

user_input = tkinter.Entry(width=15)
user_input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles", font=("Century Gothic", 14, "normal"))
miles_label.grid(row=0, column=2)

is_equal_to_label = tkinter.Label(text="is equal to", font=("Century Gothic", 14, "normal"))
is_equal_to_label.grid(row=1, column=0)

result_label = tkinter.Label(text="0", font=("Century Gothic", 14, "normal"))
result_label.grid(row=1, column=1)

Km_label = tkinter.Label(text="Km", font=("Century Gothic", 14, "normal"))
Km_label.grid(row=1, column=2)


def calculate():
    calculated_value = float(user_input.get()) * 1.6
    result_label.config(text=str(round(calculated_value)))


calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

window.mainloop()
