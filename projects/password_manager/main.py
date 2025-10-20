from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200,highlightthickness=0)
padlock_img = PhotoImage(file="/home/deniz/deniz-python-learning/projects/password_manager/logo.png")
canvas.create_image(100,100,image=padlock_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:",highlightthickness=0)
website_label.grid(column=0,row=1,sticky='e')

website_entry = Entry(width=35)
website_entry.grid(column=1, columnspan=2, row=1)

email_label = Label(text="Email:",highlightthickness=0)
email_label.grid(column=0,row=2,sticky='e')

email_entry = Entry(width=35)
email_entry.grid(column=1, columnspan=2, row=2)

password_label = Label(text="Password:",highlightthickness=0)
password_label.grid(column=0,row=3,sticky='e')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='e')

genpass_button = Button(text="Generate Password",highlightthickness=0,padx=0,pady=0,width=14)
genpass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36,highlightthickness=0,padx=0,pady=0)
add_button.grid(column= 1, columnspan=2, row=4)



window.mainloop() 