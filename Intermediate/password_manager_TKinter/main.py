from tkinter import END, Button, Canvas, Entry, Label, PhotoImage, Tk, messagebox
from generator import generator as create_password
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    random_pass = create_password()
    password_entry.delete(0, END)
    password_entry.insert(0, random_pass)
    # Use pypi package to add to clipboard
    # import pyperclip
    # pyperclip.copy(random_pass)
    # pyperclip.paste() # will paste what's in the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    if len(website_entry.get()) == 0 or len(email_user_entry.get()) ==0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Whoops!", message="Make sure all fields are filled out")
        return

    new_data = {
        website_entry.get(): {
            "email": email_user_entry.get(),
            "password": password_entry.get()
        }
    }
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            data.update(new_data)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        with open("data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
            # data.update(f"{website_entry.get()} | {email_user_entry.get()} | {password_entry.get()}\n")
    finally:
        website_entry.delete(0,END)
        password_entry.delete(0,END)
        website_entry.focus()
# ---------------------------- SEARCH PASS ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(message="There is no data file. Save a password to create one")
    else:
        try:
            record = data[website_entry.get()]
        except KeyError:
            messagebox.showerror(message=f"There is no entry for site: {website_entry.get()}")
        else:
            messagebox.showinfo(message=f"Email: {record['email']}\nPassword: {record['password']}")        

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
LOCK_IMAGE = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=LOCK_IMAGE)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:").grid(column=0, row=1)
email_user_label = Label(text="Email/Username:").grid(column=0, row=2)
password_label = Label(text="Password:").grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()
search_button = Button(text="Search", width=10, command=find_password).grid(column=2, row=1)

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "myemail@mail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate", width=10, command=generate_password).grid(column=2, row=3)
save_pass_button = Button(text="Save Password", width=32, command=save_password).grid(column=1, row=4, columnspan=2)



window.mainloop()