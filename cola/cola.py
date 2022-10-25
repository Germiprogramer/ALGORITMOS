class Nodo():
    def __init__(self, info):
        self.info = info
        self.sig = None

class Cola():
    def __init__(self):
        self.principio = None
        self.final = None
        self.tamanio = 0

    def get_final(self):
        return self.final.info
    
    def arribo(self, dato):
        print("Añadiendo {} al final de la cola".format(dato))
        if self.principio == None:
            self.principio = Nodo(dato)
        elif self.final.info == self.principio.info:
            self.principio.sig = Nodo(dato)
        else:
            self.final.sig = Nodo(dato)

        #DUDA, NO CONSIGO QUE SE AÑADAN MÁS DE DOS ELEMENTOS
        self.final = Nodo(dato)
        self.tamanio +=1
    
    def atencion(self):
        #Atiende el elemento al inicio de la cola
        dato = self.principio.info
        print("Atendiendo {}".format(dato))
        self.principio = self.principio.sig
        if self.principio is None:
            self.final = None
        self.tamanio -= 1
        return dato

    def cola_vacia(self):
        #Devuelve true si la cola está vacía
        return self.principio is None

    def principio(self):
        return self.principio.info

    def tamanio(self):
        return self.tamanio
    
    def mover_al_final(self):
        #Mueve el elemento al frente de la cola al final
        dato = self.principio.info
        self.principio = self.principio.sig
        print("Añadiendo {} al final de la pila".format(dato))
        if self.principio == None:
            self.principio = Nodo(dato)
        else:
            self.final.sig = Nodo(dato)
        self.final = Nodo(dato)
        return dato

    def imprimir(self):
        print("Imprimiendo cola: ")
        #recorriendo la pila e imprimir valores
        nodo_temporal = self.principio
        while nodo_temporal != None:
            print("{}".format(nodo_temporal.info))
            nodo_temporal = nodo_temporal.sig
        print("")
        


c = Cola()
c.arribo("hola")
print(c.get_final())

c.arribo("b")

c.arribo("c")
c.imprimir()

c.imprimir()
