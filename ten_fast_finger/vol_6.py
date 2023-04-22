from tkinter import *
from tkinter import ttk
import os
left_to_right = "E,S"
all_area = "N,W,E,S"

# BAŞLAMADAN ÖNCE OKU : BUTONUN İŞLEVİNİ EKRAN KORUYUCUYU AÇ OLARAK AYARLADIM
# NEREDE KALDIN: ENTER TUŞUNA BASILDIĞINDA ENTRY KISMININ SİLİNMESİ İÇİN UĞRAŞTIM ANCAK KAFAM DURDU
# BİR DE CLASS OLAYNI DAHA İYİ ANLAMAN LAZIM.
class TenFastFingers:
    # inside the init func There will be only widgets.
    def __init__(self, master):
        self.master = master
        master.title("Ten Fest Fingers Graphical User Interface a.k.a GUI")
        master.geometry("800x500")

        self.label = ttk.Label(master, text="Let's try if that works")
        self.label.grid(column=0, row=0)

        self.entry_var = StringVar()
        self.entry = ttk.Entry(master,textvariable=self.entry_var)
        self.entry.grid(columnspan=2,row=2, sticky=(left_to_right))
        self.entry.focus_set()

        self.button = ttk.Button(master, text="Ekran Koruyucuyu Aç! ", command=self.button_func)
        self.button.grid(column=3, row=3)

    def button_func(self):
        os.system('cmd/c "control desk.cpl,,@screensaver"')



    def given_words_func(self):
        pass

    def entry_func(self):
        pass


root = Tk()
TenFastFingers(root)
root.mainloop()
# entry command option yok.
