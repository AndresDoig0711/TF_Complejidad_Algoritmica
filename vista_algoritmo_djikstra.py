from tkinter import *

import matplotlib.pyplot as plt
import math as mth

import tkinter.font as font

def openDjikstra():
    vista_djikstra()


def vista_djikstra():
    newWindow = Tk()
    newWindow.title('Algoritmo de Djikstra')
    newWindow.geometry("1470x1200+10+20")

    myFont = font.Font(family='Helvetica bold', size = 26)
    #coordenada de la unidad policial
    unidad = [-77.01939734425481,-12.073981078922287]
    #coordenada de la escena de crimen
    crimen = [-77.021939734425481, -12.02078922287]
    graficarCoodenadas(unidad, crimen)

    bg2 = PhotoImage(file="images/plot.png", master=newWindow)
    canvas2 = Canvas(newWindow, width=1470, height=1200)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg2, anchor = "n")

    label1 = Label(newWindow, text=distancia(unidad, crimen), bg = "white")
    label1.pack(pady = 30)
    label1.config(font=myFont)

    newWindow.mainloop()

def graficarCoodenadas(unidad, crimen):
    #rango de coordenadas de la imagen
    BBox2 = ((-77.3, -76.75,-12.3, -11.788))
    img2 = plt.imread("images/mapa_lima.PNG")

    #rangos de la imagen a mostrar en la pantalla
    fig, ax = plt.subplots(figsize = (10,10))

    ax.scatter(unidad[0], unidad[1], zorder=1, alpha= 0.3, c='blue', s=500)
    ax.scatter(crimen[0], crimen[1], zorder=1, alpha= 0.3, c='red', s=500)


    ax.set_title('Plotting Spatial Data on Lima Map')
    ax.set_xlim(BBox2[0],BBox2[1])
    ax.set_ylim(BBox2[2],BBox2[3])

    #plot linea entre las dos coordenadas
    x,y = [unidad[0], crimen[0]], [unidad[1], crimen[1]]
    ax.plot(x,y)

    #abrir ventana con imagen, puntos y lineas 
    ax.imshow(img2, zorder=0, extent = BBox2, aspect= 'equal')
    #plt.show()
    plt.savefig("images/plot.png")
    
def distancia(unidad, crimen):
    d = 100*mth.sqrt(((crimen[0]-unidad[0])**2)+((crimen[1]-unidad[1])**2))
    str1 = "Distancia entre los dos puntos:",round(d,3),"km"
    return str1