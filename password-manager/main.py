from tkinter import *
from tkinter import messagebox
import random
import json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password = [random.choice(letters) for _ in range(nr_letters)]
    password += [random.choice(symbols) for _ in range(nr_symbols)]
    password += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password)
    password = "".join(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    try:
        with open(file="data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Save some passwords first.")
    else:
        website = website_entry.get()
        if website in data:
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\n"
                                                       f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Oops", message="Website not found")


def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if website == "":
        messagebox.showinfo(title="Oops", message="You must provide a Website")
    elif email == "":
        messagebox.showinfo(title="Oops", message="You must provide an Email/Username")
    elif password == "":
        messagebox.showinfo(title="Oops", message="You must provide a Password")
    elif messagebox.askokcancel(message=f"Check entered info:\nWebsite: {website}\n"
                                        f"Email: {email}\nPassword: {password}\n"
                                        "Is it ok to save?"):
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        try:
            with open("data.json") as file:
                data = json.load(file)
        except:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                data.update(new_data)
                json.dump(data, file, indent=4)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Image
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email / Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
username_entry = Entry(width=40)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, f"davi_bf@outlook.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=16, command=search)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Save", width=40, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
