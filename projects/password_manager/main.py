from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

def present_pass():
    password_entry.delete(0,END)
    password = gen_pass()
    password_entry.insert(0,str(password.strip()))

def gen_pass():
    password_list = [random.choice(letters) for x in range(nr_letters)]
    password_list += [random.choice(symbols) for x in range(nr_symbols)]
    password_list += [random.choice(numbers) for x in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char
    pyperclip.copy(password)
    return password
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    print(website)
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if not website or not password:
        messagebox.showwarning(title="WARNING!", message="Missing information!")
    else:
        try:
            with open("/home/deniz/deniz-python-learning/projects/password_manager/data.json", mode="r") as file:
                
                #Reading old data
                data = json.load(file)

                #Saving updated data
        except FileNotFoundError:
            with open("/home/deniz/deniz-python-learning/projects/password_manager/data.json", "w") as file:
                json.dump(new_data,file,indent=4)
        
        else:
            data.update(new_data)

            with open("/home/deniz/deniz-python-learning/projects/password_manager/data.json", mode="w") as file:
                json.dump(data, file, indent= 4)

        finally:
            website_entry.delete(0,END)
            # email_entry.delete(0,END)
            password_entry.delete(0,END)
 
# ---------------------------- SEARCH OPERATION ------------------------------- #
 
def search_fun():
    key_searched = website_entry.get()
    try:
        with open("/home/deniz/deniz-python-learning/projects/password_manager/data.json", mode="r") as file:
            data = json.load(file)
            email = data[key_searched]["email"]
            print(email)
            password = data[key_searched]["password"]
            print(password)
            messagebox.showinfo(title=str(key_searched.strip()), message=f"Email: {email}\nPassword: {password}")


    except FileNotFoundError:
        messagebox.showwarning(title="WARNING!", message="JSON FILE DOESN'T EXIST")
    except KeyError:
        messagebox.showerror(title="ATTENTION!", message="Make sure website is written correctly else, info doesn't exist")

        






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200,highlightthickness=0)
padlock_img = PhotoImage(file="/home/deniz/deniz-python-learning/projects/password_manager/logo.png")
canvas.create_image(100,100,image=padlock_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:",highlightthickness=0)
website_label.grid(column=0,row=1,)

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)

search_button = Button(text="Search", padx=0, pady=0, width=20, command=search_fun)
search_button.grid(column=2, row=1)

email_label = Label(text="Email:",highlightthickness=0)
email_label.grid(column=0,row=2)

email_entry = Entry(width=41)
email_entry.grid(column=1, columnspan=2, row=2)
email_entry.insert(0,"lupusipsum@hotmale.com")

password_label = Label(text="Password:",highlightthickness=0)
password_label.grid(column=0,row=3)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

genpass_button = Button(text="Generate Password",highlightthickness=0,padx=0,pady=0,width=20, command=present_pass)
genpass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=41,highlightthickness=0,padx=0,pady=0, command=save_password)
add_button.grid(column= 1, columnspan=2, row=4)






window.mainloop() 