from tkinter import *
import pandas
from random import choice

# COLORS
BACKGROUND_COLOR = "#B1DDC6"
# IMAGES
CARD_BACK_IMG = "images/card_back.png"
CARD_FRONT_IMG = "images/card_front.png"
CORRECT_IMG = "images/right.png"
WRONG_IMG = "images/wrong.png"
# GEOMETRY
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 526
LANGUAGE_X = CANVAS_WIDTH / 2
LANGUAGE_Y = CANVAS_HEIGHT / 3 
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_X = CANVAS_WIDTH / 2
WORD_Y = CANVAS_HEIGHT / 2
WORD_FONT = ("Ariel", 60, "bold")
data = {}
words_list = {}
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
finally:
    words_list = data.to_dict(orient="records")

def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = choice(words_list)
    card_canvas.itemconfig(card_background, image=card_front )
    card_canvas.itemconfig(card_language, text="French", fill="black")
    card_canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global current_card
    card_canvas.itemconfig(card_background, image=card_back )
    card_canvas.itemconfig(card_language, text="English", fill="white")
    card_canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def remove_card():
    words_list.remove(current_card)
    data = pandas.DataFrame(words_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# UI
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=CARD_FRONT_IMG)
card_back = PhotoImage(file=CARD_BACK_IMG)
card_background = card_canvas.create_image(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
card_language = card_canvas.create_text(LANGUAGE_X, LANGUAGE_Y, font=LANGUAGE_FONT)
card_word = card_canvas.create_text(WORD_X, WORD_Y, font=WORD_FONT)
card_canvas.grid(row=0, column=0, columnspan=2)

correct_image = PhotoImage(file=CORRECT_IMG)
correct_button = Button(image=correct_image, borderwidth=0, highlightthickness=0, command=remove_card).grid(row=1,column=1)

wrong_image = PhotoImage(file=WRONG_IMG)
wrong_button = Button(image=wrong_image, borderwidth=0, highlightthickness=0, command=next_card).grid(row=1,column=0)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()