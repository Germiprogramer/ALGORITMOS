#high y low es el intervalo de busqueda

def binary_search(lista, menor, mayor, busqueda):
 
    # Check base case
    if mayor >= menor:
 
        mid = (mayor + menor) // 2
 
        # If element is present at the middle itself
        if lista[mid] == busqueda:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif lista[mid] > busqueda:
            return binary_search(lista, menor, mid - 1, busqueda)
             # Else the element can only be present in right subarray
        else:
            return binary_search(lista, mid + 1, mayor, busqueda)
 
    else:
        # Element is not present in the array
        return -1