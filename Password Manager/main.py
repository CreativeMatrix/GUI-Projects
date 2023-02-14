from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH ------------------------------- #

def search():
    user_search = website_entry.get().title()
    try:
        with open("data.json") as data_file:
            json_search_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found. Please save a password.")
    else:
        if user_search in json_search_data:
            email = json_search_data[user_search]["email"]
            password = json_search_data[user_search]["password"]
            messagebox.showinfo(title=user_search, message=f"Email: {email}\nPassword: {password}")
        elif user_search not in json_search_data:
            messagebox.showinfo(title="Search Failed", message=f"No credientials for {user_search} exists.")

    
# ---------------------------- SAVE ------------------------------- #

def save_data():
    new_data = {
        website_entry.get().title(): {
            "email": email_entry.get(),
            "password" : password_entry.get()
        }
    }

    if len(website_entry.get()) == 0: 
        messagebox.showinfo(title="ERROR", message="Please enter an official Website")
    elif len(email_entry.get()) == 0:
        messagebox.showinfo(title="ERROR", message="Please enter a valid Email")
    elif len(password_entry.get()) == 0:
        messagebox.showinfo(title="ERROR", message="Please enter a secure Password")
    else:
        data_is_correct = messagebox.askokcancel(title="SAVE DATA", message=f"Would you like to save the following information? \nWEBSITE: {website_entry.get().title()} \nEMAIL: {email_entry.get()} \nPASSWORD: {password_entry.get()}")

        if data_is_correct:
            try:
                with open("data.json", "r") as data_file:
                    json_data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                json_data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(json_data, data_file, indent=4)
            
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager".center(25))
window.config(padx=25, pady=25)

canvas = Canvas(window, width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


website_label = Label(text="Website:")
website_entry = Entry(width=33)
website_entry.focus()
website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)


email_label = Label(text="Email/Username:")
email_entry = Entry(width=52)
email_label.grid(column=0, row=2)
email_entry.grid(column=1, row=2, columnspan=2, sticky=W)


password_label = Label(text="Password:")
password_entry = Entry(width=33)
password_button = Button(text="Generate Password", command=generate_password)
password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3, sticky=W)
password_button.grid(column=2, row=3, sticky=W)

search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()