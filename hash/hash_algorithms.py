def bernstein(texto):
    h = 0
    for letra in texto:
        h = h*33 +ord(letra)
    return h

class TablaHash():
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tabla = [None]*tamanio

t = TablaHash(8)
print(t.tabla)

def funcion_hash(dato, tamanio_tabla):
    #hash por division en este caso
    return bernstein(dato)%tamanio_tabla

