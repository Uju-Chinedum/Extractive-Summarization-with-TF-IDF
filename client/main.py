#==== Imports ====#
from tkinter import *
from summarization import extractive_summarization, abstractive_summarization


#==== Function Definitions ====#
def on_text_click(event):
    if text.get("1.0", "end-1c") == "Enter your text here...":
        text.delete("1.0", "end")
        text.config(fg='black')


# Summarization
def summarizer():
    input = text.get()
    sentences = int(entry.get())

    extractive = extractive_summarization(input, sentences)

    output.config(text = extractive)


#==== Declarations ====#
window = Tk()
text = Text(height = 17, width = 130, wrap="word", font = ("Times New Roman", 12))
entry = Entry(width = 4)
entry_label = Label(text = "Number of Sentences: ", font = ("Times New Roman", 12))
summarize = Button(text = "Summarize", font = ("Times New Roman", 10, "bold"), command = summarizer)
output = Label(text = "OUTPUT", bg = "white", height = 12, width = 135, font = ("Times New Roman", 12))


#==== Body ====#
# UI Setup
window.title("K  H  A  Y  '  S    S  U  M  M  A  R  I  Z  E  R")
window.config(padx = 50, pady = 50)

text.grid(column=0, row=0, columnspan=5, rowspan=5, padx=10, pady=10)
text.insert("1.0", "Enter your text here...")
text.config(fg='grey')  # Set initial text color to grey
text.bind("<FocusIn>", on_text_click)

entry.grid(column = 1, row = 5)
entry.insert(0, 7)

entry_label.grid(column = 0, row = 5, columnspan = 2)

summarize.config(padx=20)
summarize.grid(column = 2, row = 5, pady=10)

output.grid(column=0, row=6, columnspan=5, rowspan=5, padx=10, pady=10)

window.mainloop()