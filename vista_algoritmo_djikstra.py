from tkinter import *
from algoritmo_djikstra import plot_Djikstra
import tkinter.font as font
from io import StringIO
import sys

def openDjikstra():
    vista_Djikstra()


def vista_Djikstra():
    newWindow = Tk()
    newWindow.title('Algoritmo de Djikstra')
    newWindow.geometry("1470x1200+10+20")
    plot_Djikstra()
    new_stdout = StringIO()
    sys.stdout = new_stdout


    myFont = font.Font(family='Helvetica bold', size = 26)

    label1 = Label(newWindow, text=new_stdout.getvalue(), bg = "white")
    label1.pack(pady = 30)
    label1.config(font=myFont)

    newWindow.mainloop()
