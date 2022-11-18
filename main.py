from tkinter import *
from vista_algoritmo_djikstra import * 
from vista_algoritmo_FW import *


def main():
    window = Tk()
    window.title('Proyecto Final de Complejidad Algoritmica')
    window.geometry("1470x1200+10+20")
    bg = PhotoImage(file="images/mapa_lima_blur.png", master=window)
    canvas = Canvas(window, width=1470, height=1200)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor = "nw")
    label1 = Label(canvas, text="Aplicación de algoritmos para la detección de la ruta más corta a la escena de crimen.", bg = "white")
    label1.pack(pady = 20)
    label1.config(font=('Helvetica bold', 26))
    button1 = Button(canvas, text = "Algoritmo de Djikstra", command=openDjikstra)
    button1.pack(pady = 100)
    button2 = Button(canvas, text = "Algoritmo de Floyd-Warshall", command=openFW)
    button2.pack(pady = 100)
    window.mainloop()

#if __name__ == '__main__':
main()
