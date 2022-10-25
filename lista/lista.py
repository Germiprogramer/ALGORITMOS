from numpy import angle


class Nodo():
    def __init__(self, info):
        self.info = info
        self.sig = None

class Lista():
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.inicio == None or self.inicio.info > dato:
            nodo.sig = self.inicio
            self.inicio = nodo
        else:
            ant = self.inicio
            act = self.inicio.sig
            while (act is not None and act.info < dato):
                ant = ant.sig
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        self.tamanio += 1 
    
    def imprimir(self):
        print("Imprimiendo lista: ")
        #recorriendo la pila e imprimir valores
        nodo_temporal = self.inicio
        while nodo_temporal != None:
            print("{}".format(nodo_temporal.info))
            nodo_temporal = nodo_temporal.sig
        print("")
    
    def lista_vacia(self):
        return self.inicio == None

    def eliminar(self, clave):
        dato = None
        if self.inicio.info == clave:
            dato = self.inicio.info
            self.inicio = self.inicio.sig
            self.tamanio -=1
        else:
            anterior = self.inicio
            actual = self.inicio.sig
            while actual is not None and actual.info != clave:
                anterior = anterior.sig
                actual = actual.sig
            if actual is not None:
                dato = actual.info
                anterior.sig = actual.sig
                self.tamanio -=1
        return dato

    def tamanio(self):
        return self.tamanio

    def buscar(self, buscado):

        aux = self.inicio
        while(aux is not None and aux.info != buscado):
            aux = aux.sig
        return aux

#CAMPO




c = Lista()
c.insertar(1)
c.insertar(2)
c.insertar(0)
c.eliminar(1)
c.imprimir()




