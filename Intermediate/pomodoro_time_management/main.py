from math import floor
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
CHECKMARK = "✔"
reps = 0
timer_job = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer_job)
    checkmark_label.config(text="")
    activity_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    if reps == 8:
        activity_label.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
        reps = 0
    elif reps % 2 == 0:
        activity_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        activity_label.config(text="Working", fg=GREEN)
        count_down(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer_job
    seconds = count % 60
    minutes = floor(count / 60)
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        timer_job = window.after(10, count_down, count - 1)
    else:
        start_timer()
        checkmark_label.config(text=CHECKMARK * floor(reps / 2))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Time Management")
window.config(padx=100, pady=50, bg=YELLOW)

activity_label = Label(text="Timer", bg=YELLOW, fg=GREEN,font=(FONT_NAME, 55, "bold"))
activity_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
TOMATO_IMG = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=TOMATO_IMG)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer).grid(column=0, row=2)
reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer).grid(column=2, row=2)

checkmark_label = Label(bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)

window.mainloop()
