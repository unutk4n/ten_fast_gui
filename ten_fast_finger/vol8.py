from tkinter import *
from tkinter import ttk

left_to_right = "E,S"
all_area = "N,W,E,S"
from_top_to_bottom = "N,W"
average_font = ("times", 14, "bold")
to_top = "N"

# https://tcl.tk/man/tcl8.6/TkCmd/keysyms.htm  keyboard specific numbers

# the geometry options is useful but there is a con about it.
# even if you change the geometry parameter the widgets won't move
# at least that is what I have experienced. New note
# there is columnconfigure and rowconfigure for that.


class TenFastFingers:

    def __init__(self, master):
        self.master = master
        master.title("Ten Fast Fingers GUI")
        # master.geometry("800x500")

        self.mainframe = ttk.Frame(master, padding="3 3 12 12")
        self.mainframe.grid(sticky=all_area)

        # top-left
        self.text = Text(self.mainframe, width=40, height=10)
        self.text.grid(column=0, row=0, padx=20, pady=20)
        self.text.insert('1.0', "This is an example of the text buttons\n"
                                "This is an example of the text buttons")

        self.label = ttk.Label(self.mainframe, background="yellow", font=average_font, text="Words will show up here !")
        self.label.grid(column=3, row=0, padx=20, pady=20, sticky=to_top)

        self.entry_var = StringVar()
        self.word = StringVar.get(self.entry_var)
        self.entry = ttk.Entry(self.mainframe, font=average_font, textvariable=self.entry_var)
        self.entry.grid(column=3, row=0, padx=20, pady=20)
        # self.entry.focus_set()

        self.button = ttk.Button(self.mainframe, text="Bas Kardeşim", command=self.button_func, width=30)
        self.button.grid(column=0, row=3, padx=20, pady=20)

        self.button1 = ttk.Button(self.mainframe, text="Disable text edit option", command=self.disable, width=30)
        self.button1.grid(column=3, row=3, padx=20, pady=20)

        self.button2 = ttk.Button(self.mainframe, text="Enable text edit option", command=self.enable, width=30)
        self.button2.grid(column=0, row=6, padx=20, pady=20)

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

    def disable(self):
        self.text['state'] = 'disabled'

    def enable(self):
        self.text['state'] = 'normal'


root = Tk()

TenFastFingers(root)

root.mainloop()
