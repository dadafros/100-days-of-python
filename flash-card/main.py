from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
timer = None
card = None
toggle = False


def right_callback():
    if card:
        data.remove(card)
    next_card()


def next_card():
    global card
    try:
        card = random.choice(data)
    except:
        card = None
        end_message()
    else:
        canvas.itemconfig(image, image=card_front_image)
        canvas.itemconfig(language, text="French", fill="black")
        canvas.itemconfig(word, text=card["French"], fill="black")


def flip_card(event):
    global toggle
    if card:
        if toggle:
            canvas.itemconfig(image, image=card_back_image)
            canvas.itemconfig(language, text="English", fill="white")
            canvas.itemconfig(word, text=card["English"], fill="white")
            toggle = False
        else:
            canvas.itemconfig(image, image=card_front_image)
            canvas.itemconfig(language, text="French", fill="black")
            canvas.itemconfig(word, text=card["French"], fill="black")
            toggle = True
    else:
        end_message()


def end_message():
    canvas.itemconfig(image, image=card_front_image)
    canvas.itemconfig(language, text="You got everything", fill="black")
    canvas.itemconfig(word, text="covered!", fill="black")


# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image = canvas.create_image(400, 263, image=card_front_image)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.bind("<Button-1>", flip_card)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button = Button(image=right_image, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR,
                      activebackground=BACKGROUND_COLOR, command=right_callback)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong_image, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR,
                      activebackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

try:
    data = pd.read_csv("data/words_to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv").to_dict(orient="records")
except:
    end_message()

next_card()

window.mainloop()

try:
    df = pd.DataFrame(data)
except:
    pass
else:
    df.to_csv("data/words_to_learn.csv", index=False)
