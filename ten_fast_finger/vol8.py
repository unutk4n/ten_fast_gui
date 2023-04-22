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

        self.label = ttk.Label(master, background="yellow", font=average_font, text="Words will show up here !")
        self.label.grid(columnspan=20, row=0, padx=20, pady=20)

        self.entry_var = StringVar()
        self.word = StringVar.get(self.entry_var)
        self.entry = ttk.Entry(master, font=average_font, textvariable=self.entry_var)
        self.entry.grid(columnspan=20, row=2, padx=20, pady=20)
        self.entry.focus_set()

        self.button = ttk.Button(master, text="Bas Kardeşim", command=self.button_func, width=30)
        self.button.grid(column=3, row=3, padx=20, pady=20)

        self.button1 = ttk.Button(master, text="birşeyler yaz da öyle bas", command=self.deneme, width=30)
        self.button1.grid(column=4, row=4, padx=20, pady=20)

        self.label.bind('<Return>', lambda x: self.space_key_func())

        """self.seperator = ttk.Separator(master, orient=HORIZONTAL)
        self.seperator.place(relx=0, rely=0.47, relwidth=1, relheight=1)"""


        # PLACE VE GRİD AYNI PARENT ÜZERİNDE OLMAMALI O YÜZDEN GRİD İLE YAZMANIN BİR YOLUNU BUL

    def button_func(self):
        print("Tebrikler amın oğlu")
        self.label.config(text="Tebrikler aq")

    def space_key_func(self):
        f = open("append.txt", "a")
        f.write(self.word)
        f.close()

    def deneme(self):
        print(self.word)


root = Tk()

TenFastFingers(root)

root.mainloop()
