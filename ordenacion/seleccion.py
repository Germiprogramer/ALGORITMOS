#recorre iterativamente la lista de elemento en busca del menors y luego lo selecciona para ubicarlo
# a la izquierda de la lista. Es decir, selecciona el "mejor" elemento, para ubicarlo en su posicion

def seleccion(lista):
    for i in range(0, len(lista)-1):
        minimo = i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista


print(seleccion([3,2,7,8,1,9]))