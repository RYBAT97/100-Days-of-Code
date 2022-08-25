from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#E2979C"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
WORKING_TIMER = None
CHECKMARKS = ["✔", "✔✔", "✔✔✔", "✔✔✔✔"]

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(WORKING_TIMER)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if REPS % 2 == 0:
        timer_label.config(text="Work", fg=GREEN, font=(FONT_NAME, 30, 'bold'))
        count_down(work_secs)
    elif REPS == 7:
        timer_label.config(text="Long Break", fg=RED, font=(FONT_NAME, 24, 'bold'))
        count_down(long_break_secs)
    elif REPS % 2 == 1:
        timer_label.config(text="Short Break", fg=PINK, font=(FONT_NAME, 24, 'bold'))
        count_down(short_break_secs)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    minutes = int(count / 60)
    if minutes < 10:
        minutes = "0" + str(minutes)
    seconds = int(count % 60)
    if seconds < 10:
        seconds = "0" + str(seconds)

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global WORKING_TIMER
        WORKING_TIMER = window.after(1000, count_down, count - 1)
    else:
        global REPS
        if REPS % 2 == 0:
            checkmark_label.config(text=CHECKMARKS[int(REPS/2)])
        if REPS != 7:
            REPS += 1
        window.after(1000, start_timer)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)
checkmark_label = Label(bg=YELLOW, fg=GREEN, font=("Segoe UI Emoji", 12, "bold"))
checkmark_label.grid(row=3, column=1)

window.mainloop()
