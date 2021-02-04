from tkinter import *
import pandas
import random

card_dict = {}


def del_new_card():
    global card_dict, flip_timer, data_dict
    data_dict.remove(card_dict)
    window.after_cancel(flip_timer)
    card_dict = random.choice(data_dict)
    canvas.itemconfig(img, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=card_dict["French"])
    flip_timer = window.after(3000, func=card_flip)


def new_card():
    global card_dict, flip_timer
    window.after_cancel(flip_timer)
    card_dict = random.choice(data_dict)
    canvas.itemconfig(img, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=card_dict["French"])
    flip_timer = window.after(3000, func=card_flip)


def card_flip():
    global card_dict
    canvas.itemconfig(img, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=card_dict["English"])


BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

x_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=x_img, highlightthickness=0, command=new_card)
button_wrong.grid(row=1, column=0)

y_img = PhotoImage(file="images/right.png")
button_right = Button(image=y_img, highlightthickness=0, command=del_new_card)
button_right.grid(row=1, column=1)

try:
    data = pandas.read_csv("words_to_learn.csv")
    data_dict = data.to_dict(orient="records")
    print("FOUND FILE")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
    print("NO FILE")

new_card()

window.mainloop()

output = pandas.DataFrame(data_dict)
output.to_csv("words_to_learn.csv", index=False)
