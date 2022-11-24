from tkinter import *
from vista_algoritmo_djikstra import * 
from vista_algoritmo_FW import *
import tkinter.font as font


def main():
    window = Tk()
    window.title('Proyecto Final de Complejidad Algoritmica')
    window.geometry("1470x1200+10+20")

    myFont = font.Font(family='Helvetica bold', size = 26)

    bg = PhotoImage(file="images/mapa_lima_blur.png", master=window)
    canvas = Canvas(window, width=1470, height=1200)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor = "nw")

    label1 = Label(canvas, text="Aplicación de algoritmos para la detección de la ruta más corta a la escena de crimen.", bg = "white")
    label1.pack(pady = 30)
    label1.config(font=myFont)

    button1 = Button(canvas, text = "Algoritmo de Djikstra",
    height=2, width=20, bg='#0052cc', fg='#ffffff', command=openDjikstra)
    button1['font'] = myFont
    button1.pack(pady = 200)

    button2 = Button(canvas, text = "Algoritmo de Floyd-Warshall", 
    height=2, width=25, bg='#0052cc', fg='#ffffff', command=openFW)
    button2['font'] = myFont
    button2.pack(pady = 50)
    
    window.mainloop()

main()
