class Nodo(object):
    info, sig = None,None

aux = Nodo()
aux.info = "primer nodo"
palabra = input("Ingrese una palabra: ")
naux = aux
while palabra != "":
    nodo = Nodo()
    nodo.info = palabra
    nodo.sig = nodo
    naux = nodo
    palabra = input("Ingrese una palabra:  ")

while (aux is not None):
    print(nodo.info)
    aux = aux.sig

nodo = Nodo()
nodo.info = None

def partidodedos(n):
    contador = 0
    if n%2 == 0:
        pass
    else:
        if nodo.info == None:
            nodo.info = contador
        nodo.info+=1
        partidodedos(n/2)
    return nodo.info

print(partidodedos(16))
    
