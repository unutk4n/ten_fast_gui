from tkinter import *
from tkinter import ttk

left_to_right = "E,S"
all_area = "N,W,E,S"
# This area might be wrong, but you'll find out soon enough.


class TenFastFingers:
    # inside the init func There will be only widgets.
    def __init__(self, master):
        self.master = master
        master.title("Ten Fest Fingers Graphical User Interface a.k.a GUI")
        master.geometry("800x500")

        self.label = ttk.Label(master, text="Let's try if that works")
        self.label.grid(column=0, row=0)

        self.button = ttk.Button(master, text="click me! ", command=self.button_func())
        self.button.grid(column=3, row=1)

    def button_func(self):
        print("Great you clicked and I wrote :) ")


root = Tk()
TenFastFingers(root)
root.mainloop()
