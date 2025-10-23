from tkinter import *
import random
import pyperclip
import pandas as pd
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- CARDS LIST ------------------------------- #
try:
    df = pd.read_csv("~/deniz-python-learning/projects/flash_card/data/words_to_learn.csv")
    dictionary = df.to_dict(orient='records')
except FileNotFoundError:
    df = pd.read_csv("~/deniz-python-learning/projects/flash_card/data/french_words.csv")
    dictionary = df.to_dict(orient='records')






current_card = {}

def get_new_word():
    global current_card, flip_timer
    current_card =  random.choice(dictionary)
    window.after_cancel(flip_timer)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=current_card['French'], fill="black")
    canvas.itemconfig(background_img, image=image_cardfront)
    flip_timer = window.after(3000, func=flip)

def check_button():
    global current_card
    dictionary.remove(current_card)
    get_new_word()
    to_be_saved = pd.DataFrame(dictionary)
    to_be_saved.to_csv("~/deniz-python-learning/projects/flash_card/data/words_to_learn.csv", index=False)
    

def equis_button():
    global current_card, flip_timer
    get_new_word()
    to_be_saved = pd.DataFrame(dictionary)
    to_be_saved.to_csv("~/deniz-python-learning/projects/flash_card/data/words_to_learn.csv", index=False)
    



def flip():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=current_card['English'], fill="white")
    canvas.itemconfig(background_img, image=image_cardback)



 

# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

# Canvas

canvas = Canvas(width=800, height=526)
image_cardfront = PhotoImage(file="~/deniz-python-learning/projects/flash_card/images/card_front.png")
background_img = canvas.create_image(400,263,image=image_cardfront)
language = canvas.create_text(400,150,text="Title", font=("Ariel", 40, "italic"),fill="black")
word = canvas.create_text(400,263,text="", font=("Ariel", 60, "bold"),fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)
image_cardback = PhotoImage(file="~/deniz-python-learning/projects/flash_card/images/card_back.png")



# Buttons

correct_button_img = PhotoImage(file="~/deniz-python-learning/projects/flash_card/images/right.png")
correct_button = Button(image=correct_button_img,highlightthickness=0, padx=0, pady=0,bg=BACKGROUND_COLOR, command=check_button)
correct_button.grid(column=0,row=1)

wrong_button_img = PhotoImage(file="~/deniz-python-learning/projects/flash_card/images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, padx=0, pady=0,bg=BACKGROUND_COLOR, command=equis_button)
wrong_button.grid(column=1,row=1)
# Labels

# what_language_label = Label(text="French", font=("Ariel", 40, "italic"),bg="white")
# what_language_label.place(x=300, y=120)

# word_label = Label(text="Word", font=("Ariel", 60, "bold"), bg="white")
# word_label.place(x=270,y=250)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 





flip_timer = window.after(3000, func=flip)
get_new_word()
print(current_card)
window.mainloop() 

