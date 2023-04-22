from tkinter import *
from tkinter import ttk

# MAY THE POWER OF HARD WORK BE ON MY SIDE ! !  13th April 2023

left_to_right = "W,E"
up_to_down = "N,S"   # BU TANIMLAMALARI SAĞDA SOLDA GÖRMEDİM YANLIŞ ANLAŞILMASIN SAYGILAR :)
to_everywhere = "N,W,E,S"

most_common_words = ["A", "about", "after", "all", "also", "an",
                     "and", "any", "are", "as", "at", "be", "because", "been"]

listing = []
count_the_words = 0


def show_words(most_common_words):
    # buradaki fonksiyonu aşağısı ile birleştiremedim. daha doğrusu vaktım yetmedi.

    for word in most_common_words:
        count_the_words + 1
        listing.append(word)
        if count_the_words == 5:
            break
        else:
            pass

# that is the title of this program and will be displayed on the top of the program
#   right now I don't know what padding is, but we'll see soon enough.


root_frame = Tk()


root_frame.title("Fast Typing Program !")
root_frame.geometry("500x400")
main_frame = ttk.Frame(root_frame, padding="3 3 12 12")
main_frame.grid(column=0, row=0, sticky=(to_everywhere))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)


to_write = ttk.Label(main_frame, text="This text will be shown here ! ")
to_write.grid(column=0, row=0, sticky=(left_to_right))


writing = StringVar()
writing_area = ttk.Entry(main_frame, textvariable=writing)
writing_area.grid(column=2, row=2, sticky=(left_to_right))


root_frame.mainloop()

# Things I am unfamiliar with.
"""
padding
columnconfigure
rowconfigure inside both of the configure methods there is a weight parameter which I don't know as well.
"""