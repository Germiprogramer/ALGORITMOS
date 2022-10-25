class Nodo:
    #Creamos la clase Nodo definiendo en el contructor el dato a almacenar
    #Queda por definir el puntero, que definirá el siguiente elemento en la cola
    def __init__(self,info):
        self.info = info
        self.sig = None

class Pila:
    #en una Pila lo más importante es definir el elemento superior, porque va a ser sobre el que se actuará todo el rato
    def __init__(self):
        self.superior = None
        self.tamanio = 0

    def apilar(self,dato):
        print("Agregando {} en la cima de la pila".format(dato))
        #Si no hay dato, agregamos el valor del elemento superior y desapilamos
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.sig = self.superior
        self.superior = nuevo_nodo
        self.tamanio += 1

    def desapilar(self):
        #Si no hay datos en el nodo superior, regresamos
        if self.superior == None:
            print("No hay ningún elemento en la cola")
            return
        print("Desapilar {}".format(self.superior.info))
        self.superior = self.superior.sig
        self.tamanio -=1
    
    def imprimir(self):
        print("Imprimiendo pila: ")
        #recorriendo la pila e imprimir valores
        nodo_temporal = self.superior
        while nodo_temporal != None:
            print("{}".format(nodo_temporal.info))
            nodo_temporal = nodo_temporal.sig
        print("")

    def pila_vacia(self):
    #Devuelve true si la pila está vacia
        return self.superior is None

    def en_cima(self):
    #Devuelve el valor almacenado en la cima de la pila
        if self.superior is not None:
            return self.superior.info
        else:
            return None

    #DUDA NO FUNCIONA
    def tamanio(self):
    #devuelve el numero de elementos en la pila
        return self.tamanio


