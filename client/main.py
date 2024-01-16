#==== Imports ====#
from tkinter import *
import json


#==== Function Definitions ====#
# # Save Password
# def save():
#     site = website.get()
#     mail = email.get()
#     pass_ = password.get()
#     credentials = {
#         site: {
#             "email": mail,
#             "password": pass_
#         }
#     }

#     if len(site) == 0 or len(pass_) == 0:
#         messagebox.showwarning(title = "Empty Fields",
#                                message = "Please don't leave any field empty")
#     else:
#         try:
#             with open(FILE, "r") as file:
#                 data = json.load(file)
#         except FileNotFoundError:
#             with open(FILE, "w") as file:
#                 json.dump(credentials, file, indent = 4)
#         else:
#             data.update(credentials)

#             with open(FILE, "w") as file:
#                 json.dump(data, file, indent=4)
#         finally:
#             website.delete(0, END)
#             password.delete(0, END)

# # Password Generator
# def gen_passcode():
#     password_letters = [choice(letters) for _ in range(randint(8, 10))]
#     password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
#     password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

#     password_list = password_letters + password_symbols + password_numbers
#     shuffle(password_list)

#     passcode = "".join(password_list)
#     password.insert(0, passcode)
#     pyperclip.copy(passcode)

# # Find Password
# def find_password():
#     try:
#         with open(FILE, "r") as file:
#             data = json.load(file)

#             site = website.get()
#             mail = data[site]["email"]
#             pass_ = data[site]["password"]
#     except FileNotFoundError:
#         messagebox.showwarning(title = "Missing File",
#                                message = "No password file found")
#     except KeyError:
#         messagebox.showwarning(title = "Missing Data",
#                                message = f"No details for {site} exists")
#     else:
#         messagebox.showinfo(title = site, message = f"Email/Username: {mail}\nPassword: {pass_}")



#==== Declarations ====#
window = Tk()
text = Text(height = 17, width = 155)
summarize = Button(text = "Summarize") #, command = gen_passcode)


#==== Body ====#
# UI Setup
window.title("K  H  A  Y  '  S    S  U  M  M  A  R  I  Z  E  R")
window.config(padx = 50, pady = 50)

text.grid(column=0, row=0, columnspan=5, rowspan=5, padx=10, pady=10)
text.focus()

summarize.config(padx=20)
summarize.grid(column = 2, row = 5, pady=10)

window.mainloop()