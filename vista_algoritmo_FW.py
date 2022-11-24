from tkinter import *
from algoritmo_FW import plot_FW
import time

destino = 15 #10
unidad = [-77.016280,-12.113218]

def openFW():
    vista_FW(destino, unidad)


def vista_FW(destino, unidad):
    newWindow = Tk()
    newWindow.title('Algoritmo de Floyd Warshall')
    newWindow.geometry("1470x1200+10+20")
    plot_FW(destino, unidad)
    bg2 = PhotoImage(file="images/surquillo_plot.png", master=newWindow)
    canvas2 = Canvas(newWindow, width=1470, height=1200)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg2, anchor = 'nw')

    newWindow.mainloop()

