class Nodo:
    #Creamos la clase Nodo definiendo en el contructor el dato a almacenar
    #Queda por definir el puntero, que definirá el siguiente elemento en la cola
    def __init__(self,dato):
        self.dato = dato
        self.sig = None

class Pila:
    #en una Pila lo más importante es definir el elemento superior, porque va a ser sobre el que se actuará todo el rato
    def __init__(self):
        self.superior = None

    def apilar(self,dato):
        print("Agregando {} en la cima de la pila".format(dato))
        #Si no hay dato, agregamos el valor del elemento superior y desapilamos
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.sig = self.superior
        self.superior = nuevo_nodo

