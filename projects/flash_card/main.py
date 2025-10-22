from tkinter import *
import random
import pyperclip
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- CARDS LIST ------------------------------- #

df = pd.read_csv("/home/deniz/deniz-python-learning/projects/flash_card/data/french_words.csv")
dictionary = df.to_dict(orient='records')

def new_word_fun():
    randomly_picked_word = random.choice(dictionary)['French']
    canvas.itemconfig(word, text=randomly_picked_word)





# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

# Canvas

canvas = Canvas(width=800, height=526)
image_cardfront = PhotoImage(file="/home/deniz/deniz-python-learning/projects/flash_card/images/card_front.png")
canvas.create_image(400,263,image=image_cardfront)
language = canvas.create_text(400,150,text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400,263,text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0,row=0, columnspan=2)



# Buttons

correct_button_img = PhotoImage(file="/home/deniz/deniz-python-learning/projects/flash_card/images/right.png")
correct_button = Button(image=correct_button_img,highlightthickness=0, padx=0, pady=0,bg=BACKGROUND_COLOR, command=new_word_fun)
correct_button.grid(column=0,row=1)

wrong_button_img = PhotoImage(file="/home/deniz/deniz-python-learning/projects/flash_card/images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, padx=0, pady=0,bg=BACKGROUND_COLOR, command=new_word_fun)
wrong_button.grid(column=1,row=1)

# Labels

# what_language_label = Label(text="French", font=("Ariel", 40, "italic"),bg="white")
# what_language_label.place(x=300, y=120)

# word_label = Label(text="Word", font=("Ariel", 60, "bold"), bg="white")
# word_label.place(x=270,y=250)





new_word_fun()
window.mainloop() 

