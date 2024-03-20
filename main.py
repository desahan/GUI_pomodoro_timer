from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    ticks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short_rest = SHORT_BREAK_MIN * 60
    long_rest = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_rest)
        label.config(text="Break", fg=RED)
        amount_pf_work = math.floor(reps / 2)
        ticks.config(text=amount_pf_work*"✔")
    elif reps % 2 == 0:
        countdown(short_rest)
        label.config(text="Break", fg=PINK)
        amount_pf_work = math.floor(reps / 2)
        ticks.config(text=amount_pf_work*"✔")
    else:
        countdown(work)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", bg=YELLOW, fg=GREEN)
label.config(font=(FONT_NAME, 30, "bold"))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

ticks = Label(bg=YELLOW, fg=GREEN)
ticks.grid(column=1, row=3)

window.mainloop()
