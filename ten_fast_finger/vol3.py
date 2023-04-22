from tkinter import *
from tkinter import ttk

# MAY THE POWER OF HARDWORK BE ON MY SIDE ! !  13th April 2023

left_to_right = "W,E"
up_to_down = "N,S"   # BU TANIMLAMALARI SAĞDA SOLDA GÖRMEDİM YANLIŞ ANLAŞILMASIN SAYGILAR :)
to_everwhere = "N,W,E,S"

most_common_words = ["A", "about", "after", "all","also", "an", "and", "any", "are","as", "at", "be", "because", "been"]

listing =[]

def show_words(most_common_words):
    
    for word in most_common_words:      # buradaki fonksiyonu aşağısı ile birleştiremedim. daha doğrusu vaktım yetmedi.
        
        
        
        if listing.__len__ == 6:
            continue
        else:
            break



root_frame = Tk()
root_frame.title("Fast Typing Program !") # that is the title of this program and will be displayed on the top of the program
#root_frame.geometry("500x400")
main_frame = ttk.Frame(root_frame,padding="3 3 12 12") # right now I don't know what padding is but we'll see soon enough.
main_frame.grid(column=0, row=0,sticky=(to_everwhere))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)


to_write = ttk.Label(main_frame,text="This text will be shown here ! ")
to_write.grid(column=0,row=0,sticky=(left_to_right))


writing = StringVar()
writing_area = ttk.Entry(main_frame, textvariable=writing)
writing_area.grid(column=2,row=2,sticky=(left_to_right))



root_frame.mainloop()













# Things I am unfamiliar with.
"""
padding
columnconfigure
rowconfigure inside both of the configure methods there is a weight parameter which I don't know as well.
"""