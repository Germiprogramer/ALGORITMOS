from numpy import angle


class Nodo():
    def __init__(self, info):
        self.info = info
        self.sig = None

class Lista():
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


def insertar(lista, dato):
        nodo = Nodo(dato)
        if lista.inicio == None or lista.inicio.info > dato:
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while (act is not None and act.info < dato):
                ant = ant.sig
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        lista.tamanio += 1 
    
def imprimir(lista):
        print("Imprimiendo lista: ")
        #recorriendo la pila e imprimir valores
        nodo_temporal = lista.inicio
        while nodo_temporal != None:
            print("{}".format(nodo_temporal.info))
            nodo_temporal = nodo_temporal.sig
        print("")
    
def lista_vacia(lista):
        return lista.inicio == None

def eliminar(lista, clave):
        dato = None
        if lista.inicio.info == clave:
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamanio -=1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while actual is not None and actual.info != clave:
                anterior = anterior.sig
                actual = actual.sig
            if actual is not None:
                dato = actual.info
                anterior.sig = actual.sig
                lista.tamanio -=1
        return dato

def tamanio(lista):
        return lista.tamanio

def buscar(lista, buscado):

        aux = lista.inicio
        while(aux is not None and aux.info != buscado):
            aux = aux.sig
        return aux

#CAMPO




c = Lista()
insertar(c,1)
insertar(c,2)
insertar(c,0)
eliminar(c,1)
imprimir(c)




