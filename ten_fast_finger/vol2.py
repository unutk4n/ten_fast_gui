




























import tkinter as tk

window = tk.Tk()
window.title = ("BİRTAKIM KELİME OYUNLARI")
cerceve = tk.Frame()
kelime = tk.Label(window,
                  text="ANANI SİKEM TKİNTER",
                  foreground="blue",
                  background="green",
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
#Entry metotunun get, delete gibi metotları var ve ayrıca kendimiz de enter tuşuna bastığımzda şu
# olsun gibi komutlar oluşturabiliriz.
"""
GALİBA BU MODUL BİZ ONU ANLAYANA KADAR BİRAZ YORACAK
AMA ANLAYACAM OĞLUM SENİ
"""