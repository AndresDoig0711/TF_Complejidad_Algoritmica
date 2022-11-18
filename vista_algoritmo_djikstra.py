from tkinter import *

def openDjikstra():
    vista_djikstra()


def vista_djikstra():
    newWindow = Tk()
    newWindow.title('Algoritmo de Djikstra')
    newWindow.geometry("1470x1200+10+20")
    bg2 = PhotoImage(file="images/mapa_lima.png", master=newWindow)
    canvas2 = Canvas(newWindow, width=1470, height=1200)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg2, anchor = "nw")
    newWindow.mainloop()

