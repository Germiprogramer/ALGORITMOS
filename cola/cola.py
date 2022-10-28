


class NodoCola():
    def __init__(self, info):
        self.info = info
        self.sig = None

class Cola():
    def __init__(self):
        self.principio = None
        self.final = None
        self.tamanio = 0

def get_final(lista):
        pass
    
def arribo(lista, dato):
        print("Añadiendo {} al final de la cola".format(dato))
        if lista.principio == None:
            lista.principio = NodoCola(dato)
            
        elif lista.principio != None and lista.final == None:
            lista.final = NodoCola(dato)
            lista.principio.sig = lista.final
            

        else:
            lista.final.sig = NodoCola(dato)
            lista.final = NodoCola(dato)

        #DUDA, NO CONSIGO QUE SE AÑADAN MÁS DE DOS ELEMENTOS
        
        lista.tamanio +=1
    
def atencion(lista):
        #Atiende el elemento al inicio de la cola
        dato = lista.principio.info
        print("Atendiendo {}".format(dato))
        lista.principio = lista.principio.sig
        if lista.principio is None:
            lista.final = None
        lista.tamanio -= 1
        return dato

def cola_vacia(lista):
        #Devuelve true si la cola está vacía
        return lista.principio is None

def principio(lista):
        return lista.principio.info

def tamanio(lista):
        return lista.tamanio
    
def mover_al_final(lista):
        #Mueve el elemento al frente de la cola al final
        dato = lista.principio.info
        lista.principio = lista.principio.sig
        print("Añadiendo {} al final de la pila".format(dato))
        if lista.principio == None:
            lista.principio = NodoCola(dato)
        else:
            lista.final.sig = NodoCola(dato)
        lista.final = NodoCola(dato)
        return dato

def imprimir(lista):
        print("Imprimiendo cola: ")
        #recorriendo la pila e imprimir valores
        nodo_temporal = lista.principio
        while nodo_temporal != None:
            print("{}".format(nodo_temporal.info))
            nodo_temporal = nodo_temporal.sig
        print("")
        


c = Cola()
arribo(c,"hola")


arribo(c,"b")

arribo(c,"c")
imprimir(c)

imprimir(c)
