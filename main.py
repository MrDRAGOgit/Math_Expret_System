import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

EditorOpen = False

class KeyEditor(Toplevel):
    txt_box = ""
    def __init__(self, parent):
        super().__init__(parent)
        self.protocol("WM_DELETE_WINDOW", self.close_editor)
        self.title("Addition of key words")
        self.rowconfigure(0, minsize=800, weight=1)
        self.columnconfigure(1, minsize=800, weight=1)
        self.txt_box = tk.Text(self)
        frm_buttons = tk.Frame(self, relief=tk.RAISED, bd=2)
        btn_open = tk.Button(frm_buttons, text="Open", command=self.open_file)
        btn_save = tk.Button(frm_buttons, text="Save As...", command=self.save_file)

        btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_save.grid(row=1, column=0, sticky="ew", padx=5)

        frm_buttons.grid(row=0, column=0, sticky="ns")
        self.txt_box.grid(row=0, column=1, sticky="nsew")

    def close_editor(self):
        self.destroy()
        global EditorOpen
        EditorOpen = False

    def open_file(self):
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        self.txt_box.delete("1.0", tk.END)
        with open(filepath, mode="r", encoding="utf-8") as input_file:
            text = input_file.read()
            self.txt_box.insert(tk.END, text)
        self.title(f"Simple Text Editor - {filepath}")

    def save_file(self):
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, mode="w", encoding="utf-8") as output_file:
            text = self.txt_box.get("1.0", tk.END)
            output_file.write(text)
        self.title(f"Simple Text Editor - {filepath}")


class MainApp(tk.Tk):
    N = 1
    Input = ""
    txt_edit = 0
    filepath = "keywords.txt"
    keys = []
    keysfound = []
    showkeys = ""

    def __init__(self):
        super().__init__()
        with open(self.filepath, mode="r", encoding="utf-8") as input_file:
            for text in input_file:
                text = text[:-2]
                self.keys.append(text.split(';'))
        print(self.keys)
        self.title("Math Expert System")
        self.txt_edit = Text(self, width=40, height=10)
        self.showkeys = LabelFrame(self, text="Found keys will be shown here", width=40, height=10)
        self.keysfound = [Label(self.showkeys, text="")]

        frm_buttons = Frame(self, relief=RAISED, bd=2)
        btn_input = Button(frm_buttons, text="Input", command=self.read_input)
        btn_analyze = Button(frm_buttons, text="Analyze", command=self.analyze)
        btn_call_keyeditor = Button(frm_buttons, text="Edit keys", command=self.open_editor)

        btn_input.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_analyze.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        btn_call_keyeditor.grid(row=0, column=2, sticky="ew", padx=5, pady=5)

        self.set_keys()

        self.showkeys.grid(row=0, column=1, sticky="ns")
        frm_buttons.grid(row=1, column=0, sticky="ns")
        self.txt_edit.grid(row=0, column=0, sticky="nsew")

    def set_keys(self):
        i = 0
        for key in self.keysfound:
            key.grid(row=i, column=0, sticky="ew", padx=5, pady=5)
            i += 1

    def open_editor(self):
        global EditorOpen
        editor = KeyEditor(self)
        if not EditorOpen:
            EditorOpen = True
            editor.grab_set()

    def read_input(self):
        self.Input = self.txt_edit.get("1.0", END)

    def analyze(self):
        for row in self.keys:
            for key in row:
                if key in self.Input:
                    print("yes")
                    self.keysfound.append(Label(self.showkeys, text=key))
                else:
                    print("no")
        self.set_keys()


window = MainApp()
window.mainloop()
