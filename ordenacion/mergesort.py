#merge te devuelve de forma ordenada dos listas que ya estan ordenadas de serie. Si las listas no estan ordenadas no funciona

def merge(lista):
    #funcion para ordenar listas
    mitad = len(lista) // 2
    
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    l_izquierda = len(izquierda)
    l_derecha = len(derecha)

    merge(izquierda)
    merge(derecha)

    indice_izq = 0
    indice_der = 0
    indice = 0

    
    while (indice_izq < l_izquierda) and (indice_der < l_derecha):
        if izquierda[indice_izq] < derecha[indice_der]:
            lista[indice] = izquierda[indice_izq]
            indice_izq += 1
        else:
            lista[indice] = derecha[indice_der]
            indice_der += 1
        indice +=1
    
    while(indice_izq < l_izquierda):
        lista[indice] = izquierda[indice_izq]
        indice_izq += 1
        indice += 1
    
    while(indice_der < l_derecha):
        lista[indice] = derecha[indice_der]
        indice_der += 1
        indice += 1
    
    return lista

print(merge([1,2,3,0,4,5]))

lista = [1,2,3,4,5]
