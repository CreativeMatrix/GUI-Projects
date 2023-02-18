from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FLIP_CARD_TIMER = 5000
current_card = {}  

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_list = original_data.to_dict(orient="records")
else:  
    data_list = data.to_dict(orient="records")


def next_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(FLIP_CARD_TIMER, func=flip_card)
    
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)

def remove_card():
    data_list.remove(current_card)
    data = pandas.DataFrame(data_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_word()


window = Tk()
window.title("Flashy".center(50))
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(window, width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)

card_front = PhotoImage(file="./images/card_front.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

card_back = PhotoImage(file="./images/card_back.png")

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_card)
right_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_word)
wrong_button.grid(column=1, row=1)

next_word()

window.mainloop()