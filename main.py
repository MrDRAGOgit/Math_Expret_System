import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

EditorOpen = False
OptimiserOpen = False
MethodDict = {
    "name1": 0,
    "name2": 0,
    "name3": 0
}


class KeyEditor(Toplevel):
    txt_box = ""

    def __init__(self, parent):
        super().__init__(parent)
        self.protocol("WM_DELETE_WINDOW", self.close_editor)
        self.title("Addition of key words")
        self.rowconfigure(0, minsize=400, weight=1)
        self.columnconfigure(1, minsize=400, weight=1)
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


class Optimiser(Toplevel):
    global MethodDict
    dropmenu = ""
    methodoptimisation = ""
    dropdowns = []
    # dropbuttons = []
    dropchoises = []
    numdropdowns = 0

    def __init__(self, parent):
        super().__init__(parent)
        self.protocol("WM_DELETE_WINDOW", self.close_optimiser)
        self.protocol()
        self.title("Algorithm optimiser")
        self.rowconfigure(0, minsize=400, weight=1)
        self.columnconfigure(1, minsize=400, weight=1)
        self.dropmenu = LabelFrame(self, text="Chosen methods", width=40, height=10)
        self.methodoptimisation = LabelFrame(self, text="No method chosen", width=40, height=10)
        self.dropchoises = [StringVar(value="Choose method")]
        self.dropchoises[self.numdropdowns].trace('w', self.trace)
        self.dropdowns = [OptionMenu(self.dropmenu, self.dropchoises[self.numdropdowns], *MethodDict.keys())]
        # self.dropbuttons = [Button(self.dropmenu, text="Configure method", command=lambda: self.set_config_method())]
        btn_close = Button(self, text="Close optimiser", command=self.close_optimiser)

        frm_buttons = Frame(self, relief=RAISED, bd=2)
        btn_add = Button(frm_buttons, text="Add method", command=self.add_dropdown)
        btn_remove = Button(frm_buttons, text="Remove method", command=self.remove_dropdown)
        # btn_add.grid(row=0, column=0, sticky="ns", padx="5", pady="5")
        # btn_remove.grid(row=0, column=1, sticky="ns", padx="5", pady="5")

        # add button to switch config window between selected dropdowns, only needed when i will have more than one

        self.dropmenu.grid(row=0, column=0, sticky="nsew")
        self.methodoptimisation.grid(row=0, column=1, sticky="nsew")
        self.dropdowns[0].grid(row=self.numdropdowns, column=0, sticky="ew", padx=5, pady=5)
        frm_buttons.grid(row=1, column=0, sticky="ns")
        btn_close.grid(row=1, column=1, sticky="ns", padx="5", pady="5")

    def close_optimiser(self):
        self.destroy()
        global OptimiserOpen
        OptimiserOpen = False

    def add_dropdown(self):
        if self.numdropdowns < len(MethodDict)-1:
            self.numdropdowns += 1
            self.dropchoises.append(StringVar(value="Choose method"))  # change to a variable max value later
            self.dropchoises[self.numdropdowns].trace('w', self.trace)
            self.dropdowns.append(OptionMenu(self.dropmenu, self.dropchoises[self.numdropdowns], *MethodDict))
            self.dropdowns[self.numdropdowns].grid(row=self.numdropdowns, column=0, sticky="ew", padx=5, pady=5)

    def remove_dropdown(self):
        if self.numdropdowns > 0:
            self.dropdowns[self.numdropdowns].grid_remove()
            self.dropdowns.pop()
            # self.dropchoises[self.numdropdowns].trace_remove("write", "end")
            self.dropchoises.pop()
            self.numdropdowns -= 1

    def trace(self, *args):  # try passing variables to trace, might solve some of the issues
        self.methodoptimisation.config(text=self.dropchoises[0].get())  # comment this out when/if enabling multiple dropdowns
        for key in MethodDict.keys():
            MethodDict[key] = 0
        for element in self.dropchoises:
            if element.get() != "Choose method":
                MethodDict[element.get()] = 1
        print(MethodDict.values())

    # how to track which trace triggered?
    # use dictionaries maybe?
    # pass the id of the triggered stringval as key for dictionary
    # set what was the stringval set too as the value

    # def set_config_method(self, a):
    #     self.methodoptimisation.config(text=self.dropchoises[a].get())

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
        btn_call_optimiser = Button(frm_buttons, text="Optimise methods", command=self.open_optimiser)

        btn_input.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        btn_analyze.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
        btn_call_keyeditor.grid(row=0, column=2, sticky="ew", padx=5, pady=5)
        btn_call_optimiser.grid(row=0, column=3, sticky="ew", padx=5, pady=5)

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

    def open_optimiser(self):
        global OptimiserOpen
        optimiser = Optimiser(self)
        if not OptimiserOpen:
            OptimiserOpen = True
            optimiser.grab_set()

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
