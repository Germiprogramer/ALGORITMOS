def ordenacion_conteo(lista):
    maximo = max(lista)
    minimo = min(lista)

    lista_ordenada = [0] * len(lista)
    lista_conteo = [0] * (maximo +1 -minimo)

    #cuenta cuantas veces aparece un número en la lista
    for numero in lista:
        lista_conteo[numero -minimo] +=1
    print("Lista conteo:  ", lista_conteo)
    #suma cada posicion con sus predecesores, ahora nos dirá cuantos elementos menores o iguales que i existen en la col
    for i in range(1, len(lista_conteo)):
        lista_conteo[i] = lista_conteo[i] + lista_conteo[i-1]

    for i in reversed(range(0,len(lista))):
        lista_ordenada[lista_conteo[lista[i]- minimo]-1] = lista[i]
        lista_conteo[lista[i]-minimo]-= 1
    return lista_ordenada

print(ordenacion_conteo([3,1,4,3,5,14,0]))
        