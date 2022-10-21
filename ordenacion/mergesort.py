#merge te devuelve de forma ordenada dos listas que ya estan ordenadas de serie. Si las listas no estan ordenadas no funciona

def merge(izquierda = list,derecha = list):
    #funcion para ordenar listas
    lista_mezclada = []
    while (len(izquierda) > 0) and (len(derecha)> 0):
        if izquierda[0] < derecha[0]:
            lista_mezclada.append(izquierda.pop(0))
        else:
            lista_mezclada.append(derecha.pop(0))
    if len(izquierda) > 0:
        lista_mezclada += izquierda
    if len(derecha) > 0:
        lista_mezclada += derecha
    return lista_mezclada

print(merge([1,2,3],[0,4,5]))