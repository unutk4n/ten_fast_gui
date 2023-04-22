"""from tkinter import *
from tkinter import ttk

most_common_words = ["A", "about", "after", "all", 
                     "also", "an", "and", "any", "are",
                       "as", "at", "be", "because", "been",
                         "but", "by", "can", "could", "day",
                           "do", "even", "for", "from", "get",
                             "give", "go", "good", "have", "he",
                               "her", "here", "him", "his", "how",
                                 "I", "if", "in", "into", "is", "it",
                                   "its", "just", "know", "like", "look",
                                     "make", "me", "most", "my", "new", "no",
                                       "not", "now", "of", "on", "one", "only",
                                         "or", "other", "our", "out", "over",
                                           "people", "say", "see", "she", "so",
                                             "some", "take", "tell", "than", "that",
                                               "the", "their", "them", "then", "there",
                                                 "these", "they", "thing", "think", "this",
                                                   "those", "time", "to", "two", "up", "use",
                                                     "very", "want", "way", "we", "well", "what",
                                                       "when", "which", "who", "will", "with", "would",
                                                         "year", "you", "your"]
root = Tk()
root.geometry("700x700")
root.title("10 F4ST F1NG3RS")


# ANA KARE
mainframe = ttk.Frame(root,width=500,height=500)
mainframe.grid(sticky=(N,W,E,S))
#######################################


# YAZILMASI İSTENEN KELİMELER
yazilacak = ttk.Label(mainframe,text=most_common_words)
yazilacak.grid(padx=5,pady=5 , sticky=(W,E))
#########################################


# YAZMA ALANI
words = StringVar()
gir = ttk.Entry(mainframe,width=25,textvariable=words)
gir.grid(column=2,row=3,ipadx=2,ipady=2,sticky=(W,E))
####################################







root.mainloop()"""
import tkinter as tk

window = tk.Tk()
window.title = ("BİRTAKIM KELİME OYUNLARI")

kelime = tk.Label(window, 
                  text="ANANI SİKEM TKİNTER",
                  foreground="white",
                  background="black",
                  width=50,
                  height=25)
kelime.pack()

gir = tk.Entry(foreground="black",
               background= "white",
               width=50)
gir.pack()

window.mainloop()



"""
tkinter üzerindeki widget'ların hepsi birer class olduğu için her birinin komutları aynı olmayabilir.
Label	A widget used to display text on the screen
    width ve heigt oluyor
Button	A button that can contain text and can perform an action when clicked
Entry	A text entry widget that allows only a single line of text
Text	A text entry widget that allows multiline text entry
Frame	A rectangular region used to group related widgets or provide padding between widgets
"""