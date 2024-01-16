#==== Imports ====#
from tkinter import *
import json
from ..server.summarization import extractive_summarization, abstractive_summarization


#==== Function Definitions ====#
# Summarization
def summarizer():
    input = text.get()

    if len(site) == 0 or len(pass_) == 0:
        messagebox.showwarning(title = "Empty Fields",
                               message = "Please don't leave any field empty")
    else:
        try:
            with open(FILE, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(FILE, "w") as file:
                json.dump(credentials, file, indent = 4)
        else:
            data.update(credentials)

            with open(FILE, "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)


#==== Declarations ====#
window = Tk()
text = Text(height = 17, width = 130)
scale = Spinbox(from_ = 0, to = 100, width = 7)  #, command = scale_widget)
summarize = Button(text = "Summarize", command = summarizer)
output = Label(bg = "white", height = 12, width = 135, font = ("Times New Roman", 12))


#==== Body ====#
# UI Setup
window.title("K  H  A  Y  '  S    S  U  M  M  A  R  I  Z  E  R")
window.config(padx = 50, pady = 50)

text.grid(column=0, row=0, columnspan=5, rowspan=5, padx=10, pady=10)
text.focus()

scale.grid(column = 5, row = 1)

summarize.config(padx=20)
summarize.grid(column = 2, row = 5, pady=10)

output.grid(column=0, row=6, columnspan=5, rowspan=5, padx=10, pady=10)

window.mainloop()