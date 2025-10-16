from tkinter import *

window = Tk()
window.title("Mile to KM converter")
# window.minsize(width=100, height=80)
window.config(padx=20, pady=20)

#Function

def calculation():
    to_be_converted = float(entry.get())
    km = to_be_converted * 1.609344
    label_1_1.config(text=round(km,2))



#Labels

#first row labels

label_3_0 = Label(text="Miles", anchor="sw")
label_3_0.grid(column=2, row=0)


#second row labels
label_0_1 = Label(text="is equal to", anchor="e")
label_0_1.grid(column=0,row=1)

label_1_1 = Label(text="0", anchor="center")
label_1_1.grid(column=1, row=1)

label_2_1 = Label(text="Km", anchor="w")
label_2_1.grid(column=2, row=1)


#Button

button = Button(text="Calculate",command=calculation,anchor="n")
button.grid(column=1,row=2)

#Entry

entry = Entry(width=10)
entry.grid(column=1,row=0)






window.mainloop()
