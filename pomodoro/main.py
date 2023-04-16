from tkinter import *

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
check_mark = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, check_mark, timer
    check_mark = ""
    reps = 0
    if timer is not None:
        window.after_cancel(timer)
    timer = None
    label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    canvas.itemconfig(text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def button_start_callback():
    if timer is None:
        start()


def start():
    global reps
    reps += 1
    if reps % 8 == 0:
        label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
        global check_mark
        check_mark += "✔"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(seconds):
    minutes = seconds // 60
    canvas.itemconfig(text, text=f"{minutes:02d}:{seconds % 60:02d}")
    if seconds > 0:
        global timer
        timer = window.after(1000, count_down, seconds - 1)
    else:
        check_label.config(text=check_mark)
        start()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="/home/dfrossard/Desktop/100-Days-of-Python/pomodoro-start/tomato.png")
canvas.create_image(102, 112, image=tomato)
text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label.grid(row=0, column=1)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
check_label.grid(row=3, column=1)

button_start = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 10, "bold"), command=button_start_callback)
button_start.grid(row=2, column=0)

button_reset = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 10, "bold"), command=reset)
button_reset.grid(row=2, column=2)

window.mainloop()
