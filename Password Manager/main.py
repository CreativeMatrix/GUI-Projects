from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    if len(website_entry.get()) == 0: 
        messagebox.showinfo(title="ERROR", message="Please enter an official Website")
    elif len(email_entry.get()) == 0:
        messagebox.showinfo(title="ERROR", message="Please enter a valid Email")
    elif len(password_entry.get()) == 0:
        messagebox.showinfo(title="ERROR", message="Please enter a secure Password")
    else:
        data_is_correct = messagebox.askokcancel(title="SAVE DATA", message=f"Would you like to save the following information? \nWEBSITE: {website_entry.get()} \nEMAIL: {email_entry.get()} \nPASSWORD: {password_entry.get()}")

        if data_is_correct:
            data_file = open("data.txt", "a")
            data_file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            data_file.close()
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
website_entry = Entry(width=52)
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


add_button = Button(text="Add", width=44, command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

window.mainloop()