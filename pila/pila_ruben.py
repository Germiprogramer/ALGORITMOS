class nodoPila(object):
    #Clase nodo pila
    info, sig = None, None

class Pila(object):
    #clase pila

    def __init__(self):
        #crea una pila vacia
        self.cima = None
        self.tamanio = 0

def apilar(pila, dato):

    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1

def desapilar(pila):
    #desapila el elemento en la cima de la pila y te devuelve
    x = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return x

def pila_vacia(pila):
    #Devuelve true si la pila está vacia
    return pila.cima is None

def en_cima(pila):
    #Devuelve el valor almacenado en la cima de la pila
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None

def tamanio(pila):
    #devuelve el numero de elementos en la pila
    return pila.tamanio

