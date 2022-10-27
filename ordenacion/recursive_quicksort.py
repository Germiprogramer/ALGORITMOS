
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        return (
            quick_sort([e for e in lista[1:] if e <= lista[0]])
            + [lista[0]]
            + quick_sort([e for e in lista[1:] if e > lista[0]])
        )   

#print(quick_sort_recursivo([3,2,1,4,1], 0, 4))

print(quick_sort([3,2,1,4,1]))