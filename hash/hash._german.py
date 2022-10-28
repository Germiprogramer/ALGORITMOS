def bernstein(texto):
    texto = str(texto)
    h = 0
    for letra in texto:
        h = h*33 +ord(letra)
    return h

def siguiente_primo(n):
    if n < 0:
      raise ValueError
  
    for next in range(n + 1, n +200):
        if next > 1:
            for i in range(2, next):
                if (next % i) == 0:
                    break
                else:
                    return next

class Tabla_Hash():
    
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tabla = [None] * tamanio
        self.keys = {}
    
    def cantidad_elementos(self):
        return (self.tamanio - self.tabla.count(None))

    def funcion_hash(self, dato):
    #hash por division en este caso
        return bernstein(dato)%self.tamanio

    def poner_valor(self, posicion, dato):
        self.tabla[posicion] = dato
        self.keys[posicion] = dato

    def colision(self, posicion, dato):
        #doble hash
        nueva_posicion = self.funcion_hash(posicion+1)
        while self.tabla[nueva_posicion] is not None and self.tabla[posicion] != posicion:
            if self.tabla.count(None) > 0:
                nueva_posicion = self.funcion_hash(nueva_posicion+1)
            else:
                nueva_posicion = None
                break
        return nueva_posicion

    def rehashing(self):
        datos_tabla_destruida = [valor for valor in self.tabla if valor is not None]
        sig_primo = siguiente_primo(self.tamanio)
        sig_primo2 = siguiente_primo(sig_primo)
        self.tamanio = sig_primo2
        self.keys = {}
        self.tabla = [None] * self.tamanio
        for valor in datos_tabla_destruida:
            self.insertar(valor)
        
    def calcular_limite(self):
        return (self.tamanio *75 // 100)


    def insertar(self, dato):
        posicion = self.funcion_hash(dato)
        if (self.tabla[posicion] is None):
            self.poner_valor(posicion,dato)
        
        elif self.tabla[posicion] == dato:
            pass
        
        else:
            print("se produjo una colisión")
            solucion_colision = self.colision(posicion, dato)
            if solucion_colision is not None:
                self.poner_valor(solucion_colision, dato)
            else:
                print("no hay hueco")
        #n = len(self.tabla)*75/100       
        #if self.cantidad_elementos >= n:
            #self.rehashing()
            #self.insertar(dato)
            


        

    

#creacion tabla vacia
t = Tabla_Hash(8)
print(t.tabla)

t.insertar("hola")
print(t.tabla)
t.insertar("halo")
print(t.keys)
t.insertar("chupala")
t.insertar("chupala")
print(t.keys)

print(siguiente_primo(5))

print(t.calcular_limite())