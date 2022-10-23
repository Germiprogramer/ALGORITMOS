class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class Cola():
    def __init__(self):
        self.principio = None
        self.final = None
        self.tamanio = 0
    
    def arribo(self, dato):
        print("Añadiendo {} al final de la pila".format(dato))
        if self.principio == None:
            self.principio = Nodo(dato)
        else:
            self.final.sig = Nodo(dato)
        self.final = Nodo(dato)
        self.tamanio +=1
    
    def atencion(self):
        #Atiende el elemento al inicio de la cola
        dato = self.principio.dato
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
        return self.principio.dato

    def tamanio(self):
        return self.tamanio
    
    def mover_al_final(self):
        #Mueve el elemento al frente de la cola al final
        dato = self.principio.dato
        arribo(dato)


c = Cola()
c.arribo("hola")
c.atencion()
