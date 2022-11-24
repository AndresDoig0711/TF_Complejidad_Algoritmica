from tkinter import *
import matplotlib.pyplot as plt

import numpy as np
import math


def plot_FW(destino, unidad):
    def floydWarshall(G):
        n = len(G)
        cost = np.full((n, n), math.inf)
        path = np.full((n, n), -1, dtype=int)

        for u in range(n):
            for v, w in G[u]:
                cost[u, v] = w
                path[u, v] = u

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i != j and j != k and k != i:
                        f = cost[i, k] + cost[k, j]
                        if f < cost[i, j]:
                            cost[i, j] = f
                            path[i, j] = path[k, j]

        return cost, path
        

    with open("1201a.al") as f:
        G = []
        for line in f:
            if line == '-\n':
                G.append([])
            else:
                nums = [int(x) for x in line.split()]
                G.append([(nums[i], nums[i+1]) for i in range(0, len(nums), 2)])

    for x in G:
        print(x)


    cost, path = floydWarshall(G)

    def findPath(path,ini,fin):
    
        Arr = path[ini]
        Arr = Arr[0:fin+1]
        indices = np.where(Arr==-1)
        Arr = np.delete(Arr, indices)

        new_list = []

        for i in Arr:
            if i != Arr[len(Arr)-1]:
                if i not in new_list:
                    new_list.append(i)
                    j = len(new_list)-1
                else:
                    if new_list[j] != i:
                        new_list.remove(new_list[j])
                        while new_list[j-1] != i:
                            new_list.remove(new_list[j-1])
                            j -= 1
            else:
                if i not in new_list:
                    new_list.append(i)
                break
                

        return new_list

    print(findPath(path,0,13))
    #rango de coordenadas de la imagen
    BBox2 = ((-77.016380, -77.01473382354172,-12.115560,-12.112835707759556))

    img2 = plt.imread("images/surquillo.png")

    #rangos de la imagen a mostrar en la pantalla
    fig, ax = plt.subplots(figsize = (10,10))

    #coordenada de la unidad policial -12.113730993725394, -77.01625830473667
    #unidad = [-77.016280,-12.113218]
    #coordenada de esquinas para establecer limites
    crimen1 = [-77.016242, -12.113734]
    crimen2 = [-77.016185, -12.114601]
    crimen3 = [-77.016146, -12.115001]
    crimen4 = [-77.016104, -12.115518]
    crimen5 = [-77.015866, -12.113190]
    crimen6 = [-77.015651, -12.113172]
    crimen7 = [-77.015431, -12.113172]
    crimen8 = [-77.015251, -12.113151]
    crimen9 = [-77.015414, -12.113381]
    crimen10 = [-77.015240, -12.113349]
    crimen11 = [-77.015817, -12.113695]
    crimen12 = [-77.015608, -12.113685]
    crimen13 = [-77.015385, -12.113664]
    crimen14 = [-77.014932, -12.113625]
    crimen15 = [-77.015545, -12.114573]
    crimen16 = [-77.015445, -12.114569]
    crimen17 = [-77.014869, -12.114513]
    crimen18 = [-77.015559, -12.114969]
    crimen19 = [-77.015424, -12.114948]
    crimen20 = [-77.015527, -12.115475]
    crimen21 = [-77.014819, -12.115415]
    #coordenada de la escena de crimen
    ax.scatter(unidad[0], unidad[1], zorder=1, alpha= 0.3, c='blue', s=500)
    ax.scatter(crimen1[0], crimen1[1], zorder=1, alpha= 0.3, c='yellow', s=300) 
    ax.scatter(crimen2[0], crimen2[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen3[0], crimen3[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen4[0], crimen4[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen5[0], crimen5[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen6[0], crimen6[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen7[0], crimen7[1], zorder=1, alpha= 0.3, c='green', s=300)
    ax.scatter(crimen8[0], crimen8[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen9[0], crimen9[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen10[0], crimen10[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen11[0], crimen11[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen12[0], crimen12[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen13[0], crimen13[1], zorder=1, alpha= 0.3, c='purple', s=300)
    ax.scatter(crimen14[0], crimen14[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen15[0], crimen15[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen16[0], crimen16[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen17[0], crimen17[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen18[0], crimen18[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen19[0], crimen19[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen20[0], crimen20[1], zorder=1, alpha= 0.3, c='yellow', s=300)
    ax.scatter(crimen21[0], crimen21[1], zorder=1, alpha= 0.3, c='red', s=300)


    ax.set_title('Plotting Spatial Data on Lima Map')
    ax.set_xlim(BBox2[0],BBox2[1])
    ax.set_ylim(BBox2[2],BBox2[3])

    #plot linea entre las dos coordenadas
    #destino=10
    puntos = [unidad,crimen1,crimen2,crimen3,crimen4,crimen5,crimen6,crimen7,crimen8,crimen9,crimen10,crimen11,crimen12,crimen13,crimen14,crimen15,crimen16,crimen17,crimen18,crimen19,crimen20,crimen21]
    print(findPath(path,0,destino))
    a = findPath(path,0,destino)
    v=1
    cant=len(a)
    while v<cant: 
        x,y = [puntos[a[v-1]][0], puntos[a[v]][0]], [puntos[a[v-1]][1], puntos[a[v]][1]]
        ax.plot(x,y)
        v=v+1

    x,y = [puntos[a[cant-1]][0], puntos[destino][0]], [puntos[a[cant-1]][1], puntos[destino][1]]
    ax.plot(x,y)
    #abrir ventana con imagen, puntos y lineas 
    ax.imshow(img2, zorder=0, extent = BBox2, aspect= 'equal')
    #plt.show()
    plt.savefig("images/surquillo_plot.png")

    #distancia entre las dos coordenadas



