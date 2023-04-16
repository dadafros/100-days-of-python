from tkinter import *
from tkinter import messagebox
import os
import requests
from PIL import Image, ImageTk

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN") # Stored in replit secrets
SHEETY_ENDPOINT = "https://api.sheety.co/78ea250cebb814128750091852f45ff4/flightDeals/users"

def create_row(first_name, last_name, email):
  json = {
    "user": {
      "firstName": first_name,
      "lastName": last_name,
      "email": email,
    }
  }
  response = requests.post(SHEETY_ENDPOINT, headers={"Authorization": SHEETY_TOKEN}, json=json)
  response.raise_for_status()
  return response.text

def save():  
  first_name = first_name_entry.get()
  last_name = last_name_entry.get()
  email = email_entry.get()
  email_replica = email_replica_entry.get()

  if first_name == "":
      messagebox.showinfo(title="Oops", message="You must provide a First Name")
  elif last_name == "":
      messagebox.showinfo(title="Oops", message="You must provide a Last Name")
  elif email == "":
      messagebox.showinfo(title="Oops", message="You must provide an Email")
  elif email != email_replica:
      messagebox.showinfo(title="Oops", message="Emails don't match!")
  elif messagebox.askokcancel(message=f"Check entered info:\nFirst Name: {first_name}\n"
                                        f"Last Name: {last_name}\nEmail: {email}\n"
                                        "Is it ok to save?"):
      try:
        create_row(first_name, last_name, email)
      except Exception as error:
        print(error)
        print("Error. Try again later.")
      else:
        messagebox.showinfo(title="Success", message="You are in the club!")
      
      first_name_entry.delete(0, END)
      last_name_entry.delete(0, END)
      email_entry.delete(0, END)
      email_replica_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Davi's Flight Club")
window.config(padx=20, pady=20)

# Image
logo = Image.open("logo.png").resize((256, 256))
logo = ImageTk.PhotoImage(logo)
canvas = Canvas(width=256, height=256)
canvas.create_image(128, 128, image=logo)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
canvas.create_text(128, 50, text="Welcome to Davi's Flight Club!", fill="black", font=('Helvetica 10 bold'))
canvas.create_text(128, 65, text="We find the best flight deals and email you", fill="black", font=('Helvetica 7 italic'))
first_name_label = Label(text="First Name:")
first_name_label.grid(row=1, column=0)
last_name_label = Label(text="Last Name:")
last_name_label.grid(row=2, column=0)
email_label = Label(text="Email:")
email_label.grid(row=3, column=0)
email_replica_label = Label(text="Retype Email:")
email_replica_label.grid(row=4, column=0)


# Entries
first_name_entry = Entry(width=25)
first_name_entry.grid(row=1, column=1)
first_name_entry.focus()
last_name_entry = Entry(width=25)
last_name_entry.grid(row=2, column=1)
email_entry = Entry(width=25)
email_entry.grid(row=3, column=1)
email_replica_entry = Entry(width=25)
email_replica_entry.grid(row=4, column=1)

# Buttons
add_button = Button(text="Save", width=23, command=save)
add_button.grid(row=5, column=1)

window.mainloop()
