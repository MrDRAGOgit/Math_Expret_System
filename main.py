import tkinter as tk
from tkinter import *


# def btn_print():
#     print(entry.get())
#
#
# root = Tk()
#
# entry = Entry()
# button = Button(text="click", command=btn_print)
#
# entry.pack()
# button.pack()
#
# root.mainloop()
from tkinter.filedialog import askopenfilename, asksaveasfilename

Input = ""


# def open_file():
#     """Open a file for editing."""
#     filepath = askopenfilename(
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
#     )
#     if not filepath:
#         return
#     txt_edit.delete("1.0", END)
#     with open(filepath, mode="r", encoding="utf-8") as input_file:
#         text = input_file.read()
#         txt_edit.insert(END, text)
#     window.title(f"Simple Text Editor - {filepath}")


# def save_file():
#     """Save the current file as a new file."""
#     filepath = asksaveasfilename(
#         defaultextension=".txt",
#         filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
#     )
#     if not filepath:
#         return
#     with open(filepath, mode="w", encoding="utf-8") as output_file:
#         text = txt_edit.get("1.0", END)
#         output_file.write(text)
#     window.title(f"Simple Text Editor - {filepath}")


def read_input():
    global Input
    Input = txt_edit.get("1.0", END)


def analyze():
    global Input
    if "abc" in Input:
        print("yes")
    else:
        print("no")


window = Tk()
window.title("Simple Text Editor")

# window.rowconfigure(0, minsize=100, weight=1)
# window.columnconfigure(1, minsize=400, weight=1)

txt_edit = Text(window, width=40, height=10)
frm_buttons1 = Frame(window, relief=RAISED, bd=2)
frm_buttons2 = Frame(window, relief=RAISED, bd=2)
# btn_open = Button(frm_buttons1, text="Open", command=open_file)
btn_input = Button(frm_buttons2, text="input", command=read_input)
btn_analyze = Button(frm_buttons2, text="analyze", command=analyze)

# btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_input.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_analyze.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

# frm_buttons1.grid(row=0, column=2, sticky="ns")
frm_buttons2.grid(row=1, column=0, sticky="ns")
txt_edit.grid(row=0, column=0, sticky="nsew")

window.mainloop()
