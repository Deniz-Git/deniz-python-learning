from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label

my_label = tkinter.Label(text="I Am a Label",font=("Arial",24,"bold"))
my_label.grid(column=0, row=0)


my_label["text"] = "New Text"
my_label.config(text="New Text")

#Buttons

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1,row=1)

button2 = Button(text="New Button", command=button_clicked)
button2.grid(column=2, row=0)


#Entry

input = Entry(width=10)
input.grid(column=3,row=2)

window.mainloop()

