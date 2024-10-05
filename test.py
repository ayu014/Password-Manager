from tkinter import *
from tkinter import messagebox
import PasswordGenerator
import pyperclip
import json
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    created_pass = PasswordGenerator.generate()
    password_entry.insert(0, created_pass)
    pyperclip.copy(created_pass)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    uid = id_entry.get()
    password = password_entry.get()

    if len(website) == 0:
        messagebox.showerror(title="Oops", message="Please, don't leave the website field empty!")
    elif len(password) == 0:
        messagebox.showerror(title="Oops", message="Please, don't leave the password field empty!")
    elif len(uid) == 0:
        messagebox.showerror(title="Oops", message="Please, don't leave the Email/Username field empty!")
    else:
        is_ok = messagebox.askokcancel(title="Details", message=f"These are the details entered:\nWebsite: {website}\n"
                                                                f"Email/Username: {uid}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            new_data = {
                website: {
                    "Email": uid,
                    "Password": password
                }
            }

            try:
                with open("data.json", mode="r") as data_file:
                    # Attempt to load existing data
                    data = json.load(data_file)
            except (FileNotFoundError, json.JSONDecodeError):
                # If the file is missing or contains invalid JSON, we start with new data
                data = new_data
            else:
                # Update old data with the new data
                data.update(new_data)
            
            # Save updated data to data.json
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

            # Clear the entry fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(title="Saved", message="All the details are saved successfully.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas for logo
canvas = Canvas(height=200, width=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_label.grid(row=1, column=0, sticky="e")

id_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
id_label.grid(row=2, column=0, sticky="e")

password_label = Label(text="Password:", font=("Arial", 10, "normal"))
password_label.grid(row=3, column=0, sticky="e")

# Entry fields
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

id_entry = Entry(width=35)
id_entry.grid(row=2, column=1, columnspan=2)
id_entry.insert(END, "ayush0187cse@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=14)
search_button.grid(row=1, column=2)

gen_button = Button(text="Generate Password", command=generate_pass, width=14)
gen_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()