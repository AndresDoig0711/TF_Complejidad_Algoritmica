from tkinter import *
import matplotlib.pyplot as plt

import numpy as np
import math

def plot_Djikstra():
    class Nodo:	
        def __init__(self, i):
        
            self.id = i
            self.vecinos = []
            self.visitado = False
            self.padre = None
            self.costo = float('inf')

        def agregarVecino(self, v, p):		
            if v not in self.vecinos:
                self.vecinos.append([v, p])

    class Grafo:	
        def __init__(self):
            self.nodo = {}

        def agregarNodo(self, id):		
            if id not in self.nodo:
                self.nodo[id] = Nodo(id)

        def agregarArista(self, a, b, p):		
            if a in self.nodo and b in self.nodo:
                self.nodo[a].agregarVecino(b, p)
                self.nodo[b].agregarVecino(a, p)
            
        def camino(self, a, b):		
            camino = []
            actual = b
            while actual != None:
                camino.insert(0, actual)
                actual = self.nodo[actual].padre
            return [camino, self.nodo[b].costo]

        def minimo(self, l):		
            if len(l) > 0:
                m = self.nodo[l[0]].costo
                v = l[0]
                for e in l:
                    if m > self.nodo[e].costo:
                        m = self.nodo[e].costo
                        v = e
                return v
            return None

        def dijkstra(self, a):		
            if a in self.nodo:	
                self.nodo[a].costo = 0
                actual = a
                noVisitados = []
                
                for v in self.nodo:
                    if v != a:
                        self.nodo[v].costo = float('inf')
                    self.nodo[v].padre = None
                    noVisitados.append(v)

                while len(noVisitados) > 0:
                    
                    for vec in self.nodo[actual].vecinos:
                        if self.nodo[vec[0]].visitado == False:
                        
                            if self.nodo[actual].costo + vec[1] < self.nodo[vec[0]].costo:
                                self.nodo[vec[0]].costo = self.nodo[actual].costo + vec[1]
                                self.nodo[vec[0]].padre = actual
                    
                    self.nodo[actual].visitado = True
                    noVisitados.remove(actual)                				
                    actual = self.minimo(noVisitados)
            else:
                return False

    class main:
        g = Grafo()
        g.agregarNodo('A')
        g.agregarNodo('B')
        g.agregarNodo('C')
        g.agregarNodo('D')
        g.agregarNodo('E')
        g.agregarNodo('F')
        
        g.agregarArista('A', 'F', 14)
        g.agregarArista('A', 'B', 2)
        g.agregarArista('A', 'C', 9)
        g.agregarArista('B', 'C', 10)
        g.agregarArista('B', 'D', 15)
        g.agregarArista('C', 'D', 11)
        g.agregarArista('C', 'F', 2)
        g.agregarArista('D', 'E', 6)
        g.agregarArista('E', 'F', 9)

        print("\n\nLa ruta más rápida por Dijkstra junto con su costo es:")
        g.dijkstra('B')
        print(g.camino('B', 'E'))