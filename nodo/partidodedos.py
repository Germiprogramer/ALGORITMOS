#nofunciona

class Nodo(object):
    info, sig = None,None

nodo = Nodo()
nodo.info = "a"

def partidodedos(n):
    contador = 0
    if n%2 == 0:
        pass
    else:
        if nodo.info == "a":
            nodo.info = contador
            print(nodo.info)
        nodo.info+=1
        partidodedos(n/2)
    return nodo.info

print(partidodedos(16))