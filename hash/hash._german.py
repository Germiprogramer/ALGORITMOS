def bernstein(texto):
    h = 0
    for letra in texto:
        h = h*33 +ord(letra)
    return h

class Tabla_Hash():
    
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tabla = [None] * tamanio
        self.key

    def funcion_hash(self, dato):
    #hash por division en este caso
        return bernstein(dato)%self.tamanio

    #def corregir_colision(posicion, dato, self):


    def insertar(self, dato):
        posicion = self.funcion_hash(dato)
        if (self.tabla[posicion] is None):
            self.tabla[posicion] = dato
        else:
            print("se produjo una colisión")
        

    

#creacion tabla vacia
t = Tabla_Hash(8)
print(t.tabla)

t.insertar("hola")
print(t.tabla)
t.insertar("halo")