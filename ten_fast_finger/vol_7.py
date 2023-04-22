from tkinter import *
from tkinter import ttk
from pynput.keyboard import Key, Listener

left_to_right = "E,S"
all_area = "N,W,E,S"
from_top_to_bottom = "N,W"
average_font = ("times", 14, "bold")
# https://tcl.tk/man/tcl8.6/TkCmd/keysyms.htm  keyboard specific numbers

class TenFastFingers:

    def __init__(self, master):
        self.master = master
        master.title("Ten Fast Fingers GUI")
        master.geometry("800x500")

        self.label = ttk.Label(master,background="yellow", font=average_font, text="Words will show up here !")
        self.label.grid(columnspan=20, row=0,padx=20, pady=20)

        self.entry_var = StringVar()
        self.entry = ttk.Entry(master, font=average_font, textvariable=self.entry_var)
        self.entry.grid(columnspan=20, row=2,padx=20, pady=20)
        self.entry.focus_set()
        # self.entry_var.get()
        self.button = ttk.Button(master, text="Bas Kardeşim", command=self.button_func, width=30)
        self.button.grid(column=3, row=3, padx=20, pady=20)

        self.label.bind('<Enter>', lambda x: self.space_key_func())

        self.seperator = ttk.Separator(master,orient=HORIZONTAL)
        self.seperator.grid(row=2)
            
    def button_func(self):
        print("Tebrikler amın oğlu")

    def space_key_func(self):
        f = open("append.txt", "a")
        f.write(str(self.entry_var))
        f.close()


root = Tk()

TenFastFingers(root)

root.mainloop()
