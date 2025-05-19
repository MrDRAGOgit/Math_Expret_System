import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

Input = ""
EditorOpen = False


class KeyEditor(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.protocol("WM_DELETE_WINDOW", self.close_editor)
        self.title("Addition of key words")
    def close_editor(self):
        self.destroy()
        global EditorOpen
        EditorOpen = False


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Math Expert System")
        txt_edit = Text(self, width=40, height=10)
        showkeys = LabelFrame(self, width=40, height=10)
        keysbase = ["", "", ""]
        keysbase[0] = Label(showkeys, text="agdfiafi")
        frm_buttons = Frame(self, relief=RAISED, bd=2)
        btn_input = Button(frm_buttons, text="input", command=self.read_input)
        btn_analyze = Button(frm_buttons, text="analyze", command=self.analyze)
        btn_call_keyeditor = Button(frm_buttons, text="edit keys", command=self.open_editor)

        btn_input.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_analyze.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        btn_call_keyeditor.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

        frm_buttons.grid(row=1, column=0, sticky="ns")
        txt_edit.grid(row=0, column=0, sticky="nsew")

    def open_editor(self):
        global EditorOpen
        editor = KeyEditor(self)
        if not EditorOpen:
            EditorOpen = True
            editor.grab_set()

    def read_input(self):
        global Input
        Input = self.txt_edit.get("1.0", END)

    def analyze(self):
        global Input
        if "abc" in Input:
            print("yes")
        else:
            print("no")


filepath = "keywords.txt"
with open(filepath, mode="r", encoding="utf-8") as input_file:
    text = input_file.read()


window = MainApp()
window.mainloop()
